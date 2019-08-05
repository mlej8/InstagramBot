""" This example demonstrate how InstaBot can be used to automatically like pictures on an Instagram feed"""
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

# Set a loop to like pictures on the Instagram feed
bot.like_feed(10)

# Closing browser when automation is done.
bot.driver.quit()
