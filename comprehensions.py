# Comprehensions - concise syntax for describing lists, sets or dictionary
words = 'Hello World, hello people'.split()
# ['Hello', 'World,', 'hello', 'people']

# LIST
# [ expr(item) for item in iterable ]
l = [len(word) for word in words]
# [5, 6, 5, 6]

l = []
for item in words:              # <-- long-hand
    l.append(len(item))


# SET (syntax same as list, but in curly brackets)
s = {len(word) for word in words}
# {5, 6}


# DICTIONARY
# { key_expr:value_expr for item in iterable }
d = {k: v for k, v in enumerate(words)}
# {0: 'Hello', 1: 'World,', 2: 'hello', 3: 'people'}
d_reverse_kv = {v: k for k, v in d.items()}
# {'Hello': 0, 'World,': 1, 'hello': 2, 'people': 3}


# NO TUPLE COMPREHENSION !!! (parentheses already taken for.. generator expressions)
tuple(i for i in (1, 2, 3))
# (1, 2, 3)


# COMPREHENSION + FILTER
# [expr(item) for item in iterable if predicate(item)]
res = [len(word) for word in words if len(word)%2 == 0]     # store only even nums
# [6, 6]


# GENERATOR (!!! differs by round brackets)
# (expr(item) for item in iterable)
million_squares_array_now = [x*x for x in range(1000000)]

million_squares_generator = (x*x for x in range(1000000))   # <-- notice the ROUND brackets
my_list = list(million_squares_generator)                   # <-- consume


# EXERCISE
l0 = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
l0 = [[i for i in range(10, 41, 10)], [i for i in range(50, 81, 10)], [i for i in range(90, 121, 10)]]
l0 = [[i for i in range(10 + s*40, 41 + s*40, 10)] for s in range(0, 3, 1)]

flat_list = [item for sublist in l0 for item in sublist]
# equivalent to:
flat_list = []
for sublist in l0:
    for item in sublist:
        flat_list.append(item)
