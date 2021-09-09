class ComplexNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.sibling = None


def make_link_list():
    node_A = ComplexNode("A")
    node_B = ComplexNode("B")
    node_C = ComplexNode("C")
    node_D = ComplexNode("D")
    node_E = ComplexNode("E")
    node_A.next = node_B
    node_B.next = node_C
    node_C.next = node_D
    node_D.next = node_E
    node_A.sibling = node_C
    node_B.sibling = node_E
    node_D.sibling = node_B

    return node_A


def clone_list(old_list):
    pairs = {}  # tracking old_node, new_node pairs
    p_old = old_list
    p_new = dummy_head = ComplexNode(0)  # dummy head
    while p_old:
        p_new.next = ComplexNode(p_old.value)
        pairs[p_old] = p_new.next
        p_new = p_new.next

    p_old = old_list
    while p_old:
        if p_old.sibling:
            pairs[p_old].sibling = pairs[p_old.sibling]

    return dummy_head.next

