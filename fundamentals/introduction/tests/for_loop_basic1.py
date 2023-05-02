
# 1) Basic - Print all integers from 0 to 150.
# 2) Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# 3) Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" 
#   instead. If divisible by 10, print "Coding Dojo".
# 4) Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# 5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
# 6) Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and 
#   going through highNum, print only the integers that are a multiple of mult. For example, if 
#   lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
# -----------------------------------------------------------------------------------------


# 1)
for x in range(151):
    print(x)


# 2)
for x in range(5, 1001, 5):
    print(x)


# 3)
for x in range (1,101):
    if x % 10 == 0: 
        x = "Coding Dojo"
        print(x)
    elif x % 5 == 0:
        x = "Coding"
        print(x)
    else:
        print(x)


# 4)
sum = 0
for x in range(1,500001,2):
        sum += x
print(sum)


# 5)
for x in range(2018, -1, -4):
    print(x)


# 6)
low_num = 2
high_num = 9
mult = 3
for x in range(low_num, high_num+1):
    if x % mult == 0:
        print(x)