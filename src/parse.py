import urllib.request
from lxml import etree, html

URL_SLOUP_TANK = "https://hydro.chmi.cz/hppsoldv/hpps_prfdyn.php?seq=38908612"
XPATH_TABLE = "/html/body/div[1]/div[3]/div/table[2]/tr[3]/td/div/table"


def parse_table_row(
    row: str, padding_start: int = 0, padding_end: int = 0, every_nth: int = 1
) -> list[str]:
    assert isinstance(row, str)

    separated = row.split(">")[padding_start : -(padding_end + 1)]
    result = []
    for i, element in enumerate(separated):
        if i % every_nth == 0:
            result.append(element.split("<")[0])

    return result


def parse_sloup_table() -> list[tuple[str, str]]:
    html_content = urllib.request.urlopen(URL_SLOUP_TANK).read()
    tree = html.fromstring(html_content)

    table = []
    for i in range(2, 25):
        path = XPATH_TABLE + f"/tr[{i}]"
        row_raw = html.tostring(tree.xpath(path)[0]).decode("utf-8")

        row_parsed: str = parse_table_row(
            row_raw, padding_start=2, every_nth=2, padding_end=3
        )
        table.append(row_parsed)
    return table


def main():
    sloup_table = parse_sloup_table()


if __name__ == "__main__":
    main()
