import discord
from discord.ext import commands

from parse import parse_sloup_table

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


@client.command()
async def boxeri(server, *args):

    message = ""
    if len(args) < 1:
        message = "Jak rikaji boxeri, jsem vyplej <:stepa:1249080778822778881>"
    else:
        message = (
            f"Jak rikaji boxeri, {' '.join(args)} <:stepa:1249080778822778881>"
        )
    await server.send(message)


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
        message = (
            "Sorry, nejak mi ta nadrz nejde cist. <:stepa:1249080778822778881>"
        )
    else:
        message = f"Hladina vody je ted {table[0][1]} cm (Aby nebyl potok je idealni tak 11-12 cm). <:stepa:1249080778822778881>"

    await server.send(message)


with open("TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    client.run(TOKEN)
