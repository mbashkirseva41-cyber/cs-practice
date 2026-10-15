import sys
from tablestats import read_rows, count_types, total_minutes, to_csv

def main():
    try:
        path = input().strip()
    except EOFError:
        return

    try:
        with open(path, encoding="utf-8") as table:
            rows = read_rows(table)
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return

    counts = count_types(rows)
    total_error_mins = total_minutes(rows, "ошибка")

    print(len(rows))
    print(len(counts))
    print(total_error_mins)

    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

if __name__ == "__main__":
    main()
