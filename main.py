import discord
client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await message.channel.send('World!')
client.run(TOKEN)