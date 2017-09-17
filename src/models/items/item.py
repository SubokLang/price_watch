from bs4 import BeautifulSoup
import requests
import re

from src.common.database import Database
import src.models.items.constants as ItemConstants

class Item():
    def __init__(self, name, price, store):
        self.name = name
        self.url = url
        self.store = store
        tag_name = store.get_tag_name()
        query = store.query()
        self.price = self.load_price(tag_name, query)

    def __repr__(self):
        return "<Item {} with URL {}>".format(self.name, self.url)

    def load_price(self, tag_name, query):
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query)
        string_price = element.text.strip()

        pattern = re.compile("(\d+.\d+)")
        match = pattern.search(string_price)

        return match.group()

    def save_to_mongo(self):
        Database.insert(ItemConstants.COLLECTION, self.json())

    def load_from_mongo(self):
        pass

    def json(self):
        return {
            "name": self.name,
            "url": self.url
        }
