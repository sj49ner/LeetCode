class Solution:
  def romanToInt(self, s):
    mapping = {
      'i': 1,
      'v': 5,
      'x': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }

    total = 0

    for roman in range(len(s) - 1):
      if mapping[s[roman]] >= mapping[s[roman+1]]:
        total += mapping[s[roman]]
      else:
        total -= mapping[s[roman]]
    total += mapping[s[roman-1]]
    print(total)

romanNum = Solution()
romanNum.romanToInt("iii")

