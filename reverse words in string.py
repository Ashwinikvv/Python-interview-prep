Do for i in arr[:]:
      if i == '':
                arr.remove(i)
        Iterates over a copy of the list (a[:]) to avoid modification issues. as remove alters original list and size reduces

class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split(' ')
        print(arr)
        arr.reverse()
        for i in arr[:]:
            if i == '':
                arr.remove(i)
        print(arr)
        revstr=' '.join(arr)
        print(revstr)
        return revstr
obj=Solution()
print(obj.reverseWords("the sky is blue"))
        
