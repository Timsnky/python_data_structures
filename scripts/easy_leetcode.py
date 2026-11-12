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


def remove_duplicates(nums: list[int]) -> int:
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

# nums = [0,0,1,1,1,2,2,3,3,4]
# print (remove_duplicates(nums))
# print (nums)

def remove_element(nums: list[int], var : int) -> int:
    if not nums:
        return 0

    write_index = 0
    for read_index in range(len(nums)):
        if nums[read_index] == var:
            continue
        else:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index

# nums = [0,0,1,1,1,2,2,3,3,4]
# print (remove_element(nums, 1))
# print (nums)


def str_first_occurrence(haystack: str, needle: str) -> int:
    return str.find(haystack, needle)

def str_first_occurrence_2(haystack: str, needle: str) -> int:
    match_index = 0
    needle_index = 0
    for read_index in range(len(haystack)):
        current_haystack_char = haystack[read_index]
        current_needle_char = needle[needle_index]
        if haystack[read_index] == needle[needle_index]:
            if needle_index == 0:
                match_index = read_index
            needle_index += 1
        else:
            match_index = read_index
            needle_index = 0

        if needle_index == len(needle):
            return match_index

    return -1

def str_first_occurrence_3(haystack: str, needle: str) -> int:
    for index in range(len(haystack)):
        if haystack[index] == needle[0]:
            if index + len(needle) <= len(haystack) and haystack[index:index + len(needle)] == needle:
                return index

    return -1

# haystack = "sadbutsad"
# needle = "sad"
# haystack = "leetcode"
# needle = "leeto"

# haystack ="mississippi"
# needle = "issip"
# print(str_first_occurrence_3(haystack, needle))
# print(str_first_occurrence(haystack, needle))

def search_insert(nums: list[int], target: int) -> int:
    for index in range(len(nums)):
        if nums[index] >= target:
            return index

    return len(nums)


def length_of_last_word(s: str) -> int:
    length = 0
    index = len(s) - 1
    while index >= 0:
        if s[index] != ' ':
            length += 1
        else:
            if length != 0:
                return length
        index -= 1
    return length

# s = "Hello World"
# s = "   fly me   to   the moon  "
s = "luffy is still joyboy"
print(length_of_last_word(s))
