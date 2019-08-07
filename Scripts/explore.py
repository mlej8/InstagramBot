""" This script navigates to the explore page on Instagram and opens the first picture. Then, it likes and follows all the pictures and Instagram accounts on the explore page to get their attention! """
import sys
import time

def main():
    # Importing modules to work with
    from InstagramBot import InstagramBot
    
    # Creating an Instagram bot object
    bot = InstagramBot()

    # Maximize window
    bot.maximize_window()

    # Sign in to Instagram
    bot.login("Your username here", "Your password here")

    # Dealing with notification pop up
    bot.manage_notifications("off")

    # Search for a specific Instagram account
    bot.search("Specify Instagram Profile Here", 1)

    # Follow the account
    bot.follow()

    # Navigate to the explore page
    bot.navigate_to_explore()

    # Open the first picture on the page
    bot.open_first_picture()

    # Like and Follow random pictures/Instagram accounts to get their attention and store their Instagram ID in InstagramDatabase.db to unfollow them later using unfollow_all.py
    while bot.has_next_picture():
        bot.like()
        bot.follow()    

    # Closing browser when automation is done.
    bot.driver.quit()

if __name__ == "__main__":
    # change system path to get modules in the previous folder
    sys.path.append("..")
    # running script
    main()