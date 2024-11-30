def iterate_nested_dict(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            iterate_nested_dict(value)
        else:
            print(f&quot;Key: {key}, Value: {value}&quot;)

nested_dict = {'outer_key': {'inner_key1': 'value1', 'inner_key2': 'value2'}}
iterate_nested_dict(nested_dict)

'''Loop Through a Nested Dictionary Using Recursion
In this example, below Python code defines a recursive function, `iterate_nested_dict`,
to iterate through a nested dictionary, printing each key-value pair. It handles nested 
structures by recursively calling itself when encountering inner dictionaries, providing 
a clear and flexible approach for nested dictionary traversalKey: inner_key1, Value: value1
Key: inner_key2, Value: value2.'''
