import discord
from finder import search

import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
import openpyxl as xl
from discord.ext.commands import has_permissions,  CheckFailure, check
import random as rd

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix = ['>.','?'],intents=intents) #put your own prefix here



emoji = {
    'RoV':"<:ROV:1138455131646591017>",
    'Valorant':"<:valorant:1138455155923230730>",
    'PES':"<:pes:1138455173895815168>"
}

Emoji = {
    'RoV':":bow_and_arrow:",
    'Valorant':":video_game:",
    'PES':":soccer:"
}

Role = {}

@bot.command()
async def login(ctx:commands.Context,gra:int,room:int,no:int):
    data = search(gra,room,no)
    if data == []:
        emb = discord.Embed(colour=0xff3838,title=":x: No-data :x:")
        await ctx.message.add_reaction("❌")
        await ctx.send(embed=emb)
    else:
        room = str(data[0][4]*100+data[0][5])
        emb = discord.Embed(colour=0xff3838,title=":white_check_mark: Verify :white_check_mark:")
        emb.add_field(name=data[0][3],value=f'`Room: {room} No.{no}`',inline=False)
        await ctx.bot.guilds[0].get_member(ctx.author.id).add_roles(Role["Verify"])
        for i in data:
            emb.add_field(name=f'{emoji[i[0]]} {i[0]}  {Emoji[i[0]]}',value=f'**Team:** `{i[2]}`\n**Name:** `{i[7]}`\n**Group:** :regional_indicator_{i[1].lower()}: ',inline=True)
            await ctx.message.add_reaction(emoji[i[0]])
            await ctx.bot.guilds[0].get_member(ctx.author.id).add_roles(Role[i[0]])
            workbook = xl.load_workbook(filename="AllDBlog.xlsx")
            sheet = workbook.active
            sheet[f"K{i[8]+2}"] = "True"
            workbook.save(filename="AllDBlog.xlsx")
        await ctx.bot.guilds[0].get_channel(1142326292180648056).send(embed=emb)
        await ctx.send(embed=emb)



@bot.event
async def on_member_join(member):
    emb = discord.Embed(title="Welcome To Samarnmitr E-Sport Tournament",description="Please follow [guideline](https://drive.google.com/file/d/1Er-a7mNvXGpiEfze_83urKKXLvnak91X/view?usp=sharing) to login.",colour=0xffff00)
    await member.send(embed = emb)

@bot.event
async def on_ready():
    Role['RoV'] = bot.guilds[0].get_role(1137962924829331477)
    Role['Verify'] = bot.guilds[0].get_role(1137964222605697074)
    Role['Valorant'] = bot.guilds[0].get_role(1137962848258109581)
    Role['PES'] = bot.guilds[0].get_role(1137962781790973993)
    print("bot online")


bot.run("MTEzOTk3MDQ1ODg1NTQxOTk0NA.GVtwM9.WuN08KejqYilrUOKPq9jyckIGKU7M6HJRiF13A")

