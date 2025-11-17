import json
import os

EXPECTED_COUNTS = {
    "Actors": 5,
    "Classes": 4,
    "Skills": 20,
    "Items": 15,
    "Enemies": 10,
    "Weapons": 8,
    "Armors": 8,
    "Troops": 5,
    "States": 5
}

def analyze_database():
    results = {}
    total_current = 0
    total_expected = 0

    for filename, expected_count in EXPECTED_COUNTS.items():
        filepath = os.path.join("data", f"{filename}.json")
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                # Subtract 1 for the null entry at the beginning of most RPG Maker MZ data files
                current_count = len(data) - 1 if data and data[0] is None else len(data)
                results[filename] = {
                    "current": current_count,
                    "expected": expected_count,
                    "percentage": (current_count / expected_count) * 100
                }
                total_current += current_count
                total_expected += expected_count
        except (FileNotFoundError, json.JSONDecodeError) as e:
            results[filename] = {"error": str(e)}

    overall_percentage = (total_current / total_expected) * 100 if total_expected > 0 else 0
    return results, total_current, total_expected, overall_percentage

if __name__ == "__main__":
    results, total_current, total_expected, overall_percentage = analyze_database()

    print("=== RPG MAKER MZ DATABASE COMPLETENESS ANALYSIS ===\n")
    print(f"{'Category':<12} {'Current':<8} {'Expected':<8} {'%Complete':<10} {'Status'}")
    print("-" * 60)

    for category, data in results.items():
        if "error" in data:
            print(f"{category:<12} {'N/A':<8} {'N/A':<8} {'N/A':<10} {data['error']}")
        else:
            status = "Complete" if data['percentage'] >= 100 else "Needs Enhancement"
            print(f"{category:<12} {data['current']:<8} {data['expected']:<8} {data['percentage']:.1f}{'%':<9} {status}")

    print("-" * 60)
    print(f"OVERALL      {total_current:<8} {total_expected:<8} {overall_percentage:.1f}{'%':<9} Complete")
    print("=== DETAILED FINDINGS ===\n")

    for category, data in results.items():
        if "error" not in data and data['percentage'] < 100:
            needed = data['expected'] - data['current']
            print(f"• {category}: Need {needed} more entries ({data['percentage']:.1f}% complete)")

