import requests
import wikipedia
import time
import re

# 🔑 Replace with your real NewsAPI key
NEWS_API_KEY = "YOUR_API_KEY"

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    return text

def extract_keywords(text):
    words = text.lower().split()
    stopwords = ['the','is','on','at','with','a','an','of','to','and','was','in']
    keywords = [w for w in words if w not in stopwords]
    return keywords[:6]  # take top 6 imp words

def get_news(query):
    keywords = extract_keywords(query)
    query = " ".join(keywords)
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}&pageSize=5"

    try:
        response = requests.get(url).json()
        print("DEBUG API STATUS:", response.get("status"))

        if response.get("status") != "ok":
            print("❌ API ERROR:", response.get("message"))
            return []

        articles = response.get("articles", [])
        print("DEBUG Articles Found:", len(articles))

        news_texts = []
        for article in articles:
            text = article["title"] + " " + str(article.get("description", ""))
            news_texts.append(text)

        return news_texts

    except Exception as e:
        print("Error:", e)
        return []

def get_wikipedia(query):
    try:
        results = wikipedia.search(query)
        if not results:
            return None
        page = wikipedia.page(results[0])
        return page.summary
    except:
        return None

def check_match(user_text, sources):
    user_words = extract_keywords(user_text)
    score = 0

    for src in sources:
        src = src.lower()
        count = 0
        for word in user_words:
            if word in src:
                count += 1
        if count >= 2:
            score += 1
    return score

def analyze_news(text):
    start = time.time()
    print("\n===== RESULT =====")

    news_sources = get_news(text)
    wiki = get_wikipedia(text)

    all_sources = news_sources.copy()
    if wiki:
        all_sources.append(wiki)

    print("Total Sources:", len(all_sources))

    if len(all_sources) == 0:
        print("Prediction: ⚠️ No data found")
        return

    match_score = check_match(text, all_sources)

    if len(news_sources) == 0:
        prediction = "❌ Likely FAKE (No news coverage found)"
    elif match_score >= 4 and len(news_sources) >= 4:
        prediction = "✅ Likely REAL"
    elif match_score >= 2:
        prediction = "⚠️ UNCERTAIN"
    else:
        prediction = "❌ Likely FAKE"

    end = time.time()

    print("Prediction:", prediction)
    print("Match Score:", match_score)
    print("Time Taken:", round(end - start, 3), "sec")

while True:
    user_input = input("\nEnter news (or type exit): ")
    if user_input.lower() == "exit":
        break
    analyze_news(user_input)