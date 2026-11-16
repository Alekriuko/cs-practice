def read_rows(lines):
    header = None
    rows = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        
        if header is None:
            header = parts
        else:
            if len(parts) == len(header):
                row_dict = {header[i]: parts[i] for i in range(len(header))}
                rows.append(row_dict)
    return rows


def count_types(rows):
    counts = {}
    for row in rows:
        t = row.get("тип")
        if t:
            counts[t] = counts.get(t, 0) + 1
    return counts


def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row.get("тип") == kind:
            val_str = row.get("минуты", "")
            if val_str:
                val_str = val_str.replace(",", ".")
                try:
                    val = float(val_str)
                    total += val
                except ValueError:
                    pass
    return round(total, 1)


def to_csv(counts):
    sorted_types = sorted(counts.keys())
    lines = ["тип,количество"]
    for t in sorted_types:
        lines.append(f"{t},{counts[t]}")
    return "\n".join(lines) + "\n"