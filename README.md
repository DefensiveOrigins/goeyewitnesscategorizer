# goeyewitnesscategorizer
goeyewitnesscategorizer

# GoWitness + EyeWitness HTML Matcher

This tool parses a GoWitness SQLite database and cross-references HTML content from discovered web interfaces against EyeWitness-style category and default credentials signature files. It produces a CSV report mapping each web interface to a category and potential default credentials.

## 🔧 Features

- Match HTML against EyeWitness-style pattern signatures.
- Assign a **category** and **default credentials** to each matched entry.
- Output a clean, filterable **CSV report**.
- CLI-driven with clear arguments.

## 🗃️ Input Files

### 1. GoWitness SQLite DB
- Typically named `gowitness.sqlite`
- Must contain a `results` table with `url`, `title`, and `html` columns

### 2. `categories.txt`
- Format:  ```string1;string2;...|CategoryName```
- All strings must appear in the HTML for the category to be assigned.

### 3. `signatures.txt`
- Format:  ```string1;string2;...|username:password or other default cred format```

- - All strings must match for the full value after the pipe (`|`) to be recorded in the **Default Credentials** column.

## categoriy and creds/signatures files
You can make your own, or rely on work done with the eyewitness project to get you started quickly
```bash
wget https://raw.githubusercontent.com/RedSiege/EyeWitness/refs/heads/master/Python/signatures.txt
wget https://raw.githubusercontent.com/RedSiege/EyeWitness/refs/heads/master/Python/categories.txt
```

## 📤 Output

- CSV report (default: `gowitness_report.csv`) with the following columns:
- `URL`
- `Title`
- `Category`
- `Default Credentials`

## 🚀 Usage

```bash
python goeyewitnesscategorizer.py \
--db gowitness.sqlite \
--categories categories.txt \
--creds signatures.txt \
--output output_report.csv
```

## Requirements
* Python 3.7+
*  pandas

### Install Requirements 
*  pip install pandas

