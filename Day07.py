# AOC17 day 07
from collections import Counter


def make_tree(data):
    tree = {}
    for line in data.split("\n"):
        words = line.split()
        children = list(map(lambda x: x.replace(",", ""), words[3:]))
        tree[words[0]] = {"weight": int(words[1][1:-1]), "children": children}
    return tree


def get_bottom_node(tree):
    all_names = []
    for node in tree.keys():
        all_names.append(node)
    for properties in tree.values():
        for child in properties["children"]:
            all_names.remove(child)
    return all_names[0]


def check_balance(bottom, tree):
    if "total" not in tree[bottom]:
        if len(tree[bottom]["children"]) == 0:
            tree[bottom]["weights"] = []
            tree[bottom]["total"] = tree[bottom]["weight"]
            tree[bottom]["balanced"] = True
        else:
            tree[bottom]["weights"] = list(map(lambda x: check_balance(x, tree), tree[bottom]["children"]))
            tree[bottom]["total"] = tree[bottom]["weight"] + sum(tree[bottom]["weights"])
            tree[bottom]["balanced"] = all(x == tree[bottom]["weights"][0] for x in tree[bottom]["weights"])

    return tree[bottom]["total"]


def balance_weight(tree):
    unbalanced = []
    for node in tree.keys():
        if not tree[node]["balanced"]:
            unbalanced.append(node)
    unbalanced.sort(key=lambda x: tree[x]["total"])
    count = Counter(tree[unbalanced[0]]["weights"])
    weight_change = count.most_common()[0][0] - count.most_common()[1][0]
    child_index = tree[unbalanced[0]]["weights"].index(count.most_common()[1][0])
    child_name = tree[unbalanced[0]]["children"][child_index]
    return tree[child_name]["weight"] + weight_change


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day07.txt")
    tree = make_tree(data)
    bottom = get_bottom_node(tree)
    print(f"The bottom node is {bottom}")
    check_balance(bottom, tree)
    print(f"The unbalanced node would have to be {balance_weight(tree)}")
