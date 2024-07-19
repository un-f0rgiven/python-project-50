#!/usr/bin/env python3

from gendiff.scripts.parsing import fix_file


def convert_numbers(coll):
    if coll[0] == 0:
        coll[0] = ' '
    if coll[0] == 1:
        coll[0] = '-'
    if coll[0] == 2:
        coll[0] = '+'
    return coll


def generate_diff(filepath1, filepath2):
    file1 = fix_file(filepath1)
    file2 = fix_file(filepath2)
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    # print(keys1, keys2)
    # ['host', 'timeout', 'proxy', 'follow'] ['timeout', 'verbose', 'host']
    diff_set = set(keys1) & set(keys2)
    set1 = set(keys1) - set(keys2)
    set2 = set(keys2) - set(keys1)
    # print(diff_set, set1, set2)
    # {'timeout', 'host'} {'follow', 'proxy'} {'verbose'}
    _f_lst = []
    for i in diff_set:
        if file1[i] == file2[i]:
            _f_lst.append([0, i, file1[i]])
        else:
            _f_lst.append([1, i, file1[i]])
            _f_lst.append([2, i, file2[i]])
    for i in set1:
        _f_lst.append([1, i, file1[i]])
    for i in set2:
        _f_lst.append([2, i, file2[i]])
    # print(_f_lst)
    # [[0, 'host', 'hexlet.io'], [1, 'timeout', 50], [2, 'timeout', 20],
    # [1, 'follow', False], [1, 'proxy', '123.234.53.22'], [2, 'verbose', True]]
    _s_lst = sorted(_f_lst, key=lambda x: (x[1]))
    # [[1, 'follow', False], [0, 'host', 'hexlet.io'],
    # [1, 'proxy', '123.234.53.22'], [1, 'timeout', 50],
    # [2, 'timeout', 20], [2, 'verbose', True]]

    _t_lst = list(map(convert_numbers, _s_lst))

    result = ''
    for s, k, v in _t_lst:
        result = result + s + ' ' + k + ': ' + str(v).lower() + '\n'

    return f'{{\n{result}}}'
