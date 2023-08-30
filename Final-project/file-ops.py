import json
import csv
from typing import List, Dict

class NewsFeed:
    def __init__(self):
        self.news_items = []

    def add_item(self, headline, category):
        self.news_items.append({"headline": headline, "category": category})

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.news_items, f, indent=4)

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            self.news_items = json.load(f)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as f:
            fieldnames = ['headline', 'category']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.news_items)

    def load_from_csv(self, filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            self.news_items = [row for row in reader]

class NewsFeedSQL:
    def __init__(self, news_feed: NewsFeed):
        self.news_feed = news_feed

    def select(self, columns: List[str], conditions: Dict[str, str]) -> List[Dict[str, str]]:
        selected_items = []
        for item in self.news_feed.news_items:
            matches_conditions = all(item.get(col) == val for col, val in conditions.items())
            if matches_conditions:
                selected_item = {col: item[col] for col in columns}
                selected_items.append(selected_item)
        return selected_items

if __name__ == "__main__":
    feed = NewsFeed()
    feed.add_item("New Technology Advancements", "Technology")
    feed.add_item("Climate Change Conference", "Environment")
    feed.add_item("Stock Market Update", "Finance")
    
    feed.save_to_json("news_feed.json")
    feed.save_to_csv("news_feed.csv")
    
    loaded_feed = NewsFeed()
    loaded_feed.load_from_json("news_feed.json")
    
    sql_like_feed = NewsFeedSQL(loaded_feed)
    selected_items = sql_like_feed.select(columns=["headline", "category"], conditions={"category": "Technology"})
    print("Selected News Items:")
    for item in selected_items:
        print(f"Headline: {item['headline']}, Category: {item['category']}")

