def reverse_parentheses(s):
    stack = ['']

    for char in s:
        if char == '(':
            stack.append('')
        elif char == ')':
            temp_char = stack.pop()
            stack[-1] += temp_char[::-1]
        else:
            stack[-1] += char

    return stack[0]

# s = "(u(l(vo)e)i)"
# print(reverse_parentheses(s))

def longest_common_prefix(strings):
    prefix = ''
    if len(strings) == 0:
        return prefix

    first_str = strings[0]
    for index in range(len(first_str)):
        for str_index in range(1, len(strings)):
            if index > len(strings[str_index]) - 1 or strings[str_index][index] != first_str[index]:
                return prefix
        prefix += first_str[index]

    return prefix

# strs = ["flower","flow","flowering"]
# print(longest_common_prefix(strs))

def is_valid_brackets_string(s):
    stack = []
    valid_brackets_map = {")": "(", "}" : "{", "]" : "["}
    for char in s:
        if char in valid_brackets_map.values():
            stack.append(char)
        else:
            if stack and stack[-1] == valid_brackets_map.get(char, ''):
                stack.pop()
            else:
                return False

    return len(stack) == 0

#s = "(){}}{"
#s = "([])"
#print(is_valid_brackets_string(s))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_item = None):
        self.val = val
        self.next = next_item

def merge_two_lists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    head = ListNode()
    dummy = head

    while list1 is not None or list2 is not None:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        elif list2.val < list1.val:
            head.next = list2
            list2 = list2.next
        head = head.next

    if list1 is None:
        head.next = list2
    elif list2 is None:
        head.next = list1

    return dummy.next


def remove_duplicates_2(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0

    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] == nums[read_index - 1]:
            continue
        else:
            nums[write_index] = nums[read_index]
            write_index += 1

    for blank_index in range(write_index, len(nums)):
        nums[blank_index] = '_'

    return write_index

nums = [0,0,1,1,1,2,2,3,3,4]
print (remove_duplicates_2(nums))
print (nums)



