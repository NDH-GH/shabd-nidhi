import pandas as pd

df = pd.read_csv(r"..\output\shabd_nidhi_clean.csv")

master = (
    df.groupby("normalized_word", as_index=False)["frequency"]
      .sum()
      .sort_values("frequency", ascending=False)
)

master.to_csv(
    r"..\output\shabd_nidhi_master.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Unique words:", len(master))
print("Saved.")
