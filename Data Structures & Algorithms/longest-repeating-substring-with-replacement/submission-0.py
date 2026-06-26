class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        showup = {}
        counts = {}
        most_count = 0     # was “most_counts”
        opt = 0

        for i, ch in enumerate(s):
            showup[ch] = i
            counts[ch] = counts.get(ch, 0) + 1
            if counts[ch] > most_count:
                most_count = counts[ch]

            # current window size
            window = i - start + 1

            # shrink if we need more than k replacements
            if window - most_count > k:
                counts[s[start]] -= 1
                start += 1
                window -= 1

            if window > opt:
                opt = window

        return opt



        
        