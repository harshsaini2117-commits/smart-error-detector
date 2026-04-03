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
    
def suggest_fix(error):
    if "not found" in error.lower():
        return "Check file path or file existence"
    elif "null" in error.lower():
        return "Check object initialization"
    elif "memory" in error.lower():
        return "Optimize memory usage"
    else:
        return "Unknown error: requires manual debugging"

print("Paste logs (type END to finish):")

choice = input("1. Paste logs\n2. Use file\nChoose option: ")

if choice == "2":
    file_path = input("Enter file path: ")
    with open(file_path, "r") as f:
        log_input = f.read()
else:
    print("Paste logs (END to stop):")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    log_input = "\n".join(lines)

if count["ERROR"] > 5:
    print("High system instability detected")

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

file_path = input("Enter file path: ")
with open(file_path, "r") as f:
    log_input = f.read()

from collections import Counter

def analyze_errors(log_data):
    errors = extract_errors(log_data)

    if not errors:
        return "No errors found"

    count = Counter(errors)

    sorted_errors = count.most_common()

    return {
        "Top Errors": sorted_errors[:3],
        "Most Frequent Error": sorted_errors[0][0],
        "Suggestion": suggest_fix(sorted_errors[0][0])
    }
