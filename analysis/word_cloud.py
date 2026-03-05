import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("amazon_reviews_valid.csv")

text = " ".join(df["review_content"].astype(str))
text = text.lower()
text = re.sub(r"[^a-z\s]", "", text)

stopwords = {
    "the","and","to","is","it","this","that","for","of","in","on",
    "with","was","are","but","be","have","has","had","i","my","we",
    "you","they","he","she","as","at","by","an"
}

wc = WordCloud(
    width=800,
    height=400,
    background_color="white",
    stopwords=stopwords
).generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()