import pickle as pkl

class DAO:
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__object_cache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __load(self):
        with open(self.__datasource, "rb") as file:
            self.__object_cache = pkl.load(file)

    def __dump(self):
        with open(self.__datasource, "wb") as file:
            pkl.dump(self.__object_cache, file)

    def add(self, key, obj):
        self.__object_cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__object_cache[key]
        except KeyError:
            print("Score not found")

    def remove(self, key):
        try:
            self.__object_cache.pop(key)
            self.__dump()
        except KeyError:
            print("Score not found. Could not delete")

    def get_all(self):
        return self.__object_cache.values()
