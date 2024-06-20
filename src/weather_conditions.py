import discord
import parse
from client_api import respond_ch
import stats


async def sloup(message: discord.Message) -> None:
    args = message.content.split(" ")[1:]
    response = ""

    if len(args) == 0:
        table = parse.parse_sloup_table()
        response = (
            f"Hladina vody je ted {table[0][1]} cm "
            "(Aby nebyl potok je idealni tak 11-12 cm)."
            " <:stepa:1249080778822778881>"
        )

    elif args[0] in ["report", "r"]:
        if len(args) == 1:
            response = """Jeste mi musis nahlasit stav potoka:
                            0 => Sucho
                            1 => Konci to u sharmy
                            2 => Mokro jak blazen
                       """

        elif len(args) == 2:

            level = int(args[1])
            if level == 0 or level == 1 or level == 2:
                response = "Diky za zpravu, beru to na vedomi"
                stats.report_sloup(level, message.author)
            else:
                response = "No takhle snad ani byt nemuze"
    else:
        response = "Zadal jsi ten prikaz nejak spatne"

    await respond_ch(response, message)