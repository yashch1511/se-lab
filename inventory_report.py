from collections import defaultdict


def build_report(items):
    grouped = defaultdict(int)
    for name, quantity in items:
        grouped[name.strip().lower()] += int(quantity)

    report = []
    for name in sorted(grouped):
        report.append((name, grouped[name]))

    return report


if __name__ == "__main__":
    rows = [("Pen", 3), ("Notebook", 2), ("pen", 4), ("Pencil", 6)]
    print(build_report(rows))