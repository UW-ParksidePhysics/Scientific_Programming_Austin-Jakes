import numpy as np

print (f'second lines do no work because the index is out of range \n \t How to fix: instead of square brackets for number= use curly brackets' )

#Working
numbers = {}
numbers[0] = -5
numbers[1] = 10.5

#Not Working
other_numbers = {}
other_numbers[0] = -5
other_numbers[1] = 10.5

code_snippets = {
    'numbers':{'number[0]':-5, 'number[1]':10.5},
    'other_numbers':{'other_numbers[0]':-5, 'other_numbers[1]':10.5}
}

for snip in code_snippets:
    print(code_snippets[snip])