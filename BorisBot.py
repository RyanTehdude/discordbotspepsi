import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print ("Logged in as:")
    print (client.user.name)
    print ("ID:")
    print (client.user.id)
    print ("Ready to use")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("/ping"):
        await client.send_message(message.channel, "GROUNDED!")
    elif message.content.startswith("/help"):
        await client.send_message(message.channel, "Here are the commands that will get you GROUNDED! /ping, /help, /meme, /FactAboutCaillou, /storytime")
    elif message.content.startswith("/secret"):
        await client.send_message(message.channel, "Some please help me from my misery")
    elif message.content.startswith("/ground"):
        await client.send_message(message.channel, "Oh Oh Oh Oh Oh! You are so grounded! Go to your room for 30 years and die! :joy:")
    elif message.content.startswith("/meme"):
        await client.send_message(message.channel, "I am ultimately obsessed with caillou and i ground him for every single thing that counts as a move he makes!")
    elif message.content.startswith("/FactAboutCaillou"):
        await client.send_message(message.channel, random.choice(["It is certain :8ball:",
                                                                  "It is decidedly so :8ball:",
                                                                  "Without a doubt :8ball:",
                                                                  "Yes, definitely :8ball:",
                                                                  "You may rely on it :8ball:",
                                                                  "As I see it, yes :8ball:",
                                                                  "Most likely :8ball:",
                                                                  "Outlook good :8ball:",
                                                                  "Yes :8ball:",
                                                                  "Signs point to yes :8ball:",
                                                                  "Reply hazy try again :8ball:",
                                                                  "Ask again later :8ball:",
                                                                  "Better not tell you now :8ball:",
                                                                  "Cannot predict now :8ball:",
                                                                  "Concentrate and ask again :8ball:",
                                                                  "Don't count on it :8ball:",
                                                                  "My reply is no :8ball:",
                                                                  "My sources say no :8ball:",
                                                                  "Outlook not so good :8ball:",
                                                                  "Very doubtful :8ball:"]))
    elif message.content.startswith("/storytime"):
        await client.send_message(message.channel, random.choice(["Once Caillou went to Japan and ate at Taco bell and he went to take a dump and he farted that he created a nuclear chain reaction and killed everyone :joy:",
                                                                  "Caillou made one move and i grounded him for it :joy:",
                                                                  "Caillou went to sleep and i yelled at him with a megaphone and grounded him for it but im not sure if he deserved to be grounded  :thinking:",
                                                                  "Yes, Caillou is definitely 4 years old but somehow has a IQ over 100 and im scared to reveal my IQ to him  :thinking:",
                                                                  "You can rely on the fact that Caillou is totally 4 years old :joy:",
                                                                  "As I see it, i approximetely grounded Caillou 2.3647 sextillion times under 30 years :joy:",
                                                                  "Most likely that i grounded Caillou under a second now:joy:",
                                                                  "One time i ungrounded Caillou suprisingly because he hanged MacusoperAndLPSLover to a cross with diesel busters and Caillou drew a swastika on MacusoperAndLPSLover's Forehead and then Caillou and Diesel Busters started dancing as MacusoperAndLPSLover was burning to death :joy:",
                                                                  "Does it look like that if i didn't ground Caillou everyday would give my life a purpose? :joy:",
                                                                  "Caillou is invicible and he can't get killed and only thing that can stop him is by grounding him for atleast everysecond :joy:",
                                                                  "Caillou has killed more then 30 people this month and i only ground him for that :joy:",
                                                                  "Very doubtful that i even like Caillou at all :joy:"]))
client.run("MzcxNzI4OTkyNjIzMTMyNjc0.DM6iOQ.lVJmecDgTN4A3TUtumEY0VLHEFw")
