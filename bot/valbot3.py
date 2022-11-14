import discord
import os
import colors
from dotenv import load_dotenv
from valo_api import endpoints

load_dotenv(dotenv_path='../.env')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def getName(string):
    msg = string
    first = (msg.split())[1]
    second = first.split('#')
    return second


@client.event
async def on_message(message):
    if message.content == 'Valbot !':
        await message.channel.send(
            'Get mmr details (rank, rr): !mmr Player#TAG \
            \nGet account details (account level, region): !acc Player#TAG \
            \nGet player match history (stats from last five games): !hist Player#TAG \
            \nGet information of skin (price, containing collection): !skin SkinName WeaponType'
        )


    if message.content.startswith('!mmr'):
        name = getName(message.content)
        try:
            info = endpoints.get_mmr_details_by_name_v1(region='na', name=name[0], tag=name[1])
       
            await message.channel.send('\033[1mUser:\033[0m '+info.name+'\n\033[1mRank:\033[0m '+info.currenttierpatched+'\n\033[1mRR:\033[0m '+str(info.ranking_in_tier))
        except:
            await message.channel.send('Are you dumb? That user does not exist.')

    # TODO: write account, history, skin info
    if message.content.startswith('!acc'):
        pass
    if message.content.startswith('!hist'):
        # returns metadata (test to see containing), players, team, rounds, kills
        # print all to see formatting
        # access MatchPlayerV3.stats
        pass
    if message.content.startswith('!skin'):
        # API returns list of offered skins
        # search for requested, output as needed
        pass

client.run(os.getenv('TOKEN'))
