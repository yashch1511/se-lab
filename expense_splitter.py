
def split_expense(total, people):
    total = float(total)
    people = int(people)

    if people <= 0:
        raise ValueError("people must be greater than zero")

    share = total / people
    rounded = round(share, 2)
    paid = rounded * people
    difference = round(total - paid, 2)

    return {
        "each_pays": rounded,
        "balance_adjustment": difference,
    }


if __name__ == "__main__":
    print(split_expense(987.5, 7))