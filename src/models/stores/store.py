import uuid
from src.common.database import Database
import src.models.stores.constants as StoreConstants
import src.models.stores.errors as StoreErrors

class Store():
    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self.id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store {}>".format(self.name)

    def json(self):
        return {
            "_id": self.id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_id(cls,id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"_id":id}))

    def save_to_mongo(self):
        Database.insert(StoreConstants.COLLECTION, self.json())

    @classmethod
    def get_by_name(cls, store_name):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"name":name}))

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"url_prefix":{"$regex":'^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls, url):
        """

        :param url: item's URL
        :return:
        """
        for i in range(0, len(url)+1):
            try:
                store = cls.get_by_url_prefix(url[:1])
                return store
            except:
                raise StoreErrors.StoreNotFoundException("Store not found")
