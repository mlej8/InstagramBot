""" This script should be ran after explore.py. It "unfollows" every Instagram accounts stored in the InstagramDatabase. """
from Automation.InstagramBot.InstaBot import InstagramBot
from Automation.InstagramBot.account import InstagramAccount
import time

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
