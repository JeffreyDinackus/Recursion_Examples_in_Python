

letters = {
  "X" : 10,
  "IV" : 9,
  "V" : 5,
  "IV" : 4,
  "I" : 1
}


# this one is a plain ol leetcode solution to Roman to Integer, I couldn't figure out how to make it recursion. It is set for nums 1 - 39.

def roman_to_int(numerals):
  
  answer = 0
  prev = ""
  for i in numerals:

    answer += letters[i]
    if i == "V" and prev == "I" or i =="X" and prev == "I":
      answer -= letters[prev] * 2
  
      
    prev = i
  return answer

print(roman_to_int("IV"))