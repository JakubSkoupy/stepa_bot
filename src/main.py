import discord
from tokens import TOKEN
from discord.ext import commands

from parse import parse_sloup_table

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


@client.command()
async def boxeri(server):
    await server.send("Jak rikaji boxeri, jsem vyplej :stepa:")


@client.command()
async def repo(server):
    await server.send(
        "Palo prestan vymyslet picoviny, a pust Kubu do toho repozitare."
    )


@client.command()
async def sloup(server):
    table = parse_sloup_table()

    message = ""
    if table is None or table == [] or table[0] == []:
        message = "Sorry, nejak mi ta nadrz nejde cist."
    else:
        message = f"V nadrzi je ted {table[0][1]} cm vody."

    await server.send(message)


client.run(TOKEN)
