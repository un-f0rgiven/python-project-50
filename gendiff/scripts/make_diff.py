#!/usr/bin/env python3

from massives import a, b
from fs import mkdir, mkfile, get_children, is_file, is_directory, get_name, get_meta, flatten, get_type

# {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}},
# 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
# 'group2': {'abc': 12345, 'deep': {'id': 45}}}

tree = mkdir('data', a, {})


def make_tree(node):
    children = get_children(node)
    new_children = []
    level = 0

    for i in flatten(children):
        if type(children[i]) == dict:
            new_children.append(mkdir(i, children[i], {'level': level}))
        else:
            new_children.append(mkfile(i, children[i], {'level': level}))
        level = level + 1
    
    if is_directory(node):
        node['children'] = new_children

    for i in new_children:
        make_tree(i)
    
    return node

tree1 = make_tree(tree)
print(tree1)

def print_tree(node):
    print(get_name(node), get_type(node))
    if is_file(node):
        return
    children = get_children(node)
    list(map(print_tree, children))

# print_tree(tree1)

    

# def gen_diff(data1, data2):
#     keys = data1.keys() | data2.keys()
#     result = {}
#     for key in keys:
#         if key not in data1:
#             result[key] = 'added'
#         elif key not in data2:
#             result[key] = 'deleted'
#         elif data1[key] == data2[key]:
#             result[key] = 'unchanged'
#         else:
#             result[key] = 'changed'
#     return result


# example = ('a', [('b', [('c', []), ('d', [])]), ('e', [('f', [('g', [])])])])
# flat = {}

def make_flat(tree, dictionary, parent=None):
    (node, branches) = tree
    children = []
    dictionary[node] = (parent, children)
    for branch in branches:
        name = make_flat(branch, dictionary, parent=node)
        children.append(name)
    return node
