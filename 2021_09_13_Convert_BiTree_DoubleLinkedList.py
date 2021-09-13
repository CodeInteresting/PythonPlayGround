# 剑指offer：
# 面试题27： 二叉搜索树与双向链表
# 输入一颗二叉搜索树，将该二叉搜索树转换成一个排序的
# 双向链表

class BiTreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def make_tree():
    node1 = BiTreeNode(10)
    node2 = BiTreeNode(6)
    node3 = BiTreeNode(14)
    node4 = BiTreeNode(4)
    node5 = BiTreeNode(8)
    node6 = BiTreeNode(12)
    node7 = BiTreeNode(16)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    return node1


def print_link_list(tree_list_head):
    p = tree_list_head
    while p:
        print(p.value)
        p = p.right


def convert_tree_to_list(biTree):
    # not accepting empty node
    #  return (first_node, last_node)
    if biTree.left is None:
        first_node = biTree

    if biTree.right is None:
        last_node = biTree

    if biTree.left is not None:
        first, last = convert_tree_to_list(biTree.left)
        first_node = first
        last.right = biTree
        biTree.left = last

    if biTree.right is not None:
        first, last = convert_tree_to_list(biTree.right)
        last_node = last
        first.left = biTree
        biTree.right = first

    return first_node, last_node


tree = make_tree()
head, tail = convert_tree_to_list(tree)
print_link_list(head)