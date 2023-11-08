
letters = {
  1000 : "M",
  900 : "CM",
  500 : "D",
  100 : "C",
  90 : "XC",
  50 : "L",
  40 : "XL",
  10 : "X",
  9 : "IX",
  5 : "V",
  4 : "IV",
  1 : "I"

}


# only works with numbers 10 or lower, add more if you want


#original version WORKING
# def roman(num):
#   x = ""
#   if num == 0:
#      return ""
  
#   if num >= 10:
#     num -= 10
#     return letters[10] + roman(num)
#   if num == 9:
#       num -= 9
#       return letters[9] + roman(num)
#   elif num >= 5:
#       num -= 5
#       return letters[5] + roman(num)
#   elif num == 4:
#       num -= 4
#       return letters[4] + roman(num)
#   elif num >= 1:
#       num -= 1
#       return letters[1] + roman(num)



# better code, now supports numbers up to 40
def roman(num):
  if num <= 0:
    return ""
  if num == 1:
    return letters[1]
  for i in list(letters):
    if num >= i:
      num -= i
      
      return letters[i] + str(roman(num))




print(roman(999))