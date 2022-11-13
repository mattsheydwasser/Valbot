import discord

class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)

   #     self.bg_task = self.loop.create_task(self.my_background_task())

  #  async def my_background_task(self):
  #      channel = self.get_channel(210562329375539200)
  #      counter = 0
   #     while not self.is_closed():
  #          counter += 1
 #           await channel.send(counter)

  
    async def on_message(self, message):
        msg = message.content
        channel = self.get_channel(210562329375539200)

        if message.content == 'hi':
            print(True)
            await message.channel.send('hi')
        else:
            print(msg)
            print(False)

client = Client()
client.run('MTA0MTIwOTk3MDY1OTY5MjYzNA.GclzrA.wMRLaCc8iPLNTf32HxMPRvnNZhLu_L84dlM_Pk')
