import requests
from bs4 import BeautifulSoup
from collections import Counter

def analyze_news_page(url):
    headers = { # 0. Set Headers to Avoid Blocking 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers) # 1. Get Page Content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    text = soup.get_text() # 2. Word Count
    words = text.lower().split()

    clean_words = []
    for word in words:
        clean_word = ''.join(char for char in word if char.isalnum())
        if clean_word:
            clean_words.append(clean_word)
    word_freq = Counter(clean_words)
    

    tags = [tag.name for tag in soup.find_all()] # 3. HTML Tags Count
    tag_freq = Counter(tags)

    links_count = len(soup.find_all('a')) # 4. Links count
    
    images_count = len(soup.find_all('img')) # 5. Images count
    
    return {
        'words': dict(word_freq.most_common(10)),
        'tags': dict(tag_freq),
        'links': links_count,
        'images': images_count
    }

def main():
    print("Аналіз новинної сторінки\n"
          "Натиснiть Enter для вiдображення за замовчуванням (https://www.bbc.com/news):")
    url = input("Введіть URL: ") or "https://www.bbc.com/news"
    result = analyze_news_page(url)
    print(f"Топ-10 слів: {result['words']}\n"
          f"HTML-теги: {result['tags']}\n"
          f"Посилання: {result['links']}\n"
          f"Зображення: {result['images']}")

if __name__ == "__main__":
    main()