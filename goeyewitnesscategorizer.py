import sqlite3
import argparse
import pandas as pd

def load_signature_file(path):
    signatures = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if "|" not in line:
                continue
            parts, tag = line.strip().split("|", 1)
            patterns = [p.strip().lower() for p in parts.split(";") if p.strip()]
            signatures.append((patterns, tag.strip()))
    return signatures

def match_all_patterns(html, signature_list):
    html_lower = html.lower()
    for patterns, tag in signature_list:
        if all(pat in html_lower for pat in patterns):
            return tag
    return None

def process_gowitness_db(db_path, categories_file, creds_file, output_file):
    categories = load_signature_file(categories_file)
    creds = load_signature_file(creds_file)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT url, title, html FROM results")
    rows = cursor.fetchall()

    report_data = []

    for url, title, html in rows:
        if not html:
            continue
        category = match_all_patterns(html, categories)
        default_creds = match_all_patterns(html, creds)

        report_data.append({
            "URL": url,
            "Title": title,
            "Category": category if category else "Uncategorized",
            "Default Credentials": default_creds if default_creds else ""
        })

    df = pd.DataFrame(report_data)
    df.to_csv(output_file, index=False)
    print(f"[+] CSV report written to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Categorize GoWitness results and match default credentials.")
    parser.add_argument("--db", required=True, help="Path to GoWitness SQLite database (gowitness.sqlite)")
    parser.add_argument("--categories", required=True, help="Path to EyeWitness categories.txt")
    parser.add_argument("--creds", required=True, help="Path to EyeWitness signatures.txt (default creds)")
    parser.add_argument("--output", default="gowitness_report.csv", help="Path to output CSV report (default: gowitness_report.csv)")

    args = parser.parse_args()

    process_gowitness_db(
        db_path=args.db,
        categories_file=args.categories,
        creds_file=args.creds,
        output_file=args.output
    )

if __name__ == "__main__":
    main()
