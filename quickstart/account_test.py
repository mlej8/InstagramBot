""" The purpose of this example is to demonstrate the account module's functionalities """
from Automation.InstagramBot.account import InstagramAccount

# Creating InstagramAccounts 
acc1 = InstagramAccount("tester")
acc3 = InstagramAccount("halogen")
acc2 = InstagramAccount("instachinobot", "Michael Li", "360","453","456")
acc4 = InstagramAccount("Talal", "Yuyun", "215", "4566", "2316")

# Insert into respective tables in the InstagramDatabse
acc1.insert_ig_id()
acc3.insert_ig_id()
acc2.insert_ig_account()
acc4.insert_ig_account()

# Remove account from InstagramDatabase
# acc1.remove_ig_id()
# acc3.remove_ig_id()
# acc2.remove_ig_account()
# acc4.remove_ig_account()

# Print tables from InstagramDatabase
print("InstagramAccounts table:")
print(InstagramAccount.get_instagram_accounts())
print("InstagramIDs table:")
print(InstagramAccount.get_instagram_ids())

# Clear tables from InstagramDatabase
InstagramAccount.clear_accounts()
InstagramAccount.clear_ids()


