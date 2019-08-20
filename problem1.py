##Author: ricky
##date: 2 oct 2018
##description: 7.103 problem 1
##count the words, spaces and vowels in a sentence
##date modified: 2 oct 2018


# input to get user sentence
sentence_input = input("Please enter a sentence: ")

# split sentence into words
my_list = sentence_input.split(" ")

# count words in the sentence
num_word = len(my_list)
print("The number of words in this sentence is:",num_word)

# count spaces in the sentence
num_space = int(num_word)-1
print("The number of spaces in this sentence is:",num_space)

# count vowels in the sentence
count_a = sentence_input.lower().count("a")
count_e = sentence_input.lower().count("e")
count_i = sentence_input.lower().count("i")
count_o = sentence_input.lower().count("o")
count_u = sentence_input.lower().count("u")
count_vowel = count_a + count_e + count_i +count_o + count_u
print("The number of vowels in this sentence is:",count_vowel)


