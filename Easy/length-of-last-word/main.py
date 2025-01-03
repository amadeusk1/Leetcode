class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlist = []
        word = ""
        for char in s:
            if char == " ":
                if word != "":
                    wordlist.append(word)
                word = ""
            else:
                word += char
        if word != "" and word != " ":
            wordlist.append(word)
        return len(wordlist[len(wordlist)-1])

#testing
run = Solution()
print(run.lengthOfLastWord("   fly me   to   the moon  "))
