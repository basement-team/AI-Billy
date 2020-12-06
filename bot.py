import discord
import os
import random
import pkg_resources
from discord.ext import commands
import asyncio
import aiml
import json

# configuration
with open('config.json') as f:
  data = json.load(f)

STARTUP_FILE = data["startup_file"]
channel_name = data["channel"]
prefix       = data["prefix"]
owner_id     = data["owner_id"]
token        = data["token"]

# setup
aiml_kernel = aiml.Kernel()

# if there is already a compiled brain, loads it.
if os.path.isfile("bot_brain.brn"):
	aiml_kernel.bootstrap(brainFile="bot_brain.brn")

# else loads all the aiml files.
else:
	aiml_kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")

	# saves the brain
	# so that every time you don't have to compile from the  aiml files
	aiml_kernel.saveBrain("bot_brain.brn")

# initializing discord client
try:
	# there is a token variable defined
	bot = commands.Bot(command_prefix=prefix)
except:
	# there is no token variable defined, or invalid
	# so the bot starts with default prefix
	bot = commands.Bot(command_prefix='!')
	prefix = '!'


# on ready event
@bot.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(bot.user.name))
	print("ID: {}".format(bot.user.id))
	print("---------------------")


# on message event
@bot.event
async def on_message(message):
	# if it is a command, then bot shouldn't pass the message to aiml.
	if message.content.startswith(prefix):
		await bot.process_commands(message)

	# some checks before handing the message to aiml
	if await _checks(message):
		return
	
	# after all these checks, proceed to the reply message generation
	else:
		# processing response
		aiml_response = aiml_kernel.respond(message.content)

		# we can't send an empty message, is the message empty?
		if aiml_response == '':
			await message.channel.send("uhm?")
		# this is the final step, sending the correct response to the channel.
		else:
			print(aiml_response)
			await message.channel.send(aiml_response)


# talking to AI through a command method.
@bot.command(name='respond', aliases=['ai'])
async def _respond(ctx, *, message=None):
	# checking whether the message is empty, this may not make sense
	# but when some attachments are sent, it will trigger on_message.
	if message is None:
		print("Empty message received.")
		await ctx.send("uhm what was that")
		return

	# processing response
	aiml_response = aiml_kernel.respond(message)

	# we can't send an empty message, is the message empty?
	if aiml_response == '':
		await ctx.send("uhm?")
	# sending the correct response.
	else:
		print(aiml_response)
		await ctx.send(aiml_response)


# checks for the channel based chatting.
async def _checks(message):
	# bot shouldn't respond to it's own messages,
	# or messages being received in ANY channel
	if message.author.bot or str(message.channel) != channel_name:
		return True

	# checking whether the message is empty, this may not make sense
	# but when some attachments are sent, it will trigger on_message.
	if message.content is None:
		print("Empty message received.")
		return True

	# logging messages in the chatting channel
	print("Message: " + str(message.content))

	# owner wants to shut down the bot
	if 'shutdown' in message.content and message.author.id == owner_id:
		await bot.logout()
		return True
	else:
		return False

# taking the show to the stage :P
bot.run(token)