import discord
import yaml
from TOKEN_file import TOKEN

client = discord.Client()

links = {}
active = True

def isActive():
    return active

def setActive(act):
    global active
    active = act

def registerWords():
    links.clear()
    with open("words.yml", 'r') as stream:
        try:
            dic = yaml.load(stream)
            print(dic)
            links.update(dic)
        except yaml.YAMLError as exc:
            print(exc)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!salut'):
        msg = 'SALUT ALDE GRAND FAN'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!debug'):
        await message.channel.send(links)
    
    if message.content.startswith("!listen"):
        if isActive():
            setActive(False)
            await message.channel.send("Le bot ne réagira plus aux messages")
        else:
            setActive(True)
            await message.channel.send("Le bot va maintenant réagir aux messages")
            await message.channel.send("https://tenor.com/view/alderiate-grand-moment-streaming-gif-15661070")

    if message.content.startswith("!updateGif"):
        registerWords()
        await message.channel.send("La liste des gifs a été rechargée")

    if isActive():
        for key in links.keys():
            if key in message.content:
                await message.channel.send(links.get(key))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    registerWords()

client.run(TOKEN)