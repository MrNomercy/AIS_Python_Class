##author: ricky
##date: 2 oct 2018
##description: 7.103 problem 2
##An = n^2 or An = n/3
##date modified: 2 oct 2018

# input to get user data
num_input = int(input("Please enter a number of n: "))

# create a function call seq_gen()
def seq_gen(times):
    for n in range(times):
        if n%3 != 0:
            An = n**2
            print(An)
        elif n%3 == 0:
            An = n/3
            print(int(An))

# using the function
result = seq_gen(num_input)













