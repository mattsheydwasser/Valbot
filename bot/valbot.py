#from valo_api import endpoints
import discord

def main():
    
    
    TOKEN = 'MTA0MTIwOTk3MDY1OTY5MjYzNA.GclzrA.wMRLaCc8iPLNTf32HxMPRvnNZhLu_L84dlM_Pk'
    client = discord.Client()

    @client.event
    async def on_ready():
    
        print('We have successfully loggged in as {0.user}'.format(client))


    @client.event
    async def on_message(message):

        if message.author == client.user:

            return



        if message.content.lower() == 'hello':

            await message.channel.send(f'Hello, {message.author.display_name}!')

            return



        if message.content.lower() == 'bye':

            await message.channel.send(f'See you later, {message.author.display_name}!')

            return



    client.run(TOKEN)
 #   info = endpoints.get_account_details_by_name(version='v1', name='Silas', tag='69LOL')
  #  store = endpoints.get_store_offers_v1()

    
if __name__ == '__main__':
    main()
    
