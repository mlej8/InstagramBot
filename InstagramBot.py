from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import time
import datetime
import sqlite3
from account import InstagramAccount 

class InstagramBot():

    # Create class variable to set an uniform loading time of 1s
    PAUSE_TIME = 2

    def __init__(self): 
        """ InstagramBot's constructor. Each time an InstagramBot is created, a driver is automatically instantiated as its instance variable """
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)  # setting an implicit wait. It is good practice to set up an implicit wait right after the driver was created to avoid "NoSuchElementError" and give the browser more time to load.  

    def maximize_window(self):
        """ Method to maximize current browser window """
        self.driver.maximize_window()
        
    def login(self, username, password):
        """ Methods that log in to Instagram by taking user's credentials as parameters"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        try:            
            self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username) # filling username
            self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password) # filling password
            self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()              # submit form
        except NoSuchElementException:
            print("Failed to log in: Unable to locate Username/Password/LogIn element(s)")

        # If login is unsuccessful, Instagram will show a message "Sorry, your password was incorrect. Please double-check your password."
        success = self.driver.find_elements_by_xpath("//p[@id = \"slfErrorAlert\"]")
        if len(success) == 0:
            print("Login successful!")
        else: 
            print("Sorry, sign in unsuccessful. Please double-check your credentials.")
    
    def manage_notifications(self, command):
        """ When we log in in the Instagram page, it asks you if you'd like to turn on or off the notifications. This method takes as argument either 'on' or 'off'. """
        # Creating a dictionary to map command to corresponding text 
        commands = {"on": "Turn On" , "off": "Not Now"}
        # Formalize input  
        command = command.lower()
        # If command is neither "on" or "off", return None
        if command not in commands:
            print("Wrong argument please input \"ON\" or \"OFF\" as argument")
            return None                
        # Click button corresponding to the command 
        try:
            self.driver.find_element_by_xpath("//button[text()=\"" + commands.get(command) + "\"]").click()
        except NoSuchElementException:
            print("Couldn't find " + commands.get(command) + " button.")

    def close(self):
        """ Method that close the current tab """
        self.driver.close()
        
    def quit(self):
        """ Method that closes the browser and shuts down the ChromeDriver """
        self.driver.quit()  

    def scroll_down(self):
        """ Method that scrolls once to the bottom of the current page. """ 
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # document.body.scrollHeight return the entire height of an element (in this case "body") in pixels, including padding, but excluding the border, scrollbar or margin. 
            time.sleep(self.PAUSE_TIME) # adding a pause time to allow page to load
        except: 
            print("Failed to scroll down")

    def scroll_till_end(self):
        """ Method that scrolls down to the bottom of the page in order to load everything on a page. This method keeps scrolling until the end of the page is reached. """
        # Create boolean variable "end" to indicate if the "end" is reached
        end = False        
        # Setting initial page height
        page_height = self.driver.execute_script("return document.body.scrollHeight;")  

        while not end:
            # Scroll down 
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Introduce a wait time to give the time to the browser to load
            time.sleep(self.PAUSE_TIME)
            # Get current page height
            current_height = self.driver.execute_script("return document.body.scrollHeight;")
            # If page has not moved, we have reached the end of the page
            if current_height == page_height:
                end = True
            # Setting page height to current page height for next iteration
            page_height = current_height        
        print("Reached the end of " + self.driver.current_url)

    def like(self):
        """Method that finds all the like buttons and clicks on each one of them, if they are not already clicked (liked)."""
        like_xpath = "//span[contains(@class,\"glyphsSpriteHeart\") and @aria-label = \"Like\"]//parent::button"
        liked_xpath = "//span[contains(@class,\"glyphsSpriteHeart\") and @aria-label=\"Unlike\"]"
        unliked = self.driver.find_elements_by_xpath(like_xpath)
        liked = self.driver.find_elements_by_xpath(liked_xpath)        
        # If there are like buttons
        if unliked:
            for button in unliked:
                try:
                    button.click()
                    time.sleep(self.PAUSE_TIME) # Adding a wait time to allow the page to load entirely
                except StaleElementReferenceException:  # We face this stale element reference exception when the element we are interacting is destroyed and then recreated again in the DOM. When this happens the reference of the element in the DOM becomes stale. Hence we are not able to get the reference to the element.
                    print("Failed to like picture: Element is no longer attached to the DOM") 
                except ElementClickInterceptedException:
                    print("Failed to click on the like button due to overlaying elements")
            return True
            # return True
        elif liked:
            print("Picture has already been liked")
            return False

    def like_feed(self, number_of_iterations):
        """ Method that likes pictures on an Instagram feed for a specified number of iterations. If the driver doesn't find any likable picture, it will scroll down the feed to show new pictures. """        
        for _ in range(number_of_iterations):
            if not self.like():
                self.scroll_down()
                time.sleep(self.PAUSE_TIME) # Adding a wait time to allow the page to load entirely

    def like_all_pictures(self):
        """ Method that likes every picture on an Instagram page."""  
        # Open the first picture
        self.open_first_picture()  
        # Create has_picture variable to keep track if user has another picture
        has_picture = True     
        while has_picture:
            self.like()
            # Updating value of has_picture
            has_picture = self.has_next_picture()
        try:
            # Closing the picture pop up after having liked the last picture
            self.driver.find_element_by_xpath("//button[@class=\"ckWGn\"]").click()                
            print("Liked all pictures of " + self.driver.current_url)
        except: 
            # If driver fails to find the close button, it will navigate back to the main page
            print("Couldn't close the picture, navigating back to Instagram's main page.")
            self.driver.get("https://www.instagram.com/")

    def has_next_picture(self):
        """ Helper method that finds if the current picture has a \"Next\" button to navigate to the next picture. If it does, it will navigate to the next picture."""
        next_button = "//a[text()=\"Next\"]"
        try:
            self.driver.find_element_by_xpath(next_button).click()
            return True
        except (NoSuchElementException, TimeoutException):
            print("User has no more pictures")
            return False
        except StaleElementReferenceException:
            print("Failed to navigate to next picture due to StaleElementReferenceException")
            return False

    def search(self, keyword, index):
        """ Method that searches for an username and navigates to the nth profile in the results where n corresponds to the index """        
        search_input = "//input[@placeholder=\"Search\"]"
        navigate_to = "(//div[@class=\"fuqBx\"]//descendant::a)[" + str(index) + "]"
        try:
            self.driver.find_element_by_xpath(search_input).send_keys(keyword)
            self.driver.find_element_by_xpath(navigate_to).click()
            print("Successfully searched for: " + keyword)
            time.sleep(self.PAUSE_TIME) # Adding a wait time to allow the page to load entirely
        except (NoSuchElementException, StaleElementReferenceException):
            print("Search failed")

    def follow(self):
        """ Method that clicks on a 'Follow' button and store information from the user you followed into a SQLite3 database """
        try:
            self.driver.find_element_by_xpath("//header//button[text()=\"Follow\"]").click()
            account = self.get_account()
            if account:
                if account.posts:
                    account.insert_ig_account()
                else:
                    account.insert_ig_id()
            else:
                print("Failed to store account in database")
        except NoSuchElementException:
            print("Follow button not found.")

    def unfollow(self):
        """ Method that clicks on a 'Unfollow' button and erases its information from the SQLite3 database """
        try:
            self.driver.find_element_by_xpath("//header//button[text()=\"Following\"]").click()
            self.driver.find_element_by_xpath("//button[text()=\"Unfollow\"]").click()
            print("Successfully unfollowed " + self.driver.current_url)
        except NoSuchElementException:
            print("Failed to Unfollow user, navigating back to Instagram's main page.")
            self.driver.get("https://www.instagram.com/")

    def get_account(self):
        """ Method that returns an InstagramAccount object from the current user's profile page """
        infos = [header.text for header in self.driver.find_elements_by_xpath("//header//descendant::h1")] + [number.text for number in self.driver.find_elements_by_xpath("//span[@class=\"g47SY \"]")]
        if len(infos) == 5:
            instagram_id, username, num_posts, num_followers, num_following= infos
            return InstagramAccount(instagram_id, name=username, posts=num_posts, followers=num_followers, following=num_following)           
        # In the case user has no name
        elif len(infos) == 4: 
            instagram_id, num_posts, num_followers, num_following  = infos
            return InstagramAccount(InstagramID=instagram_id, posts=num_posts, followers=num_followers, following=num_following)            
        else:
            try: 
                instagram_id = self.driver.find_element_by_xpath("//header//descendant::h2[@class=\"BrX75\"]/a").text
                return InstagramAccount(InstagramID=instagram_id)
            except NoSuchElementException:
                print("Failed to get account, Instagram ID not found.")
                return None

    def navigate_to_explore(self):
        """ Method that navigates to the Explore section of Instagram """
        try:
            self.driver.find_element_by_xpath("//a[@href=\"/explore/\"]").click()
            time.sleep(self.PAUSE_TIME) # Adding a wait time to allow the page to load entirely
        except NoSuchElementException:
            print("Failed to navigate to \"explore\"")

    def open_first_picture(self):
        """ Method that opens the first picture on an Instagram profile page """
        try:             
            self.driver.find_element_by_xpath("(//div[@class=\"eLAPa\"]//parent::a)[1]").click()
        except NoSuchElementException:
            print("Profile has no picture")
        except StaleElementReferenceException:
            print("Failed to open the first picture")
        except TimeoutException:
            print("Did not find the first picture")

    def get_Instagram_page(self):
        """ Method that navigates to Instagram's main page """
        self.driver.get("https://www.instagram.com/")

    def unfollow_all(self):
        """ This method gets all the randomly followed account from the instagramids table of InstagramDatabase and unfollow the accounts one by one """ 
        # Assemble every InstagramAccount in the InstagramDatabase
        accounts = InstagramAccount.get_instagram_accounts() + InstagramAccount.get_instagram_ids()
        # For each account, navigate to their url and unfollow that user.
        for account in accounts:
            self.driver.get(account.url)
            self.unfollow()
        # Clear InstagramDatabase after all accounts have been unfollowed
        InstagramAccount.clear_accounts()
        InstagramAccount.clear_ids()        
        # Navigate back to Instagram's main page after everything is done
        self.get_Instagram_page()
