import discord
import re
import os

# Initialize bot with message content intent
intents = discord.Intents.default()
intents.message_content = True 

client = discord.Client(intents=intents)

# Regex to find TikTok links
TIKTOK_REGEX = r"(https?://(?:www\.|vm\.|vt\.)?tiktok\.com/[^\s?]+)"
INSTAGRAM_REGEX = r"(https?://(?:www\.)?instagram\.com/[^\s?]+)"

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Don't let the bot respond to itself
    if message.author == client.user:
        return

    # Check if message contains a TikTok link
    match = re.search(TIKTOK_REGEX, message.content)
    
    if match:
        original_url = match.group(1)
        
        # Replace the domain with vxtiktok.com for a better embed
        fixed_url = original_url.replace("tiktok.com", "tnktok.com")
        
        # Delete the original message and send the fixed link
        try:
            await message.edit(suppress=True)
            await message.channel.send(f"{message.author.mention}: Fixed that for you! 🎬\n{fixed_url}")
        except discord.Forbidden:
            print("Missing 'Manage Messages' permission to delete message.")

    # Check if message contains an Instagram link
    match = re.search(INSTAGRAM_REGEX, message.content)
    
    if match:
        original_url = match.group(1)
        
        # Replace the domain with kkclip.com for a better embed
        fixed_url = original_url.replace("instagram.com", "kkclip.com")
        
        # Delete the original message and send the fixed link
        try:
            await message.edit(suppress=True)
            await message.channel.send(f"{message.author.mention}: Fixed that for you! 🎬\n{fixed_url}")
        except discord.Forbidden:
            print("Missing 'Manage Messages' permission to delete message.")

token = os.getenv('DISCORD_TOKEN')
if not token:
    print("Error: DISCORD_TOKEN environment variable not set.")
    exit(1)

if __name__ == "__main__":
    client.run(token)
