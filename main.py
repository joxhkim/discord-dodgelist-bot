import discord
import asyncio
import json
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

load_dotenv()
bot = commands.Bot(command_prefix='!')
dodge_list = {}


@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\n')
    print(f'Version: {discord.__version__}')
    print(f'Successfully logged in and booted')


@bot.command()
async def add(ctx, player_tag):
    if player_tag in dodge_list:
        await ctx.reply("Player already exists on the dodge list.")
    else:
        entry = datetime.now()
        dodge_list[player_tag] = entry.strftime("%B %d %Y %I:%M%p CST")
        await ctx.reply("Player " + '"' + player_tag + '"' + " has been added to the dodge list.")
        print(dodge_list)


@bot.command()
async def remove(ctx, player_tag):
    if player_tag in dodge_list:
        del dodge_list[player_tag]
        await ctx.reply("Player " + '"' + player_tag + '"' + " has been removed from the dodge list.")
        print(dodge_list)
    else:
        await ctx.reply("Player " + '"' + player_tag + '"' + " does not exist on the dodge list.")
        print(dodge_list)


@bot.command()
async def list(ctx):
    if not dodge_list:
        await ctx.reply("List is empty.")
    else:
        await ctx.reply(dodge_list)


@bot.command()
async def lookup(ctx, player_tag):
    if player_tag in dodge_list:
        # TODO: Return the date/time the player was added to the dodge list and who added it
        index = dodge_list.index(player_tag)
        await ctx.reply(player_tag + " was added to the dodge list at " + entry_time)
    else:
        await ctx.reply("Player " + '"' + player_tag + '"' + " does not exist on the dodge list.")


bot.run(getenv('TOKEN'))
