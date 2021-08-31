import os
import random
from dotenv import load_dotenv
from os.path import join, dirname
from twitchio import user
from twitchio.ext import commands

# credentials:

BOT_PREFIX = "!" #This is the character that goes before every command
CHANNEL = "Channel name" #Name of the channel you want to run the bot
ACCESS_TOKEN = "YOUR TOKEN HERE" #Access Token from twitch. you can get it here: https://twitchtokengenerator.com/


class Bot(commands.Bot):
    def __init__(self):
        
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=ACCESS_TOKEN, prefix=BOT_PREFIX, initial_channels=[CHANNEL])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'{self.nick} is ready!\n \n')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot
        # For now we just want to ignore them
        if message.echo:
            return

        # Print the contents the message to console
        print(f"{message.author.name} : {message.content}")

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands
        await self.handle_commands(message)
    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        #When a user send !hello in chat runs:
        await ctx.send(f'{ctx.author.name} Hello!')

    @commands.command()
    async def yesno(self, ctx: commands.Context):
        #When a user send !yesno in chat runs:
        lucky = int(random.randint(0, 100))
        if lucky > 49:
            await ctx.send(f'YES!')
        else:
            await ctx.send(f'NO!')
        

bot = Bot()
bot.run()
