""" This script demonstrate how InstaBot can be used to automatically like all the pictures on an Instagram profile page. It can be applied to an user's profile page or to the Instagram \"Explore\" page. """ 
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

    # Navigate to an user's profile page using Search 
    bot.search("Specify Instagram Profile Here", 1)

    # Use like_all_pictures() method to like all the pictures on current page
    bot.like_all_pictures()

    # Closing browser when automation is done.
    bot.driver.quit()

if __name__ == "__main__":
    # change system path to get modules in the previous folder
    sys.path.append("..")
    # running script
    main()