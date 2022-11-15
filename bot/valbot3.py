import discord
import os
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
    if message.content == 'Valbot !cmds':
        await message.channel.send(
            'Get mmr details (rank, rr): !mmr Player#TAG \
            \nGet account details (account level, region): !acc Player#TAG \
            \nGet player match history (stats from last five games): !hist Player#TAG \
            \nGet information of skin (price, containing collection): !skin SkinName WeaponType'
        )


    # TODO: write account, history, skin info
    # put functionality into seperate function, check if then go to that specific function
    if message.content.startswith('!acc'):
        #try: 
        nameTag = getName(message.content)
        await accountDetails(nameTag[0], nameTag[1], message)
        #except:
        #    await message.channel.send('Are you dumb? That user does not exist.')
        
    if message.content.startswith('!hist'):
        # returns metadata (test to see containing), players, team, rounds, kills
        # print all to see formatting
        # access MatchPlayerV3.stats
        pass
    if message.content.startswith('!skin'):
        # API returns list of offered skins
        # search for requested, output as needed
        pass

async def accountDetails(name, tag, message):
    """ 
    Gets account information of given user
    Input: Name of user, tag of user
    Output: Information (level, picture, region)
    """

    details = endpoints.get_account_details_by_name_v1(name, tag)
    mmr = endpoints.get_mmr_details_by_name_v1(region='na', name=name, tag=tag)
        # prints information to chat
        # CARD DISPLAY MAY CAUSE ERRORS
    #await message.channel.send(
     #   '\033[1mUser:\033[0m ' + details.name + { files:[ details.card.small ] } + 
      #  '\n\033[1mLevel:\033[0m '+details.account_level + 
       # '\033[1m Region:\033[0m '+ details.region)
        
    embed = discord.Embed(title = name+'#'+tag)

    embed.add_field(name='Rank: ', value=mmr.currenttierpatched)
    embed.add_field(name='RR: ', value=str(mmr.ranking_in_tier), inline=True)
    embed.add_field(name='Account Level: ', value=str(details.account_level), inline=True)

    imageurl = details.card.wide
    embed.set_image(url = imageurl)
    await message.channel.send(embed=embed)
        
client.run(os.getenv('TOKEN'))
