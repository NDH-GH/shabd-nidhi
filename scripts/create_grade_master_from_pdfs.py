import fitz
import pandas as pd
import re
from pathlib import Path

# ==========================
# PATHS
# ==========================

PDF_FOLDER = Path(
    r"C:\Users\nidhi.waldia.EI-LAP-8913\Downloads\downloads\Hindi ncert"
)

CLEAN_FILE = Path(
    r"..\output\shabd_nidhi_clean.csv"
)

MASTER_FILE = Path(
    r"..\output\shabd_nidhi_master.csv"
)

OUTPUT_FILE = Path(
    r"..\output\shabd_nidhi_grade_master.csv"
)

# ==========================
# LOAD CLEAN FILE
# ==========================

clean_df = pd.read_csv(CLEAN_FILE)

# expected columns:
# word, normalized_word

normalize_map = dict(
    zip(
        clean_df["word"].astype(str),
        clean_df["normalized_word"].astype(str)
    )
)

# ==========================
# GRADE MAP
# ==========================

grade_map = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12
}

# ==========================
# FIND EARLIEST GRADE
# ==========================

earliest_grade = {}

pdf_files = list(PDF_FOLDER.glob("*.pdf"))

print(f"Found {len(pdf_files)} PDFs")

for pdf_file in pdf_files:

    filename = pdf_file.name.lower()

    first_char = filename[0]

    if first_char not in grade_map:
        continue

    grade = grade_map[first_char]

    print(f"Processing {pdf_file.name} -> Grade {grade}")

    try:

        doc = fitz.open(pdf_file)

        text = ""

        for page in doc:
            text += page.get_text()

        doc.close()

        words = re.findall(
            r"[\u0900-\u097F]+",
            text
        )

        for word in words:

            normalized_word = normalize_map.get(
                word,
                word
            )

            if normalized_word not in earliest_grade:

                earliest_grade[normalized_word] = grade

            else:

                earliest_grade[normalized_word] = min(
                    earliest_grade[normalized_word],
                    grade
                )

    except Exception as e:

        print(f"Error in {pdf_file.name}")
        print(e)

# ==========================
# CREATE GRADE DATAFRAME
# ==========================

grade_df = pd.DataFrame({
    "normalized_word": list(earliest_grade.keys()),
    "earliest_grade": list(earliest_grade.values())
})

# ==========================
# LOAD MASTER FILE
# ==========================

master_df = pd.read_csv(MASTER_FILE)

# expected:
# normalized_word, frequency

# ==========================
# MERGE
# ==========================

result = master_df.merge(
    grade_df,
    on="normalized_word",
    how="left"
)

# ==========================
# SAVE NEW FILE
# ==========================

result.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

print()
print("DONE")
print(f"Saved: {OUTPUT_FILE}")
print(f"Rows: {len(result)}")
