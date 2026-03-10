from statistics import mean


def grade_summary(scores):
    cleaned = [float(value) for value in scores if value is not None]
    if not cleaned:
        return {"count": 0, "average": 0.0, "highest": 0.0, "lowest": 0.0}

    return {
        "count": len(cleaned),
        "average": round(mean(cleaned), 2),
        "highest": max(cleaned),
        "lowest": min(cleaned),
    }


if __name__ == "__main__":
    sample = [74, 81, 66, 90, 88, 79]
    print(grade_summary(sample))