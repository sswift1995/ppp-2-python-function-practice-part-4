#Python function called max_num() to find 3 max numbers
def max_num(x,y,z):
    return([x,y,z])
print(max_num(3,4,5))
print(max_num(5,10,15))
print(max_num(10,20,30))
#Python function called mult_list() to multiply all numbers in list
def mult_list(list):
    #if statement for empty list returning 0
    if len(list) == 0:
        return 0
    # Product starts with the first element
    prod = list[0]

# Grouping the elements to multiply together
    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i

    return prod
#printing the functions answers
print(mult_list([3,4,5]))
print(mult_list([]))
print(mult_list([32]))

#Python function called rev_string()
def rev_string(my_string):
     #to reverse the characters in the string.
    return my_string[::-1]
print (rev_string(""))
print(rev_string("parrot"))
print(rev_string("my string"))

#Python function called num_within()
def num_within(r,s,t):

    #return statement as true or false
    return r in range(s,t+1)

#prints true or false
print(num_within(3,2,4))
print(num_within(2,3,4))
print(num_within(15,16,12))

