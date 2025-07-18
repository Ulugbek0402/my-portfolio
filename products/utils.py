import csv
import os.path


def read(filename: str) -> list:
    path = f"data/{filename}"
    if os.path.exists(path=path):
        with open(file=path, mode="r", encoding="UTF-8") as file:
            return list(file)
    return []


def write(filename: str, data: list, mode: str = "w") -> None:
    path = f"data/{filename}"
    with open(file=path, mode=mode, encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        if mode == "w":
            writer.writerows(data)
        else:
            writer.writerow(data)


def generate_id(filename: str) -> int:
    data = read(filename=filename)
    if len(data) == 0:
        return 1
    else:
        return int(data[-1][0]) + 1
