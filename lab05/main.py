from tablestats import *

def main():
    try:
        filename = input().strip()
    except EOFError:
        return

    if not filename:
        return

    with open(filename, encoding="utf-8") as table:
        rows = read_rows(table)

    num_records = len(rows)
    
    counts = count_types(rows)
    num_types = len(counts)
    
    err_minutes = total_minutes(rows, "ошибка")

    # Вывод трёх требуемых значений
    print(num_records)
    print(num_types)
    print(err_minutes)

    # Запись сводки в summary.csv
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

if __name__ == "__main__":
    main()