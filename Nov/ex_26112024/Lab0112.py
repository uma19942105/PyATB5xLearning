from collections import Counter
from pydoc import sort_attributes

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2}

missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)


# Sort a dictionary by its values in descending order
my_dict = {"a": 3, "b": 1, "c": 2}

"""output = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))"""

# sorting dictionary by values in descending order
output = dict(Counter(my_dict).most_common())
print(output)


# {b: 1 , c: 2 , a :3}

