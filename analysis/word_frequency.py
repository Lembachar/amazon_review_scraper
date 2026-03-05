import pandas as pd
import re
from collections import Counter

df = pd.read_csv("amazon_reviews_valid.csv")

text = " ".join(df["review_content"].astype(str))

text = text.lower()
text = re.sub(r"[^a-z\s]", "", text)

words = text.split()

stopwords = {
    "the","and","to","is","it","this","that","for","of","in","on",
    "with","was","are","but","be","have","has","had","i","my","we",
    "you","they","he","she","as","at","by","an"
}

words = [w for w in words if w not in stopwords and len(w) > 2]

freq = Counter(words)

top_words = freq.most_common(20)

for w, c in top_words:
    print(w, ":", c)