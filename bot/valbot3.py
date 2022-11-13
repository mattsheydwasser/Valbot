import discord
from valo_api import endpoints

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def getName(string):
    msg = string
    first = (msg.split())[1]
    second = first.split('#')
    return second


@client.event
async def on_message(message):
    if message.content.startswith('pi'):
        name = getName(message.content)
        try:
            info = endpoints.get_mmr_details_by_name_v1(region='na', name=name[0], tag=name[1])
       
            await message.channel.send('User: '+info.name+'\nRank: '+info.currenttierpatched+'\nRR: '+str(info.ranking_in_tier))
        except:
            await message.channel.send('Are you dumb? That user does not exist.')


client.run('MTA0MTIwOTk3MDY1OTY5MjYzNA.GclzrA.wMRLaCc8iPLNTf32HxMPRvnNZhLu_L84dlM_Pk')
