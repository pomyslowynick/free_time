import collections
import functools
import json
import itertools

def tree():
    return collections.defaultdict(tree)

def fahrenheit(user_input_Celsius):
    fahr = user_input_Celsius * 9/5 +32
    return fahr

#some_tree = tree()
#tree_values = some_tree["100"] ['7878232']["Even numbers < 89"] = ["78", "65", "54"]
#print(json.dumps(some_tree, indent=4))

print list(itertools.compress(range(10,100), [0,1,0,1,0,0,0,1,0,1,0]))

items = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("b", 2)]
