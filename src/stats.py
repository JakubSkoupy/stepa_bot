from parse import parse_sloup_table
from paths import PATHS_SLOUP
import json
import os


def init_json(path: str) -> None:
    if not os.path.exists(path) or os.stat(path).st_size == 0:
        with open(path, "w") as file:
            json.dump([], path, indent=4)
    return


def report_sloup(
    state: int, author: str, path=PATHS_SLOUP["file_reports"]
) -> None:
    init_json(path)
    # TODO not loading the entire json for every new record
    reports = load_sloup_reports(path=path)

    table = parse_sloup_table()
    adjusted_sum = sum(
        (int(x[1]) / (fallof + 1)) for (fallof, x) in enumerate(table)
    ) / len(table) + int(table[0][1])

    report = {
        "date": table[0][0],
        "level": int(table[0][1]),
        "value": adjusted_sum,
        "state": state,
        "author": author,
    }
    reports.append(report)

    json_report = json.dumps(reports, indent=4)

    with open(path, "w") as out:
        out.write(json_report)


def load_sloup_reports(path=PATHS_SLOUP["file_reports"]):
    with open(path, "r") as file:
        reports = json.loads(file.read())
        return reports


def main():
    report_sloup(0)

    reports = load_sloup_reports()
    print(reports)
    pass


if __name__ == "__main__":
    main()
