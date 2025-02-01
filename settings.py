import os
from dotenv import load_dotenv
import discord


#Loads the .env file that contains DISCORD_API_SECRET and GUILDS_ID
try:
    load_dotenv()
except:
    print("dotenv environment was not found. pip install python-dotenv ")


try:
    #  DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
    DISCORD_API_SECRET = os.getenv("TEST_TOKEN")
except:
    print("DISCORD_API_SECRET was not found. Create .env file and declare your DISCORD_API_SECRET")
    print("remember to add .env to gitignore to keep your keys off github")
    
try:
    GUILDS_ID = discord.Object(id=int(os.getenv("GUILD")))
except:
    print("GUILDS_ID was not found. Create .env file and declare your GUILDS_ID")
    print("remember to add .env to gitignore to keep your guild id off github")
    
try:
    CHANNEL_ID = int(os.getenv("CHANNEL"))
except:
    print("CHANNEL_ID was not found. Create .env file and eclare your CHANNEL_ID")