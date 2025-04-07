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
- Format:  
