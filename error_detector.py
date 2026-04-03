from collections import Counter

def extract_errors(log_data):
    errors = []

    for line in log_data.split("\n"):
        if "ERROR" in line:
            error_message = line.replace("ERROR:", "").strip()
            errors.append(error_message)

    return errors


def suggest_fix(error):
    suggestions = {
        "File not found": "Check file path and ensure file exists",
        "Null pointer": "Ensure object is initialized before use",
        "Out of memory": "Optimize memory usage or increase memory"
    }

    return suggestions.get(error, "No suggestion available")


def analyze_errors(log_data):
    errors = extract_errors(log_data)

    if not errors:
        return "No errors found"

    count = Counter(errors)
    most_common_error = count.most_common(1)[0][0]

    return {
        "Most Frequent Error": most_common_error,
        "Count": count[most_common_error],
        "Suggestion": suggest_fix(most_common_error)
    }


print("Paste logs (type END to finish):")

lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

log_input = "\n".join(lines)

result = analyze_errors(log_input)

print("\nAnalysis Result:")
print(result)