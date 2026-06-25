from openai import OpenAI
import pandas as pd
import time
import os

# ==========================
# CONFIG
# ==========================

API_KEY = "YOUR_API_KEY"

client = OpenAI(
    api_key=API_KEY,
    base_url="URL"
)

INPUT_FILE = r"..\input\hindi_word_frequency.csv"
OUTPUT_FILE = r"..\output\shabd_nidhi_clean.csv"

BATCH_SIZE = 50

# ==========================
# LOAD INPUT
# ==========================

df = pd.read_csv(INPUT_FILE)

# Change these if your column names differ
WORD_COL = "word"
FREQ_COL = "frequency"

# ==========================
# RESUME SUPPORT
# ==========================

processed_words = set()

if os.path.exists(OUTPUT_FILE):
    old_df = pd.read_csv(OUTPUT_FILE)
    processed_words = set(old_df["word"].astype(str))

results = []

# ==========================
# PROCESS IN BATCHES
# ==========================

remaining_df = df[
    ~df[WORD_COL].astype(str).isin(processed_words)
]

print(f"Remaining words: {len(remaining_df)}")

for start in range(0, len(remaining_df), BATCH_SIZE):

    batch = remaining_df.iloc[start:start+BATCH_SIZE]

    words = batch[WORD_COL].astype(str).tolist()

    prompt = f"""
You are a Hindi linguist.

For each Hindi word:

1. Correct OCR/PDF extraction errors.
2. Return ONLY CSV.

Format:

original_word,normalized_word

Words:

{chr(10).join(words)}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = response.choices[0].message.content.strip()

        lines = text.split("\n")

        parsed = []

        for line in lines:

            if "," not in line:
                continue

            parts = line.split(",", 1)

            original = parts[0].strip()
            normalized = parts[1].strip()

            parsed.append({
                "word": original,
                "normalized_word": normalized
            })

        parsed_df = pd.DataFrame(parsed)

        freq_map = dict(
            zip(
                batch[WORD_COL].astype(str),
                batch[FREQ_COL]
            )
        )

        parsed_df["frequency"] = parsed_df["word"].map(freq_map)

        if os.path.exists(OUTPUT_FILE):
            parsed_df.to_csv(
                OUTPUT_FILE,
                mode="a",
                header=False,
                index=False,
                encoding="utf-8-sig"
            )
        else:
            parsed_df.to_csv(
                OUTPUT_FILE,
                index=False,
                encoding="utf-8-sig"
            )

        print(
            f"Processed {start + len(batch)} / {len(remaining_df)}"
        )

        time.sleep(1)

    except Exception as e:

        print("ERROR")
        print(e)

        time.sleep(10)

print("DONE")
