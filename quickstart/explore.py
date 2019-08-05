""" This script navigates to the explore page on Instagram and opens the first picture. Then, it likes and follows all the pictures and Instagram accounts on the explore page to get their attention! """
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

# Navigate to the explore page
bot.navigate_to_explore()

# Open the first picture on the page
bot.open_first_picture()

# Like and Follow random pictures/Instagram accounts to get their attention and store their Instagram ID in InstagramDatabase.db to unfollow them later using unfollow_all.py
while bot.has_next_picture():
    bot.follow()
    bot.like()

# Closing browser when automation is done.
bot.driver.quit()
