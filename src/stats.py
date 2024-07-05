from parse import parse_sloup_table
from paths import PATHS_SLOUP
import csv
import json
import os


def init_json(path: str) -> None:
    if not os.path.exists(path) or os.stat(path).st_size == 0:
        json.dump([], path, indent=4)
    return


def init_csv(path: str, header: list[str]) -> None:
    if not os.path.exists(path):
        with open(path, "a") as file:
            writer = csv.writer(file, [header])
            writer.writerows()


def report_sloup(state: int, author: str, path=PATHS_SLOUP["file_reports"]) -> None:
    table = parse_sloup_table()
    date = table[0][0]

    table_remove_column(table, 0)  # Remove date
    entry = table_to_entry(table)
    entry = [state, author, date] + entry

    print("Reporting entry: ", entry)

    with open(path, "a") as file:
        writer = csv.writer(file)
        writer.writerow(entry)
    return


def load_sloup_reports(path=PATHS_SLOUP["file_reports"]):
    with open(path, "r") as file:
        reports = json.loads(file.read())
        return reports


def table_to_entry(table: list[list[any]], col_s=0, col_e=-1) -> list[any]:
    """Transforms table into a single row entry"""
    row = []
    for table_row in table:
        for x in table_row[col_s:col_e]:
            row.append(x)
    return row


def table_add_column(table: list[list[any]], column: list[any], index: int) -> None:
    for table_row, item in zip(table, column):
        table_row.insert(index, item)


def table_remove_column(table: list[list[any]], index: int) -> None:
    for table_row in table:
        table_row.pop(index)


def main():
    report_sloup(0, "test")

    reports = load_sloup_reports()
    print(reports)
    pass


if __name__ == "__main__":
    main()
