a = {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22", "follow": False}
b = {"timeout": 20, "verbose": True, "host": "hexlet.io"}

def generate_diff(file1, file2):
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    # print(keys1, keys2) # ['host', 'timeout', 'proxy', 'follow'] ['timeout', 'verbose', 'host']
    diff_set = set(keys1) & set(keys2)
    set1 = set(keys1) - set(keys2)
    set2 = set(keys2) - set(keys1)
    # print(diff_set, set1, set2) # {'timeout', 'host'} {'follow', 'proxy'} {'verbose'}
    _f_lst = []
    for i in diff_set:
        if a[i] == b[i]:
            _f_lst.append([0, i, a[i]])
        if a[i] != b[i]:
            _f_lst.append([1, i, a[i]])
            _f_lst.append([2, i, b[i]])
    for i in set1:
        _f_lst.append([1, i, a[i]])
    for i in set2:
        _f_lst.append([2, i, b[i]])
    # print(_f_lst)   # [[0, 'host', 'hexlet.io'], [1, 'timeout', 50], [2, 'timeout', 20], 
                    # [1, 'follow', False], [1, 'proxy', '123.234.53.22'], [2, 'verbose', True]]
    _s_lst = sorted(_f_lst, key=lambda x: (x[1]))     # [[1, 'follow', False], [0, 'host', 'hexlet.io'], 
                                                    # [1, 'proxy', '123.234.53.22'], [1, 'timeout', 50], 
                                                    # [2, 'timeout', 20], [2, 'verbose', True]]
    result = ''
    for s, k, v in _s_lst:
        if s == 0:
            s = ''
        if s == 1:
            s = '-'
        if s == 2:
            s = '+'
        result = result + s + ' ' + k + ' ' + str(v) + '\n'

    print(f'{{\n{result}}}')



generate_diff(a, b)