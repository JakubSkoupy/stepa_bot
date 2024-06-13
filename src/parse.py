import urllib.request
from lxml import etree, html
from paths import PATHS_SLOUP, PATHS_TRAM


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
    PATHS_SLOUP["xpath_l_table"]
    html_content = urllib.request.urlopen(PATHS_SLOUP["url_level"]).read()
    tree = html.fromstring(html_content)

    table = []
    for i in range(2, 25):
        path = PATHS_SLOUP["xpath_l_table"] + f"/tr[{i}]"
        row_raw = html.tostring(tree.xpath(path)[0]).decode("utf-8")
        row_parsed: str = parse_table_row(
            row_raw, padding_start=2, every_nth=2, padding_end=3
        )
        table.append(row_parsed)
    return table


def parse_trams() -> list[tuple[int, str, str]]:
    trees = [
        html.fromstring(urllib.request.urlopen(x).read())
        for x in [
            PATHS_TRAM["url_salina_center"],
            PATHS_TRAM["url_salina_out"],
        ]
    ]

    for tree in trees:
        tram = html.tostring(
            tree.xpath(PATHS_TRAM["xpath_first_num"])[0]
        ).decode("utf-8")
        print(tram)
    return


def main():
    sloup_table = parse_sloup_table()
    parse_trams()


if __name__ == "__main__":
    main()
