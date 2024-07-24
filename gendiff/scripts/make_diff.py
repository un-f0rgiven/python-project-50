#!/usr/bin/env python3

from massives import a, b
from fs import mkdir, mkfile, get_children, is_file, is_directory, get_name, get_meta, flatten

# def new_tree(coll):
#     keys = flatten(coll)
#     for i in keys:
#         if type(coll[i]) == dict:
#             mkdir(i, coll[i])
#             children = get_children(coll)
#             list(map(new_tree, children))   
#         else:
#             mkfile(i)


def make_tree(node):
    tree = mkdir('data', node, 'general')
    children = get_children(tree)
    keys = flatten(children)
    for i in keys:
        if type(children[i]) == dict:
            mkdir(i, children[i])
            # children = get_children(children)
            # list(map(new_tree, children))   
        else:
            mkfile(i)
    return tree
    

def print_tree(node):
    # print(get_name(node))
    # if is_file(node):
    #     return
    children = get_children(node)
    print(children)
    # list(map(print_tree, children))


tree1 = make_tree(a)
tree2 = make_tree(b)
# print(tree1)
# print_tree(tree1)
# print(get_name(tree1))
# children = (get_children(tree1))
# print(children['common'])




def make_diff(m1, m2):
    tree = {}
    keys1 = list(m1.keys())
    keys2 = list(m2.keys())
    general_set = set(keys1) & set(keys2)
    set1 = set(keys1) - set(keys2)
    set2 = set(keys2) - set(keys1)

    for i in general_set:
        if is_directory(m1[i]) is True:
            tree[i] = mkdir(i, m1[i], 'unchanged')
        else:
            tree[i] = mkfile(i, 'unchanged')
    
    for i in set1:
        if is_directory(m1[i]) is True:
            tree[i] = mkdir(i, m1[i], 'deleted')
        else:
            tree[i] = mkfile(i, 'deleted')

    for i in set2:
        if is_directory(m2[i]) is True:
            tree[i] = mkdir(i, m2[i], 'added')
        else:
            tree[i] = mkfile(i, 'added')

    return f'keys1 - {keys1}, keys2 - {keys2}, general_set - {general_set}, set1 - {set1}, set2 - {set2}'
    return tree


# print(make_diff(tree1, tree2))

def gen_diff(data1, data2):
    keys = data1.keys() | data2.keys()
    result = {}
    for key in keys:
        if key not in data1:
            result[key] = 'added'
        elif key not in data2:
            result[key] = 'deleted'
        elif data1[key] == data2[key]:
            result[key] = 'unchanged'
        else:
            result[key] = 'changed'
    return result

def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:

            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)

    return result

def convert(coll):
    result = {}
    
    def walk(subcoll):
        for i in subcoll:
            if isinstance(i, tuple):
                walk(i)
            result.update({i[0]: i[1]})
    walk(coll)

    return result

a = [('key', [('key2', 'anotherValue')]), ('key2', 'value2')]
# ('key', [('key2', 'anotherValue')]) - <class 'tuple'>
# key - <class 'str'>
# [('key2', 'anotherValue')] - <class 'list'>
# ('key2', 'value2') - <class 'tuple'>
# key2 - <class 'str'>
# value2 - <class 'str'>

for i in a:
    keys = []
    values = []
    for i in a:
        keys.append(i[0])
        values.append(i[1])
print(keys, values)


# print(convert(a))
