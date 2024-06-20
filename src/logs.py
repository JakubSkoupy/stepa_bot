import parse
from weather_conditions import sloup_table_formatted
from table2ascii import table2ascii as t2a, PresetStyle
from client_api import client, send_message
from datetime import datetime
from timing import do_periodically


async def log_sloup() -> None:
    channel_id_test = 1249689807576367125
    channel_id_data = 1253286788299100180
    channel_id = channel_id_data

    table = sloup_table_formatted(even=True)
    await send_message(table, channel_id=channel_id)


async def log_sloup_period() -> None:
    target_time = datetime.strptime("23:59:59", "%H:%M:%S")
    delay = 60 * 60 * 24
    await do_periodically(target_time, delay, log_sloup)
