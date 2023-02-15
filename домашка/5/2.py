myStr = "utig85u7g6u56g76g5g8"
maxIn = 0
maxChar = ''
for char in myStr:
    if(myStr.count(char) > maxIn):
        maxIn = myStr.count(char)
        maxChar = char
print(maxChar, maxIn)

