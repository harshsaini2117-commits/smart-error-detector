from collections import Counter


# Extract errors from logs (case-insensitive + flexible parsing)
def extract_errors(log_data):
    errors = []

    for line in log_data.split("\n"):
        line_lower = line.lower()

        if "error" in line_lower:
            parts = line.split("ERROR:")
            if len(parts) > 1:
                error_message = parts[1].strip()
            else:
                error_message = line.strip()

            errors.append(error_message)

    return errors


# Smart suggestion system (pattern-based, not hardcoded exact match)
def suggest_fix(error):
    error = error.lower()

    if "not found" in error:
        return "Check file path or ensure file exists"
    elif "null" in error:
        return "Ensure object is initialized before use"
    elif "memory" in error:
        return "Optimize memory usage or increase memory"
    elif "permission" in error:
        return "Check file or system permissions"
    else:
        return "Unknown error: requires manual debugging"


# Main analysis function
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
        "suggestion": suggest_fix(sorted_errors[0][0])
    }


# Input system (file + manual both)
def get_input():
    choice = input("1. Paste logs\n2. Read from file\nChoose option: ")

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


# MAIN PROGRAM
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
        print(result["suggestion"])

        # Basic severity insight
        if result["count"] > 5:
            print("\n⚠ High frequency error detected! System may be unstable.")

    else:
        print("No errors found.")
