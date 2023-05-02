
#    1) Countdown - Create a function that accepts a number as an input. Return a new list that 
#     counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#         Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(start):
    result = []
    for x in range(start, -1, -1):
        result.append(x)
    return result

print(countdown(5))
print("expected", [5,4,3,2,1,0])

#    2) Print and Return - Create a function that will receive a list with two numbers. Print 
#     the first value and return the second.
#         Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(nums):
    print(nums[0])
    return nums[1]
print(print_and_return([1,2]))
print("expected", "1, 2")


#    3) First Plus Length - Create a function that accepts a list and returns the sum of the 
#     first value in the list plus the list's length

def first_plus_length(nums):
    result = nums[0] + len(nums)
    return result
print(first_plus_length([6,1,2,3]))
print("expected", 10)


#    4) Values Greater than Second - Write a function that accepts a list and creates a new list 
#     containing only the values from the original list that are greater than its 2nd value. 
#     Print how many values this is and then return the new list. If the list has less than 2
#     elements, have the function return False
#         Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#         Example: values_greater_than_second([3]) should return False

def greater_than_second(nums):
    new_list = []
    greater_than = 0
    for x in range(0, len(nums)):
        if len(nums) < 2:
            return False
        if nums[x] > nums[1]:
            new_list.append(nums[x])
            greater_than += 1
    print(greater_than)
    return new_list

print(greater_than_second([5,2,3,2,1,4]))        
print("expected", 3,",", [5,3,4])
print(greater_than_second([3])) 
print("expected False")



#    5) This Length, That Value - Write a function that accepts two integers as parameters: size 
#     and value. The function should create and return a list whose length is equal to the
#     given size, and whose values are all the given value.
#         Example: length_and_value(4,7) should return [7,7,7,7]
#         Example: length_and_value(6,2) should return [2,2,2,2,2,2]


def this_len_that_val(int1, int2):
    result = []
    i = int1
    while i > 0:
        result.append(int2)
        i -= 1
    return result
print(this_len_that_val(4,7))
print("expected", [7,7,7,7])
print(this_len_that_val(6,2))
print("expected", [2,2,2,2,2,2])


