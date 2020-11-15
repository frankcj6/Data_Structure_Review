class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


# implementation


s = Stack()
print(s.is_empty())
s.push('A')
s.push('B')
s.push('C')
print(s.get_stack())
s.pop()
print(s.get_stack())
s.push('D')
print(s.get_stack())
print(s.peek())


# problem solving (balance parenthesis)
# check if balanced use of parenthesis

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '{' and p2 == '}':
        return True
    if p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_balanced_paren(paren_string):
    paren = Stack()
    is_balance = True
    index = 0
    while index < len(paren_string) and is_balance:
        i = paren_string[index]
        if i in '({[':
            paren.push(i)
        else:
            if paren.is_empty():
                is_balance = False
            else:
                top = paren.pop()
                if not is_match(top, i):
                    is_balance = False
        index += 1

    if paren.is_empty() and is_balance:
        return True
    else:
        return False

print(is_balanced_paren('(())'))
print(is_balanced_paren('([]'))
print(is_balanced_paren('(('))

#  convert integer into binary


def div_by_2(deci):
    num = Stack()

    while deci > 0:
        remainder = deci % 2
        num.push(remainder)
        deci = deci // 2

    result = ''
    while not num.is_empty():
        result += str(num.pop())

    return result


print(div_by_2(301))


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ''
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str


stack1 = Stack()
input_str1 = 'Hello'
print(reverse_string(stack1, input_str1))

