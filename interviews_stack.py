
class Stack:

    def __init__(self, input_list: list):
        self.input_list = input_list

    def is_empty(self):
        return len(self.input_list) == 0

    def push(self, element):
        self.input_list.append(element)

    def pop(self):
        return self.input_list.pop()

    def peek(self):
        return self.input_list[-1]

    def size(self):
        return len(self.input_list)


if __name__ == "__main__":
    balanced_samples = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
    unbalanced_samples = ['}{}', '{{[(])]}}', '[[{())}]']

    bracket_str = unbalanced_samples[2]  # insert here the list index you want to check
    bracket_lst = list(bracket_str)
    stack_inst = Stack(bracket_lst)

    if stack_inst.is_empty() is False and stack_inst.size() % 2 == 0:
        stack_inst_bool = Stack([])
        for _ in range(stack_inst.size() - 1):
            cut_off_elem = stack_inst.pop()
            result = cut_off_elem == stack_inst.peek()
            stack_inst_bool.push(result)

        result_lst = stack_inst_bool.__dict__['input_list']
        chunk = stack_inst_bool.size() // 2

        try:
            assert (result_lst[chunk+1:] == result_lst[:chunk][::-1])
            print('The list is balanced')
        except AssertionError:
            print('The list is NOT balanced')
    else:
        print('The list is NOT balanced')

