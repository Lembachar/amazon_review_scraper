import pandas as pd

df = pd.read_csv("amazon_reviews_FINAL.csv")

valid = df[
    (df["verified_purchase"] == True) &
    (df["helpful_votes"] > 10)
]

valid.to_csv("amazon_reviews_valid.csv", index=False, encoding="utf-8-sig")

print("Total reviews:", len(df))
print("Valid reviews:", len(valid))