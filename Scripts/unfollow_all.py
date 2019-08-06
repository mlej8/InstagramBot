""" This script should be ran after explore.py. It "unfollows" every Instagram accounts stored in the InstagramDatabase. """
import sys
import time

def main():
    # Importing modules to work with
    from InstagramBot import InstagramBot
    from account import InstagramAccount

    # Creating an Instagram bot object
    bot = InstagramBot()

    # Maximize window
    bot.maximize_window()

    # Sign in to Instagram
    bot.login("Your username here", "Your password here")

    # Dealing with notification pop up
    bot.manage_notifications("off")

    # Unfollow all the Instagram accounts stored in the InstagramDatabase
    bot.unfollow_all()

    # Closing browser when automation is done.
    bot.driver.quit()

if __name__ == "__main__":
    # change system path to get modules in the previous folder
    sys.path.append("..")
    # running script
    main()