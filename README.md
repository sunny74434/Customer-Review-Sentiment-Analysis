# Customer-Review-Sentiment-Analysis
This Project is made to Analyze the Customer Sentiments based on their input, the following text is converted into Tokens where each token is assigned  a polarity score based on which the compound score is generated using normalization sum of each tokens ,it mainly uses Natural Language Processing Model knowns as Vader used in Sentiment Analysis.
# 🎭 Sentiment Analysis using VADER & NLTK

A lightweight Python project that analyzes the sentiment of any given text and classifies it as **Positive**, **Negative**, or **Neutral** using the VADER (Valence Aware Dictionary and sEntiment Reasoner) model from the NLTK library.

---

## 📌 What is Sentiment Analysis?

Sentiment Analysis is an NLP (Natural Language Processing) technique used to identify the emotional tone behind a piece of text. It is widely used in:

- Product reviews & feedback analysis
- Social media monitoring
- Customer support automation
- Market research

---

## ⚙️ How It Works

1. The input text is passed to VADER's `SentimentIntensityAnalyzer`
2. VADER tokenizes the text and looks up each word in its pre-built sentiment lexicon
3. It applies heuristic rules for negation, capitalization, punctuation, and booster words
4. A **compound score** is calculated (range: -1.0 to +1.0)
5. The compound score is classified using thresholds:

| Compound Score | Sentiment |
|---|---|
| >= 0.05 | Positive |
| <= -0.05 | Negative |
| Between -0.05 and 0.05 | Neutral |

---

## 🛠️ Tech Stack

- **Language:** Python
- **Library:** [NLTK](https://www.nltk.org/)
- **Model:** VADER (rule-based, no training required)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis

# Install dependencies
pip install nltk
```

---

## 🚀 Usage

```python
from sentiment import analyze_sentiment

print(analyze_sentiment("I love this project!"))   # Positive
print(analyze_sentiment("This is terrible."))      # Negative
print(analyze_sentiment("It is okay."))            # Neutral
```

---

## 📁 Project Structure

```
sentiment-analysis/
│
├── sentiment.py       # Core sentiment analysis logic
└── README.md          # Project documentation
```

---

## 📊 Example Output

```
Input:  "I absolutely love this!"
Output: Positive

Input:  "This is the worst experience ever."
Output: Negative

Input:  "The product is okay."
Output: Neutral
```

---

## 📝 Notes

- VADER works best on **short social media-style text** (tweets, reviews, comments)
- No model training is required — it's purely lexicon and rule-based
- Does not require a GPU or large compute resources

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
