def process_grades(records: list[str]) -> dict:
    valid_count = 0
    total = 0
    passed = set()
    skipped = 0

    for rec in records:
        if ":" not in rec:
            skipped += 1
            continue

        name, _, grade = rec.partition(":")
        name = name.strip()
        grade = grade.strip()

        if not name:
            skipped += 1
            continue

        try:
            grade = int(grade)
        except ValueError:
            skipped += 1
            continue

        if grade < 0 or grade > 100:
            skipped += 1
            continue

        valid_count += 1
        total += grade
        if grade >= 60:
            passed.add(name)

    average = round(total / valid_count, 1) if valid_count else 0.0
    return {
        "valid_count": valid_count,
        "average": average,
        "passed": sorted(passed),
        "skipped": skipped,
    }


if __name__ == "__main__":
    data = [
        "Иванов: 85",
        "Петров: 42",
        "Сидоров: abc",
        "Козлов: 90",
        ": 55",
        "Иванов: 70",
    ]
    print(process_grades(data))
