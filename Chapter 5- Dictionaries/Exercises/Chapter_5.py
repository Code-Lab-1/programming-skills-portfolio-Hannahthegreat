# This is the solution to Excercise 1
Hannah = {
    'first_name':"Hannah",'last_name':'Soliao','age':'17','city':'ajman'
    }


# This is the solution to Excercise 2
p_words = {
    'print':'\n\tUsed for displaying an output',
    'input':'\n\tUsed to get input from user',
    'variable':'\n\tSymbolic name to reference an object',
    'if statements': '\n\tWritten with if, elif, and else clauses. Used to make conditions',
    'dictionaries':'\n\tUsed to store key/value pairs'
    }
print("Print: ",p_words.get('print'))
print("Input: ",p_words.get('input'))
print("Variable: ",p_words.get('variable'))
print("If statements: ",p_words.get('if statements'))
print("Dictionaries: ",p_words.get('dictionaries'))

# This is the solution to Excercise 3
p_words = {
    'Print:':'\n\tUsed for displaying an output',
    'Input:':'\n\tUsed to get input from user',
    'Variable:':'\n\tSymbolic name to reference an object',
    'If statements:': '\n\tWritten with if, elif, and else clauses. Used to make conditions',
    'Dictionaries:':'\n\tUsed to store key/value pairs',
    'Program:':'\n\tset of instructions that a computer uses to perform a specific action.',
    'List:':'\n\tis a data type that can store a collection of values.',
    'Fucntion:':'\n\tis a reusable block of code that performs a certain action (or actions).',
    'For loop/While loop:':' \n\texecute the same code for every element of a collection',
    'Intrepreter:':'\n\tto read and execute the source code'
    }

for key,value in p_words.items():
    print(key, value)

# This is the solution to Excercise 4
river = {
    'Amazon':'South America',
    'Yangtze':'China',
    'Congo':'Africa'
    }

for key,value in river.items():
    print(key, "river runs through", value)

# This is the solution to Excercise 5
rollo = {
    'pet':'cat','owner':'dana'
}

mahal = {
    'pet':'cat', 'owner':'faith'
}

doge = {
    'pet':'dog','owner':'hannah'
}

pets = [rollo,mahal,doge]

for variable in pets:
    for key,value in variable.items():
        print(key,value)