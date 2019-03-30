from collections import defaultdict
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

class StringKernels:
    def __init__(self):
        self.ps = PorterStemmer()

    def stemming(self, s):
        ns = []
        for word in s:
            ns.append(self.ps.stem(word))
        #print(ns)
        return ns

    def convert(self, words):
        string = ''
        for word in words:
            string += word
            string += ' '
        return string[0:len(string)-1]

    def compute(self, s, t, n, options='spectrum'):
        # type: (string, string, list) -> int
        if options not in ['spectrum', 'presence', 'intersection']:
            print("Invalid option!")
            return 0
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        s = s.split()
        s = self.stemming(s)
        t = t.split()
        t = self.stemming(t)
        for i in n:
            for j in range(0, len(s) - i + 1):
                if options != 'presence':
                    dict_s[self.convert(s[j:j + i])] += 1
                else:
                    dict_s[self.convert(s[j:j + i])] = 1
            for j in range(0, len(t) - i + 1):
                if options != 'presence':
                    dict_t[self.convert(t[j:j + i])] += 1
                else:
                    dict_t[self.convert(t[j:j + i])] = 1
        result = 0
        for key in dict_s.keys():
            if options != 'intersection':
                result += dict_s[key] * dict_t[key]
            else:
                result += min([dict_s[key], dict_t[key]])
        return result



if __name__ == '__main__':
    s = "Red pig like eating pig shit"
    t = "Red pig has red shit"
    sk = StringKernels()
    print(sk.compute(s, t, [1, 2], options='intersections'))



