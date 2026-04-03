from collections import Counter
import re


# Extract errors using regex (flexible + real-world style)
def extract_errors(log_data):
    errors = []
    pattern = re.compile(r'error[:\s]*(.*)', re.IGNORECASE)

    for line in log_data.split("\n"):
        match = pattern.search(line)
        if match:
            errors.append(match.group(1).strip())

    return errors


# Suggest fix based on pattern (pseudo-AI behavior)
def suggest_fix(error):
    error = error.lower()

    if "not found" in error:
        return "Check file path or ensure file exists"
    elif "null" in error:
        return "Ensure object is initialized"
    elif "memory" in error:
        return "Optimize memory usage"
    elif "permission" in error:
        return "Check permissions"
    else:
        return "Manual debugging required"


# Analyze errors
def analyze_errors(log_data):
    errors = extract_errors(log_data)

    if not errors:
        return None

    count = Counter(errors)
    sorted_errors = count.most_common()

    return {
        "top_errors": sorted_errors[:3],
        "most_frequent": sorted_errors[0][0],
        "count": sorted_errors[0][1],
        "all_counts": count
    }


# Input system (file + manual)
def get_input():
    choice = input("1. Paste logs\n2. Read from file\nChoose: ")

    if choice == "2":
        file_path = input("Enter file path: ")
        try:
            with open(file_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            print("File not found!")
            return None
    else:
        print("Paste logs (type END to finish):")
        lines = []
        while True:
            line = input()
            if line == "END":
                break
            lines.append(line)
        return "\n".join(lines)


# MAIN
log_data = get_input()

if log_data:
    result = analyze_errors(log_data)

    if result:
        print("\n===== Analysis Result =====")

        print("\nTop Errors:")
        for err, cnt in result["top_errors"]:
            print(f"{err} -> {cnt} times")

        print("\nMost Frequent Error:")
        print(result["most_frequent"])

        print("\nSuggestion:")
        print(suggest_fix(result["most_frequent"]))

        # Severity insight
        if result["count"] > 5:
            print("\nHigh frequency error detected!")

        # Percentage analysis
        total = sum(result["all_counts"].values())
        print("\nError Distribution:")
        for err, cnt in result["all_counts"].items():
            percent = (cnt / total) * 100
            print(f"{err}: {percent:.2f}%")

    else:
        print("No errors found.")
