from typing import List

class Codec:
    # Brute force, O(n), O(n)
    # def encode(self, strs: [str]) -> str:
    #     """Encodes a list of strings to a single string.
    #     """
    #     encoded_string = ""
        
    #     for s in strs:
    #         encoded_string += s + "&nbsp;"
    #     return encoded_string
        

    # def decode(self, s: str) -> [str]:
    #     """Decodes a single string to a list of strings.
    #     """
    #     strs = s.split("&nbsp;")
    #     strs.pop()
    #     return strs
    
    
    # Map the strings to a lookup dictionary, O(n), O(n) but likely smaller
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        words = {}
        positions = []
        encoded_string = ""
        
        for i, s in enumerate(strs):
            if s not in words:
                words[s] = len(words)
            positions.append(words[s])
        
        for word in words:
            encoded_string += str(words[word]) + "ā" + word + "ā"
        encoded_string += "&&" + "ā"
        
        for p in positions:
            encoded_string += str(p) + "ā"
    
        return encoded_string[:-1]
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        words = {}
        strs = []
        splitted = s.split("ā")
        
        pos, word = splitted.pop(0), splitted.pop(0)
        while pos != "&&":
            words[int(pos)] = word
            pos, word = splitted.pop(0), splitted.pop(0)
        
        strs.append(words[int(word)])
        for p in splitted:
            strs.append(words[int(p)])
        
        return strs
    
    
    # Can also use encoding similar to HTTP v1.1, 
    # Chunk the strings, and encode with size in bytes preceding word,
    # O(n), O(n)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


# Testcases
if __name__ == "__main__":
    codec = Codec()
    print(codec.decode(codec.encode(strs=["Hello","World"])))
    print(codec.decode(codec.encode(strs=[""])))
    print(codec.decode(codec.encode(strs=["Hello","World","Hello","World","Goodbye"])))
    print(codec.decode(codec.encode(strs=["tP","8f_f@^","w{=dT(0@:",""])))
