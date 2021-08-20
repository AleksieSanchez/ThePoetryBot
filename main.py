import discord
import os
from keep_alive import keep_alive
from discord.ext import commands, tasks
from random import randrange

client = discord.Client()
bot = commands.Bot(command_prefix='?')

#statistics for keeping cat alive
energy = 100
hapiness = 100
Money = 100
love = 100

ableToWork = True

firsTime = True


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global Money
    global energy
    global hapiness
    global love

    global ableToWork

    if message.author == client.user:
        return

    if message.author.id == (423679371044323329):
      if message.content.startswith("?resCat"):
        await message.channel.send("Cat has been revived.")
        energy = 100
        hapiness = 100
        love = 100



    if(energy <= 0):
      await message.channel.send("Sadly the server cat has died. It became a fat blob with no energy.")
      client.close()

    if (hapiness <= 0):
      await message.channel.send("Sadly the server cat has died. You stopped playing with it, and ran away.")
      client.close()

    if (love <= 0):
      await message.channel.send("Sadly the server cat has died. You left it alone and never gave it any attention")
      client.close()

    if (message.content.startswith("?payAttention")):
      await message.channel.send("You look at the cat")
      randicus = randrange(1, 5)

    if message.content.startswith("?helpCat"):
      await message.channel.send("**Cat Commands**\n\nUse **?ping** to see if the bot is active\nUse **?stats** to see the cat's stats\nUsing **?work** will give you 100 coins but you will lose 10 points of every stats **only works once per hour**\nUse **?pet** to pet the cat with a 50/50 chance of it working\nUse **?feed** to feed the cat while paying 25 coins to feed it\nUsing **?gamble** while begin a dice roll game where highest number wins.\nThere is also a 1/10 chance that you will develop a gambling addiction and your cat will lose 25 of every stat.")


    if message.content.startswith('?ping'):
        await message.channel.send("pong")

    if message.content.startswith('?stats'):
        await message.channel.send("**Cat's Statistics**\n\nEnergy - **" +
                                   str(energy) + "**\nHapiness - **" +
                                   str(hapiness) + "**\nLove - **" +
                                   str(love) + "**\n\nYou have **" +
                                   str(Money) + "** money")
        if ableToWork:
          await message.channel.send("**Plus you are able to work!**")

    if message.content.startswith('?work') and ableToWork:
        await message.channel.send(
            "You work a 9 to 5 job.\nYour cat loses 10 of every stat...\nBut you got 100 dollars!"
        )
        Money += 100
        energy -= 10
        hapiness -= 10
        love -= 10
        ableToWork = False
        name_of_function.start()

    if message.content.startswith("?work") and not ableToWork:
      await message.channel.send("You can't work anymore!")


    if message.content.startswith("?pet"):
      await message.channel.send("You attempt to pet the cat.")
      randus = randrange(0, 2)
      if(randus == 0):
        await message.channel.send("The cat is nowhere to be found. Almost like it teleported\nNothing changes")
      else:
        await message.channel.send("The cat allows you to pet it.\nWhile petting it you feel a sense of pride for owning such a marvelous creature.\nLove increases by 10")
        love += 10
    
    if message.content.startswith("?feed"):

        if(Money <= 25):
          await message.channel.send("You don't have enough money to buy cat food!")
          return

        await message.channel.send("You pay 25 dollars for cat food\nThe cat's energy stat increases by 5")
        energy += 5
        Money -= 25

    if message.content.startswith('?gamble'):

        if(Money <= 25):
          await message.channel.send("You don't have enough money to gamble!")
          return



        await message.channel.send('You bet 25 dollars and roll the die')
        rand = randrange(1, 7)
        randEnemy = randrange(1, 7)
        await message.channel.send("You rolled a " + str(rand))
        await message.channel.send("Opponent rolls a " + str(randEnemy))

        if (rand > randEnemy):
            await message.channel.send("You win! Here is 25 coins!")
            Money += 25
        elif (randEnemy > rand):
            await message.channel.send("You lose! Goodbye 25 coins...")
            Money -= 25
        else:
            await message.channel.send("You Tie! Nothing is lost!")

      
        randus = randrange(1, 11)
        if(randus == 10):
          await message.channel.send("You spent so much time addicted to gambling. That your cat lost 25 of every stat!")
          energy -= 25
          hapiness -= 25
          love -= 25



@tasks.loop(hours=1)
async def name_of_function():
    await client.wait_until_ready()
    print('1 hour has passed')
    global firsTime
    if(firsTime):
      firsTime = False
      return
    global ableToWork
    ableToWork = True

@tasks.loop(minutes = 30)
async def lower_stats():

  global energy
  global love
  global hapiness

  await client.wait_until_ready()
  print('Lowering one stat')
  rano = randrange(1, 4)

  if(rano == 1):
    energy -= 10
  elif(rano == 2):
    love -= 10
  else:
    hapiness -= 10
    


keep_alive()
lower_stats.start()
client.run(os.getenv('TOKEN'))
