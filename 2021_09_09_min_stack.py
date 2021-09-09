# 剑指offer：面试题21：包含min函数的栈
# 题目：
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。
# 在该栈中，调用min、push及pop的时间复杂度都是O（1）。

class MinStack:
    def __init__(self) -> None:
        self._data_stack = []
        self._min_stack = []

    def __len__(self):
        # can method refer to variable outside class
        return len(self._data_stack)

    def min(self):
        return self._min_stack[-1]  # index error if stack is empty

    def push(self, elem):
        if len(self) == 0:
            cur_min = elem
        else:
            cur_min = self._min_stack[-1]
            if elem < cur_min:
                cur_min = elem
        self._min_stack.append(cur_min)
        self._data_stack.append(elem)

    def pop(self):
        self._min_stack.pop()
        return self._data_stack.pop()

    def __repr__(self) -> str:
        return f"{repr(self._data_stack)}{repr(self._min_stack)}"


stack_a = MinStack()
for i in 3, 4, 2, 1:
    stack_a.push(i)


print(stack_a)
stack_a.pop()
stack_a.pop()
print(stack_a)
