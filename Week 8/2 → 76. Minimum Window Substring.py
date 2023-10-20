class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hd, tl = 0, 0
        min_win = ""
        
        substr_counter = Counter(t)
        substr_count = len(t)
        
        while tl <= len(s) - 1:
            print(tl)
            if substr_counter[s[tl]] > 0:
                substr_count -= 1
                
            substr_counter[s[tl]] -= 1
            
            while substr_count == 0:
                win_len = tl - hd + 1
                
                if len(min_win) == 0 or len(min_win) > win_len:
                    min_win = s[hd:tl + 1]
                    
                substr_counter[s[hd]] += 1
                
                if substr_counter[s[hd]] > 0:
                    substr_count += 1
                    
                hd += 1
                
            tl += 1
                
        return min_win