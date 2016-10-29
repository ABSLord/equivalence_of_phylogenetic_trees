from phylogenetic_trees import is_equals_phylogenetic_trees


def test():
    print(is_equals_phylogenetic_trees("tree1.txt", "tree2.txt"))
    print(is_equals_phylogenetic_trees("tree3.txt", "tree4.txt"))


test()