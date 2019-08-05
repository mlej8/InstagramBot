""" This script demonstrate how InstaBot can be used to automatically like all the pictures on an Instagram profile page. It can be applied to an user's profile page or to the Instagram \"Explore\" page. """ 
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

# Navigate to an user's profile page using Search 
bot.search("Specify Instagram Profile Here", 1)

# Use like_all_pictures() method to like all the pictures on current page
bot.like_all_pictures()

# Closing browser when automation is done.
bot.driver.quit()
