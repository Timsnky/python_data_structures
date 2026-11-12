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
# s = "luffy is still joyboy"
# print(length_of_last_word(s))


def plus_one(digits: list[int]) -> list[int]:
    start_string = ''
    for num in digits:
        start_string += str(num)

    value_string = str(int(start_string) + 1)
    new_list = []
    for char in value_string:
        new_list.append(int(char))

    return new_list

# digits = [1,2,3]
# digits = [9]
# print(plus_one(digits))
def add_binary_2(a : str, b : str) -> str:
    return str(bin(int(a, 2) + int(b, 2)))[2:]


def add_binary(a : str, b : str) -> str:
    a_value = 0
    for index in range(len(a) - 1, -1, -1):
        a_value += (int(a[index]) * (2 ** (len(a) - 1 - index)))

    b_value = 0
    for index in range(len(b) - 1, -1, -1):
        b_value += (int(b[index]) * (2 ** (len(b) - 1 - index)))

    final_value = a_value + b_value
    if final_value == 0:
        return '0'

    final_value_str = ''
    while final_value > 0:
        final_value_str += str(final_value % 2)
        final_value = final_value // 2

    return final_value_str[::-1]



# a = "11"
# b = "1"
# print(add_binary_2(a, b))

def detect_capital_use(word: str) -> bool:
    return str.upper(word) == word or str.lower(word) == word or (str.upper(word[0]) == word[0] and str.lower(word[1:]) == word[1:])

def detect_capital_use_2(word: str) -> bool:
    return word.isupper() or word.islower() or word == word.capitalize()

def reverse_words(self, s: str) -> str:
    return ' '.join(word[::-1] for word in s.split(' '))


def matrix_reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    if (len(mat) * len(mat[0])) != (r * c):
        return mat

    new_mat = [[]]
    r_index = 0
    for m_list in mat:
        for n_item in m_list:
            if len(new_mat[r_index]) < c:
                new_mat[r_index].append(n_item)
            else:
                new_mat.append([n_item])
                r_index += 1

    return new_mat

# mat = [[1,2],[3,4]]
# r = 1
# c = 4
# mat = [[1,2],[3,4]]
# r = 4
# c = 1
# print(matrix_reshape(mat, r, c))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def populate_tree(tree_list : list[int]) -> TreeNode | None:
    tree = None
    for item in tree_list:
        if not tree:
            tree = TreeNode(item)
            continue

        if not tree.left:
            tree.left = TreeNode(item)
            continue

        if not tree.right:
            tree.right = TreeNode(item)
            continue






def is_subtree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    if not root or not sub_root:
        return False

    current_root = root
    while current_root:
        if current_root.val != sub_root.val:
            return False

        return is_subtree(current_root.left, sub_root.left) and is_subtree(current_root.right, sub_root.right)

    return True

root = [3, 4, 5, 1, 2]
subRoot = [4, 1, 2]


