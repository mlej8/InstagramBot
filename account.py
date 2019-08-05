import sqlite3
import datetime

class InstagramAccount():
# Class that stores information about people that we follow in database in order to unfollow them later 
    
    def __init__(self, InstagramID, name="Unspecified", posts=None, followers=None, following=None):
        self.name = name 
        self.InstagramID = InstagramID
        self.posts = posts
        self.followers = followers
        self.following = following

    def __repr__(self):
        return "Name: {}\nInstagramID: {}\nPosts: {}\nFollowers: {}\nFollowing: {}".format(self.name,self.InstagramID,self.posts,self.followers,self.following)

    @property 
    def url(self):
        """ Returns an Instagram Account's URL """
        return "https://www.instagram.com/{}/".format(self.InstagramID)
 
    def insert_ig_account(self):        
        """ Method that inserts an Instagram Account's information into the instagramaccounts table of the InstagramDatabase.db """
        # Establish connection with DB
        conn = sqlite3.connect("InstagramDatabase.db")
        # Create a cursor to interact with DB
        cursor = conn.cursor()
        # SQL Query
        table = "CREATE TABLE IF NOT EXISTS instagramaccounts(id TEXT, name TEXT, posts TEXT, followers TEXT, following TEXT);"
        query = "INSERT INTO instagramaccounts VALUES (:id,:name,:posts,:followers,:following)"
        # Execute queries
        cursor.execute(table)
        cursor.execute(query, {"id": self.InstagramID, "name": self.name, "posts": self.posts, "followers": self.followers, "following": self.following})
        # Commit into database 
        conn.commit()
        # Close cursor 
        cursor.close()
        # Close connection
        conn.close()
    
    def remove_ig_account(self):
        """ Method that removes an Instagram account from the instagramaccounts table of the InstagramDatabase.db """ 
        # Connect to database
        conn = sqlite3.connect("InstagramDatabase.db")
        # Create cursor 
        cursor = conn.cursor()
        # Create queries        
        query = "DELETE FROM instagramaccounts WHERE id = :id;"
        # Execute queries 
        cursor.execute(query, {"id": self.InstagramID})
        # Commit changes
        conn.commit()
        # Close cursor
        cursor.close()
        # Close connection
        conn.close()     

    def insert_ig_id(self):
        """ Method that inserts an Instagram Account's ID and the current time into the instagramids table of the InstagramDatabase.db """ 
        # Connect to database
        conn = sqlite3.connect("InstagramDatabase.db")
        # Create cursor 
        cursor = conn.cursor()
        # Create queries        
        table = "CREATE TABLE IF NOT EXISTS instagramids(id TEXT, date TEXT);"
        query = "INSERT INTO instagramids (id, date) VALUES (:id, :date);"
        # Execute queries 
        cursor.execute(table)
        cursor.execute(query, {"id": self.InstagramID, "date": datetime.datetime.now()})
        # Commit changes
        conn.commit()
        # Close cursor
        cursor.close()
        # Close connection
        conn.close()
        
    def remove_ig_id(self):
        """ Method that removes an Instagram Account's ID and the current time from the instagramids table of the InstagramDatabase.db """ 
        # Connect to database
        conn = sqlite3.connect("InstagramDatabase.db")
        # Create cursor 
        cursor = conn.cursor()
        # Create queries        
        query = "DELETE FROM instagramids WHERE id = :id;"
        # Execute queries 
        cursor.execute(query, {"id": self.InstagramID})
        # Commit changes
        conn.commit()
        # Close cursor
        cursor.close()
        # Close connection
        conn.close()     

    @staticmethod    
    def get_instagram_accounts():
        """ Method that returns all the accounts stored in instagramaccounts table of the InstagramDatabase.db and returns a list of InstagramAccounts """
        # Connect to database 
        conn = sqlite3.connect("InstagramDatabase.db")
        # Create cursor
        cursor = conn.cursor()
        # SQL Query
        query = "SELECT * from instagramaccounts"
        # Execute query
        cursor.execute(query)
        # Fetch all results
        table = cursor.fetchall()
        # Close cursor 
        cursor.close()
        # Close connection 
        conn.close()
        # Return a list of InstagramAccounts
        return [InstagramAccount(InstagramID=element[0], name=element[1], posts=element[2], followers=element[3], following=element[4]) for element in table]

    @staticmethod    
    def get_instagram_ids():
        """ Method that returns all the Instagram IDs stored in instagramids table of the InstagramDatabase.db and returns a list of InstagramAccounts"""
        # Connect to database 
        conn = sqlite3.connect("InstagramDatabase.db")
        # Create cursor
        cursor = conn.cursor()
        # SQL Query
        query = "SELECT * from instagramids"
        # Execute query
        cursor.execute(query)
        # Fetch all results
        table = cursor.fetchall()
        # Close cursor 
        cursor.close()
        # Close connection 
        conn.close()
        # Return a list of InstagramAccounts
        return [InstagramAccount(InstagramID=element[0]) for element in table]

    @staticmethod
    def clear_accounts():
        """ Method that clears the instagramaccounts table from the InstagramDatabase.db """ 
        # Connect to database
        conn = sqlite3.connect("InstagramDatabase.db")
        # Create cursor 
        cursor = conn.cursor()
        # Create queries        
        query = "DELETE FROM instagramaccounts;"
        # Execute queries 
        cursor.execute(query)
        # Commit changes
        conn.commit()
        # Close cursor
        cursor.close()
        # Close connection
        conn.close()     
        
    @staticmethod
    def clear_ids():
        """ Method that clears the instagramids table from the InstagramDatabase.db """ 
        # Connect to database
        conn = sqlite3.connect("InstagramDatabase.db")
        # Create cursor 
        cursor = conn.cursor()
        # Create queries        
        query = "DELETE FROM instagramids;"
        # Execute queries 
        cursor.execute(query)
        # Commit changes
        conn.commit()
        # Close cursor
        cursor.close()
        # Close connection
        conn.close()     
