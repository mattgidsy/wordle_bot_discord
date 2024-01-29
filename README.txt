This bot is made to help assist in solving wordle word puzzles.
The user will input their guesses and the bot will give them possible answers for them to choose for their next guess.

This bot is a variant of my original wordle bot that uses discord UI slash commands


REQUIREMENTS:
python 3.11.4
install a clean virtual environment # I used dotenv as noted below
pip install dotenv
pip install discord


# your .env file should look like this: 
DISCORD_API_TOKEN = 'YourSeCret12345kEy' #this is your bot's private api key
GUILD = '123456609857' #this is your guild ID


.gitignore:
__pycache__/
.env