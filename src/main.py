import discord
import stats
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
            "Jak rikaji boxeri,"
            + " ".join(args)
            + "<:stepa:1249080778822778881>"
        )
    await server.send(message)


@client.command()
async def repo(server):
    await server.send(
        "Palo prestan vymyslet picoviny, a pust Kubu do toho repozitare."
    )


@client.command()
async def sloup(server, *args):
    table = parse_sloup_table()
    message = ""

    # Show current water state
    if len(args) == 0:
        if table is None or table == [] or table[0] == []:
            message = "Sorry, nejak mi ta nadrz nejde cist. <:stepa:1249080778822778881>"
        else:
            message = (
                f"Hladina vody je ted {table[0][1]} cm "
                "(Aby nebyl potok je idealni tak 11-12 cm)."
                " <:stepa:1249080778822778881>"
            )
    # Receive report
    elif args[0] in ["r", "report"]:
        if len(args) == 1:
            message = """Jeste mi musis nahlasit stav potoka:
                            0 => Sucho
                            1 => Konci to u sharmy
                            2 => Mokro jak blazen
                       """
        else:
            message = "Diky za zpravu, beru to na vedomi."
            stats.report_sloup(args[1])

    # Send message
    await server.send(message)


with open("TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    client.run(TOKEN)
