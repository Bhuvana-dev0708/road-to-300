def isAnagrams(s,t):
       if len(s)!=len(t):
            return False
       else:
            return sorted(s)==sorted(t)