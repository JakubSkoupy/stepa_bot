import discord
from discord.ext import commands


intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


async def send_message(message: str, channel_id=None, user_id=None) -> None:
    if channel_id is not None:
        channel = client.get_channel(channel_id)
        await channel.send(message)
    if user_id is not None:
        user = get_user(user_id)
        await user.send(message)


async def respond_ch(message: str, sender: discord.Message) -> None:
    await send_message(message, channel_id=sender.channel.id)


async def get_user(user_id: int) -> discord.user:
    return await client.fetch_user(user_id)
