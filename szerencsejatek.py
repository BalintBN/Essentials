#(c) copyright 2020 - 2023 BalintEssentials
#By: M.Balint
import os
import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix = '~')
token = 'NzMxMTAxMzU2MzgzMDEwODE3.XwnFDg.AZTHITTEDMI?!'

os.chdir("/home/pi/bot")

@bot.command(aliases=["bal"])
async def balance(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    money_am = users[str(user.id)]["money"]
    bank_amt = users[str(user.id)]["bank"]
    
    em = discord.Embed(title = f"{ctx.author.name} pénztárcája:")
    em.add_field(name = "Pénz:",value = f"{money_am}$") 
    await ctx.send(embed=em)

async def open_account(user):
#    with open("bank.json","r") as f:
#        users = json.load(f)
    
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["money"] = 0
        users[str(user.id)]["bank"] = 0  

        with open("bank.json","w") as f:
            json.dump(users,f)
            return True

async def get_bank_data():
    with open("bank.json","r") as f:
        users = json.load(f)

    return users  


@bot.command()
async def add_money(ctx ,member:discord.Member, amount):
    await open_account(ctx.author)
    await open_account(member)
    user = ctx.author
    users = await get_bank_data()

    
    users[str(member.id)]["money"] += int(amount)

    with open("bank.json","w") as f:
        json.dump(users,f)

    await ctx.send(amount +"$ hozzáadva " + member.mention + " pénztárcájához.")  


bot.login(token)        
