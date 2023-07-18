# %% [markdown]
# ##### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# %%
def is_two(x):
    # is_two will be our named function which will perform actions down below
    if x % 2 == 0:
        return True
    else:
        return False

# %% [markdown]
# ##### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# 

# %%
def is_vowel(x):
    x.lower()
    # preprocess by lowering all string characters
    if x in ('aeiouAEIOU'):
    # selecting which letters will be 'vowels'
        return True
    else:
        return False

# %% [markdown]
# ##### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# 

# %%
def is_consenant(x):
    x.lower()
    if x != ('a','e','i','o','u') and len(x) > 1:
    # inverse of vowels to get all letters that are not vowels
        return True
    else:
        return False

# %% [markdown]
# ##### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# 

# %%
vowels = ('a','e','i','o','u')
def auto_caps(x):
    y = str(x[0])
    # selecting the first letter of argument to be held within a variable
    if y.lower() not in vowels:
    # checking if first letter in argument is contained within the vowels list
        return x.capitalize()
    # instead of altering the first letter chose the .capitalize() function to do the job
    else:
        return x

auto_caps('bape')

# %% [markdown]
# ##### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# %%
def calculate_tip(tip, bill):
    # two arguments in order to express both the tip and bill
    return (float(tip) * bill)

calculate_tip(.2, 30)

# %% [markdown]
# ##### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# %%
def apply_discount(price, disc):
    after = price * disc
    return after + price
# this one must include price as well as discounted price

apply_discount(40, .10)

# %% [markdown]
# ##### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output

# %%
def handle_commas(x):
    if x.isdigit() == False:
    # filtering any arguments that are not digits
        x = x.replace(',','')
        x = int(x)
        return x
    # problem with this function is it will only break if argument is not a number with a comma


handle_commas('100,33')

# %% [markdown]
# ##### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
# 

# %%
def get_letter_grade(grade):
    # defining grade ranges
    if grade >= 88 and grade <= 100:
        print('A')
    elif grade >= 80 and grade <= 87:
        print('B')
    elif grade >= 67 and grade <= 79:
        print('C')
    elif grade >= 60 and grade <= 66:
        print('D')
    else:
        print('F')
    return

get_letter_grade(80)


# %% [markdown]
# ##### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# %%
def remove_vowels(x):
    vowels = ('a','e','i','o','u')
    result = ''
    for vowel in x:
        if vowel not in vowels:
            result += vowel
    return result

remove_vowels('plant')


# %% [markdown]
# ##### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
# - - Name will become name
# - - First Name will become first_name
# - - % Completed will become completed

# %%
def normalize_name(name):
    # selecting all characters that could be removed, this does not include everything but would be useful for most bodies of text
    removals = [".", "," , "'", '"', "/", "[", "]", "|", "!", "?", "@", "#", "$", "%", "^", "&", "*", "(", ")" ]
    # simple preprocessing to handle white spaces and lowercase texts
    if type(name) == type('str'):
    # defining type in order to filter data types
        for punc in removals:
            name = name.lower().strip()
            name = name.replace(punc, '')
            name = name.replace(' ', '_')
    else:
        print("please provide a string")
    return name

normalize_name('h\'ow i#s t%h *at [ ]')
    

# %% [markdown]
# ##### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# %%
# importing accumulate from itertools in order to easily add list iterations
#from itertools import accumulate

# help(accumulate)

# %%
# numpy cumsum was option 1
# itertools accumulate was option 2
#from itertools import accumulate
#i = 0
#x = []
#def cumulative_sum(x):
#     return list((accumulate(x)))
    
# solved with option 2

#cumulative_sum([1,3,4])



