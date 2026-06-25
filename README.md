# Shabd-Nidhi

**Shabd-Nidhi** is an open Hindi vocabulary resource derived from the **NCERT Hindi textbooks (Classes 1–12)**. It provides a normalized Hindi lexical database to support educational research, language technology, corpus linguistics, and Foundational Literacy and Numeracy (FLN) initiatives.

---

## Overview

Shabd-Nidhi was created by extracting vocabulary from the Hindi textbooks published by the National Council of Educational Research and Training (NCERT), normalizing OCR and PDF extraction errors, and enriching the resulting vocabulary with corpus statistics and AI-assisted lexical information.

The dataset is intended to serve as a reusable resource for researchers, educators, curriculum designers, lexicographers, and Natural Language Processing (NLP) practitioners working with Hindi.

---

## Dataset Statistics

- **14,926** unique normalized Hindi words
- Word frequencies across NCERT Hindi textbooks (Classes 1–12)
- Earliest NCERT grade in which each word first appears
- AI-generated example sentence for each word
- OCR/PDF normalization mapping

---

## Repository Contents

### `shabd_nidhi_master.csv`

Contains the unique normalized Hindi vocabulary.

| Column | Description |
|--------|-------------|
| `normalized_word` | Normalized Hindi word |
| `frequency` | Total frequency across the corpus |

---

### `shabd_nidhi_grade_master.csv`

Adds the earliest NCERT grade in which each word first appears.

| Column | Description |
|--------|-------------|
| `normalized_word` | Normalized Hindi word |
| `frequency` | Total frequency across the corpus |
| `earliest_grade` | First NCERT grade in which the word appears |

---

### `shabd_nidhi_lexicon.csv`

Provides AI-generated lexical information for each word.

| Column | Description |
|--------|-------------|
| `word` | Hindi word |
| `frequency` | Word frequency |
| `pos` | AI-generated part of speech |
| `example_sentence` | AI-generated example sentence |

---

### `shabd_nidhi_clean.csv`

Maps extracted OCR/PDF word forms to their normalized forms.

| Column | Description |
|--------|-------------|
| `word` | Original extracted word |
| `normalized_word` | Corrected/normalized word |
| `frequency` | Frequency of the extracted word |

---

## Methodology

1. Extract text from NCERT Hindi textbooks (Classes 1–12).
2. Generate a corpus-wide word frequency list.
3. Normalize OCR and PDF extraction errors using a Large Language Model (LLM).
4. Merge duplicate word forms into a single normalized vocabulary.
5. Determine the earliest NCERT grade in which each word first appears.
6. Generate lexical metadata (part of speech and example sentence) using AI.

---

## Applications

Shabd-Nidhi can be used for:

- Foundational Literacy and Numeracy (FLN)
- Educational content development
- Curriculum design
- Hindi Natural Language Processing (NLP)
- Vocabulary and corpus analysis
- Readability analysis
- Lexicography
- Educational assessment
- Question generation
- Linguistic research

---

## Limitations

- OCR normalization and lexical metadata are AI-assisted and may contain occasional errors.
- A small number of words may not have an assigned earliest grade because they could not be matched reliably during automated processing.
- The dataset reflects the vocabulary present in NCERT Hindi textbooks and is not intended to represent the complete Hindi lexicon.

---

## Author

**Nidhi Waldia**  
Lead Educational Specialist – Literacy  
Educational Initiatives (EI), India

---

## Citation

If you use **Shabd-Nidhi** in research, educational resources, software, or publications, please cite this GitHub repository.

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.
