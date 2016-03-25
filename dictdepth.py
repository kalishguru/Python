dictval = {"key 1": 1,"key 2":{ "key 3": 1, "key 4": {  "key 5": 4 }}}

def recursion_depth(dict_, depth):
    for k in dict_:
        print "{0} = depth:{2}".format(k, dict_[k], depth)
    if type(dict_[k]) == dict:
        actual_depth = recursion_depth(dict_[k], depth+1)
        if actual_depth > depth: depth += 1
    return depth

print(recursion_depth(dictval,1))
