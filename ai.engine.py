# ai_engine.py

from textblob import TextBlob
import language_tool_python
import re
import sqlite3

tool = language_tool_python.LanguageTool('en-US')


# ===============================
# 1️⃣ SENTIMENT ANALYSIS
# ===============================
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"


# ===============================
# 2️⃣ GRAMMAR CHECK
# ===============================
def grammar_check(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text, len(matches)


# ===============================
# 3️⃣ SMART SUGGESTIONS
# ===============================
def smart_suggestions(text):
    suggestions = []

    if len(text) < 15:
        suggestions.append("Try writing longer content.")

    if text.isupper():
        suggestions.append("Avoid writing everything in uppercase.")

    if not re.search(r'[.!?]', text):
        suggestions.append("Add punctuation for better clarity.")

    if "hate" in text.lower():
        suggestions.append("Try using more positive words.")

    return suggestions


# ===============================
# 4️⃣ READABILITY SCORE
# ===============================
def readability_score(text):
    words = len(text.split())
    sentences = len(re.split(r'[.!?]+', text))
    characters = len(text)

    if sentences == 0:
        sentences = 1

    if words == 0:
        words = 1

    score = 206.835 - (1.015 * (words / sentences)) - (84.6 * (characters / words))
    return round(score, 2)


# ===============================
# 5️⃣ SAVE TO DATABASE
# ===============================
def save_analysis(username, text, sentiment, readability):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            text TEXT,
            sentiment TEXT,
            readability REAL
        )
    ''')

    c.execute(
        "INSERT INTO history (username, text, sentiment, readability) VALUES (?, ?, ?, ?)",
        (username, text, sentiment, readability)
    )

    conn.commit()
    conn.close()
