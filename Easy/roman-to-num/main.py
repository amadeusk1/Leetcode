class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        numbers = []
        sum = 0
        for char in s:
            numbers.append(roman[char])
        num = 0
        while num < len(numbers):
            try: 
                if numbers[num] < numbers[num+1]:
                    sum += numbers[num+1] - numbers[num]
                    num += 1
                else:
                    sum += numbers[num]
            except:
                sum += numbers[num]
            num += 1  
        return sum
    

run = Solution()
print(run.romanToInt("IX"))
