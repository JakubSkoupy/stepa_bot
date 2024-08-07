import discord
from client_api import client
from commands import COMMANDS
from logs import log_sloup_period


@client.event
async def on_message(message: discord.Message) -> None:
    if message.content[0] == "!":
        await handle_command(message)


async def handle_command(message: discord.Message) -> None:
    command = message.content[1:].split(" ")[0]
    function = COMMANDS.get(command)
    if function is not None:
        await function(message)


def main() -> None:
    with open("TOKEN.txt", "r") as token_file:
        TOKEN = token_file.read()
        client.run(TOKEN)


# @client.event
# async def on_ready():
#     client.loop.create_task(log_sloup_period())


if __name__ == "__main__":
    main()
