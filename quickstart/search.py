""" This example demonstrates how InstaBot can be used to search and follow a specific Instagram user. """
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

# Search for a specific Instagram account
bot.search("Specify Instagram Profile Here", 2)

# Follow the account
bot.follow()

# Go back to Instagram page
bot.get_Instagram_page()

# Closing browser when automation is done.
bot.driver.quit()
