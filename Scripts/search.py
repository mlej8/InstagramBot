""" This example demonstrates how InstaBot can be used to search and follow a specific Instagram user. """
import time
import sys

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

    # Go back to Instagram page
    bot.get_Instagram_page()

    # Closing browser when automation is done.
    bot.driver.quit()

if __name__ == "__main__":
    # change system path to get modules in the previous folder
    sys.path.append("..")
    # running script
    main()