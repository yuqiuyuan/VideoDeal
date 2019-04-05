str = raw_input()
n = input()
if n > len(str) or n < 0:
    print -1
else:
    s = ''
    for i in range(0,len(str)-n+1,1):
        s = s + str[i:i+n] + ' '
    print s[0:len(s)-1]