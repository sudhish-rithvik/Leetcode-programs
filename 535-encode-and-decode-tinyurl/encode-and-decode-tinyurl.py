class Codec:

    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl):
        self.counter += 1
        shortUrl = "http://tinyurl.com/" + str(self.counter)
        self.url_map[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        return self.url_map[shortUrl]