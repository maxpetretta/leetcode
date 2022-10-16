from typing import List


class Codec:
    # Concatenate all strings with non-ASCII delimiter, O(n), O(1) for encode O(n) for decode
    # def encode(self, strs: List[str]) -> str:
    #     """Encodes a list of strings to a single string.
    #     """
    #     s = chr(257).join(strs)
    #     return s
        

    # def decode(self, s: str) -> List[str]:
    #     """Decodes a single string to a list of strings.
    #     """
    #     strs = s.split(chr(257))
    #     return strs
    
    
    # Map the strings to a lookup dictionary, O(n), O(n) but likely smaller
    # def encode(self, strs: List[str]) -> str:
    #     """Encodes a list of strings to a single string.
    #     """
    #     words = {}
    #     positions = []
    #     encoded_string = ""
        
    #     for i, s in enumerate(strs):
    #         if s not in words:
    #             words[s] = len(words)
    #         positions.append(words[s])
        
    #     for word in words:
    #         encoded_string += str(words[word]) + "ā" + word + "ā"
    #     encoded_string += "&&" + "ā"
        
    #     for p in positions:
    #         encoded_string += str(p) + "ā"
    
    #     return encoded_string[:-1]
        

    # def decode(self, s: str) -> List[str]:
    #     """Decodes a single string to a list of strings.
    #     """
    #     words = {}
    #     strs = []
    #     splitted = s.split("ā")
        
    #     pos, word = splitted.pop(0), splitted.pop(0)
    #     while pos != "&&":
    #         words[int(pos)] = word
    #         pos, word = splitted.pop(0), splitted.pop(0)
        
    #     strs.append(words[int(word)])
    #     for p in splitted:
    #         strs.append(words[int(p)])
        
    #     return strs
    
    
    # Use chunked transfer encoding like HTTP v1.1, O(n), O(1) for encode O(n) for decode
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for word in strs:
            s += str(len(word)) + chr(257) + word
        return s
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs, i = [], 0
        while i < len(s):
            j = i
            while s[j] != chr(257):
                j += 1
            length = int(s[i:j])
            strs.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return strs


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
