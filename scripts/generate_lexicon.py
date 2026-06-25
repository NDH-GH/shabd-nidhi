from openai import OpenAI
import pandas as pd
import os
import time
import sys

# ==========================
# CONFIG
# ==========================

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="URL"
)

INPUT_FILE = r"..\output\shabd_nidhi_master.csv"
OUTPUT_FILE = r"..\output\shabd_nidhi_lexicon.csv"

BATCH_SIZE = 50

# ==========================
# LOAD MASTER VOCAB
# ==========================

df = pd.read_csv(INPUT_FILE)

# ==========================
# RESUME SUPPORT
# ==========================

processed_words = set()

if os.path.exists(OUTPUT_FILE):

    old_df = pd.read_csv(OUTPUT_FILE)

    processed_words = set(
        old_df["word"].astype(str).str.strip()
    )

remaining_df = df[
    ~df["normalized_word"]
    .astype(str)
    .str.strip()
    .isin(processed_words)
]

print(f"Remaining words: {len(remaining_df)}")

# Uncomment for testing
# remaining_df = remaining_df.head(200)

# ==========================
# PROCESS
# ==========================

for start in range(0, len(remaining_df), BATCH_SIZE):

    batch = remaining_df.iloc[start:start + BATCH_SIZE]

    words = batch["normalized_word"].astype(str).tolist()

    prompt = f"""
For each Hindi word:

1. Create one natural Hindi sentence using the word.
2. Identify the part of speech (POS) of that word in the sentence.

Return ONLY CSV.

Format:

word,pos,example_sentence

Allowed POS:
NOUN
VERB
ADJ
ADV
PRON
POSTPOSITION
CONJUNCTION
INTERJECTION

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

        rows = []

        for line in text.split("\n"):

            if line.count(",") < 2:
                continue

            parts = line.split(",", 2)

            word = parts[0].strip()
            pos = parts[1].strip()
            sentence = parts[2].strip()

            freq_match = batch.loc[
                batch["normalized_word"] == word,
                "frequency"
            ]

            frequency = None

            if len(freq_match) > 0:
                frequency = freq_match.iloc[0]

            rows.append({
                "word": word,
                "frequency": frequency,
                "pos": pos,
                "example_sentence": sentence
            })

        result_df = pd.DataFrame(rows)

        if len(result_df) > 0:

            if os.path.exists(OUTPUT_FILE):

                result_df.to_csv(
                    OUTPUT_FILE,
                    mode="a",
                    header=False,
                    index=False,
                    encoding="utf-8-sig"
                )

            else:

                result_df.to_csv(
                    OUTPUT_FILE,
                    index=False,
                    encoding="utf-8-sig"
                )

        print(
            f"Processed {start + len(batch)} / {len(remaining_df)}"
        )

        time.sleep(1)

    except Exception as e:

        print("ERROR:", e)

        if "401" in str(e):
            print("Authentication failed.")
            sys.exit()

        time.sleep(10)

print("DONE")
