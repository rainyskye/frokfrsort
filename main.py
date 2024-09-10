import csv
from collections import defaultdict
import sys

def sort_csv(input_file, output_file, split_level='Feed frokfrdk'):
    with open(input_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Group by Current Level
    grouped_data = defaultdict(list)
    for row in data:
        grouped_data[row['Current level']].append(row['Member'])

    # Sort members alphabetically within each group
    for level in grouped_data:
        grouped_data[level].sort(key=str.lower)

    # Write the sorted data to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tier', 'Member', '', 'skye was here'])  # Header row

        for level, members in sorted(grouped_data.items()):
            writer.writerow([f"{level}:"])  # Tier name
            if level == split_level:
                # Split this level into two columns
                half = len(members) // 2
                for i in range(max(len(members[:half]), len(members[half:]))):
                    col1 = members[i] if i < len(members[:half]) else ""
                    col2 = members[i + half] if i + half < len(members) else ""
                    writer.writerow(["", col1, col2])
            else:
                # Write other levels in the first column
                for member in members:
                    writer.writerow(["", member])
            writer.writerow([])  # Blank line between tiers

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    split_level = 'Feed frokfrdk'  # Tier to make 2 columns

    sort_csv(input_file, output_file, split_level)
    print(f"Sorted member list has been written to {output_file}")