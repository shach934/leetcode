535. Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

class Codec:
    
    def __init__(self):
        self.dic = {}
        self.count = 0
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.dic[self.count + 1] = longUrl
        self.count += 1
        return 'http://tinyurl.com/' + str(self.count)
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        num = shortUrl.split('/')[-1]
        return self.dic[int(num)]

其实是应该要设计一个hash function才对。那样的话，能够压缩并且不会随便被破解
但是这个里面其实就是用了个dictionary记住了。而不是算出来的，会使用大量的空间
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))