from datetime import datetime, time
import asyncio
import pytz


async def do_periodically(
    target_time: datetime, period: int, action: any
) -> None:
    now = datetime.now(pytz.timezone("CET"))
    # target_time = target_time.replace(tzinfo=pytz.timezone("CET"))
    target_time = target_time.combine(
        now.date(),
        time(target_time.hour, target_time.minute, tzinfo=now.tzinfo),
    )

    delay = abs((target_time - now).total_seconds())

    print(f"delay = {delay}")
    await asyncio.sleep(delay)

    while True:
        await action()
        await asyncio.sleep(period)
