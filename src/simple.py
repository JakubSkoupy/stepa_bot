import discord
from client_api import respond_ch


async def boxeri(message: discord.Message) -> None:
    args = message.content.split(" ")[1:]
    response = ""
    if len(args) < 1:
        response = (
            "Jak rikaji boxeri, jsem vyplej <:stepa:1249080778822778881>"
        )
    else:
        response = (
            "Jak rikaji boxeri, "
            + " ".join(args)
            + " <:stepa:1249080778822778881>"
        )
    await respond_ch(response, message)


async def repo(message: discord.Message) -> None:
    await respond_ch("Palo prestan vymyslet picoviny... vsak vis", message)
