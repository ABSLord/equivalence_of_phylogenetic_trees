def is_equals_phylogenetic_trees(file_name1, file_name2):
    f1 = open(file_name1)
    f2 = open(file_name2)
    tree1 = dict()
    tree2 = dict()
    for line in f1:
        lst = line.split()
        tree1[lst[0]] = [lst[2], lst[3]]
    for line in f2:
        lst = line.split()
        tree2[lst[0]] = [lst[2], lst[3]]
    f1.close()
    f2.close()
    units1 = marked_units(tree1)
    units2 = marked_units(tree2)
    if units1 != units2:
        return False
    for i in range(0, len(units1) - 1):
        for j in range(i + 1, len(units1)):
            if inverse_level_of_general_ancestor(units1[i], units1[j], tree1) != inverse_level_of_general_ancestor(units2[i], units2[j], tree2):
                return False
    return True


def level_up(obj, dct):
    for key in dct:
        if obj in dct[key]:
            return key


def inverse_level_of_general_ancestor(obj1, obj2, dct):
    count = 0
    val1 = obj1
    val2 = obj2
    while val1 != val2:
        val1 = level_up(val1, dct)
        val2 = level_up(val2, dct)
        count += 1
    return count


def marked_units(dct):
    res = list()
    for key in dct:
        if (dct[key][0] not in dct) and (dct[key][1] not in dct):
            res.append(dct[key][0])
            res.append(dct[key][1])
    res.sort()
    return res
