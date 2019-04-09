# -*- CODING:UTF-8 -*- #

class Solusion(object):

    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        r = []
        for d in digits:
            c = phone[d]
            # print c
            if len(r) == 0:
                for e in c:
                    r.append(e)
            else:
                c_r = []
                for e in c:
                    for c_e in r:
                        c_r.append(c_e + e)
                r = c_r
        return r


s = Solusion()
print s.letterCombinations('23')
