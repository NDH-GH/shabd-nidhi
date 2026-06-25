# Shabd-Nidhi

**Shabd-Nidhi** is an open-source Hindi vocabulary resource derived from the **NCERT Hindi textbooks (Classes 1–12)**. It provides a normalized Hindi lexical database to support educational research, language technology, corpus linguistics, and Foundational Literacy and Numeracy (FLN) initiatives.

**Repository:** https://github.com/NDH-GH/shabd-nidhi

---

## Overview

Shabd-Nidhi was developed by extracting vocabulary from the Hindi textbooks published by the **National Council of Educational Research and Training (NCERT)**, normalizing OCR and PDF extraction errors, and enriching the resulting vocabulary with corpus statistics and AI-assisted lexical information.

The dataset is intended to serve as a reusable resource for researchers, educators, curriculum designers, lexicographers, and Natural Language Processing (NLP) practitioners working with Hindi.

---

## Repository Structure

```text
shabd-nidhi/
│
├── data/
│   ├── shabd_nidhi_master.csv
│   ├── shabd_nidhi_grade_master.csv
│   ├── shabd_nidhi_lexicon.csv
│   └── shabd_nidhi_clean.csv
│
├── scripts/
│   ├── normalize_all_words.py
│   ├── create_master_vocab.py
│   ├── create_grade_master_from_pdfs.py
│   └── generate_lexicon.py
│
├── README.md
└── LICENSE
```

---

## Dataset Statistics

* **14,926** unique normalized Hindi words
* Word frequencies across NCERT Hindi textbooks (Classes 1–12)
* Earliest NCERT grade in which each word first appears
* AI-generated part-of-speech tags
* AI-generated example sentences
* OCR/PDF normalization mapping

---

## Dataset Files

### `data/shabd_nidhi_master.csv`

Contains the unique normalized Hindi vocabulary.

| Column            | Description                       |
| ----------------- | --------------------------------- |
| `normalized_word` | Normalized Hindi word             |
| `frequency`       | Total frequency across the corpus |

---

### `data/shabd_nidhi_grade_master.csv`

Contains the normalized vocabulary along with the earliest NCERT grade in which each word first appears.

| Column            | Description                                 |
| ----------------- | ------------------------------------------- |
| `normalized_word` | Normalized Hindi word                       |
| `frequency`       | Total frequency across the corpus           |
| `earliest_grade`  | First NCERT grade in which the word appears |

---

### `data/shabd_nidhi_lexicon.csv`

Provides AI-generated lexical information for each word.

| Column             | Description                   |
| ------------------ | ----------------------------- |
| `word`             | Hindi word                    |
| `frequency`        | Word frequency                |
| `pos`              | AI-generated part of speech   |
| `example_sentence` | AI-generated example sentence |

---

### `data/shabd_nidhi_clean.csv`

Maps OCR/PDF extracted word forms to their normalized forms.

| Column            | Description                     |
| ----------------- | ------------------------------- |
| `word`            | Original extracted word         |
| `normalized_word` | Corrected/normalized word       |
| `frequency`       | Frequency of the extracted word |

---

## Scripts

The `scripts/` directory contains Python programs used to generate and process the dataset, including:

* OCR/PDF text extraction
* OCR normalization
* Master vocabulary generation
* Grade mapping
* Lexical metadata generation
* Corpus processing and automation

---

## Methodology

1. Extract text from NCERT Hindi textbooks (Classes 1–12).
2. Generate a corpus-wide word frequency list.
3. Normalize OCR and PDF extraction errors using a Large Language Model (LLM).
4. Merge duplicate word forms into a single normalized vocabulary.
5. Determine the earliest NCERT grade in which each word first appears.
6. Generate AI-assisted lexical metadata, including part-of-speech tags and example sentences.

---

## Applications

Shabd-Nidhi can be used for:

* Foundational Literacy and Numeracy (FLN)
* Educational content development
* Curriculum design
* Hindi Natural Language Processing (NLP)
* Vocabulary and corpus analysis
* Readability analysis
* Lexicography
* Educational assessment
* Question generation
* Linguistic research

---

## Limitations

* OCR normalization and lexical metadata are AI-assisted and may contain occasional errors.
* A small number of words may not have an assigned earliest grade because they could not be matched reliably during automated processing.
* The dataset reflects vocabulary present in NCERT Hindi textbooks and is not intended to represent the complete Hindi lexicon.

---

## Future Work

Future versions of Shabd-Nidhi may include:

* Word meanings and definitions
* Word families and derivational relationships
* Morphological information
* Additional lexical metadata
* Expanded vocabulary from other Hindi corpora

---

## Author

**Nidhi Waldia**
Lead Educational Specialist – Literacy
Educational Initiatives (EI), India

---

## Acknowledgements

This project is based on vocabulary extracted from the Hindi textbooks published by the **National Council of Educational Research and Training (NCERT), India**. Shabd-Nidhi is an independent educational and research resource and is not affiliated with or endorsed by NCERT.

---

## Citation

If you use **Shabd-Nidhi** in research, educational resources, software, or publications, please cite this repository.

**Suggested citation**

> Waldia, N. (2026). *Shabd-Nidhi: An Open-Source Hindi Vocabulary Resource Derived from NCERT Hindi Textbooks (Classes 1–12).* GitHub. https://github.com/NDH-GH/shabd-nidhi

---

## License

The Python code in this repository is licensed under the **MIT License**.

The dataset is derived from publicly available NCERT Hindi textbooks. Users are responsible for ensuring that their use of the dataset complies with the applicable terms governing the underlying source material.
