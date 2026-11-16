from pip._internal.utils import retry


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(node_list: list) -> ListNode | None:
    if not node_list:
        return None

    head = ListNode(node_list[0])
    current_head = head
    for index in range(1, len(node_list)):
        new_node = ListNode(node_list[index])
        current_head.next = new_node
        current_head = new_node

    return head

def traverse_linked_list(linked_list: ListNode | None):
    current_head = linked_list
    while current_head is not None:
        print(current_head.val)
        current_head = current_head.next

def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    if l1 is None and l2 is None:
        return None

    if l1 is None:
        return l2

    if l2 is None:
        return l1

    l3 = None
    current_sum_node = l3
    carry = 0
    while l1 is not None or l2 is not None:
        l1_value = l2_value = 0
        if l1 is not None:
            l1_value = l1.val
            l1 = l1.next

        if l2 is not None:
            l2_value = l2.val
            l2 = l2.next

        sum_value = l1_value + l2_value + carry
        carry = 0
        if sum_value > 9:
            carry = sum_value // 10
            sum_value = sum_value - 10

        new_node = ListNode(sum_value)
        if current_sum_node is None:
            current_sum_node = new_node
        else:
            current_sum_node.next = new_node
            current_sum_node = current_sum_node.next

        if l3 is None:
            l3 = new_node

    if carry != 0:
        current_sum_node.next = ListNode(carry)

    return l3

# # l1 = [2,4,3]
# l1 = [9,9,9,9,9,9,9]
# l1_linked_list = build_linked_list(l1)
# # l2 = [5,6,4]
# l2 = [9,9,9,9]
# l2_linked_list = build_linked_list(l2)
# l3_linked_list = add_two_numbers(l2_linked_list, l1_linked_list)
# traverse_linked_list(l3_linked_list)

def length_of_longest_substring(s: str):
    longest_substr = ""
    current_substr = ""
    for char in s:
        existing_index = current_substr.rfind(char)
        if existing_index != -1:
            if existing_index + 1 < len(current_substr):
                current_substr = current_substr[existing_index + 1:]
            else:
                current_substr = ""

        current_substr += char

        if len(current_substr) > len(longest_substr):
            longest_substr = current_substr

    return len(longest_substr)


def length_of_longest_substring_2(s: str):
    last_seen: dict[str, int] = {}
    left = 0
    longest = 0

    for right, char in enumerate(s):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)

        last_seen[char] = right
        longest = max(longest, right - left + 1)

    return longest

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "1R1T7"
# print(length_of_longest_substring(s))


def longest_palindrome(s: str) -> str:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    longest_pal = ""
    for index in range(len(s)):
        main_str = s[index:]
        for reverse_index in range(len(main_str), -1, -1):
            current_str = main_str[:reverse_index]

            if is_palindrome(current_str) and len(current_str) > len(longest_pal):
                longest_pal = current_str

    return longest_pal


def longest_palindrome_2(s: str) -> str:
    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0  and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right

    best_start = 0
    best_end = 0

    for index in range(len(s)):
        start, end = expand(index, index)
        if end - start > best_end - best_start:
            best_start, best_end = start, end

        start, end = expand(index, index + 1)
        if end - start > best_end - best_start:
            best_start, best_end = start, end

    return s[best_start:best_end]

# s = "babad"
# s = "cbbd"
# s = "a"
# print(longest_palindrome(s))


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    s_nested_list = ["" for _ in range(num_rows)]
    row_index = 0
    direction = 1

    for char in s:
        s_nested_list[row_index] += char

        if row_index == 0:
            direction = 1
        elif row_index == num_rows - 1:
            direction = -1

        row_index += direction

    return ''.join(s_nested_list)

# s = "PAYPALISHIRING"
# num_rows = 3
# print(convert(s, num_rows))


def reverse_integer(x: int) -> int:
    is_negative = x < 0
    reversed_x = str(abs(x))[::-1]
    if is_negative:
        reversed_x = "-" + reversed_x

    return int(reversed_x)


def reverse_integer_2(x: int) -> int:
    is_negative = x < 0
    x = -abs(x)
    result = 0
    last_digit_limit = -8 if is_negative else -7

    while x != 0:
        last_digit = x % -10
        x = (x - last_digit) // 10

        if result < -214748364:
            return 0

        if result == -214748364 and last_digit < last_digit_limit:
            return 0

        result = result * 10 + last_digit

    return result if is_negative else -result

# x = -123
# x = -2147483648
# print(reverse_integer_2(x))

def my_atoi(s: str) -> int:
    is_negative = False
    result = None
    for char in s:
        if char == " ":
            if result is not None:
                break
            continue

        if char == "-" or char == "+":
            if result is not None:
                break
            is_negative = char == "-"
            result = 0
            continue

        char_ord = ord(char)
        if char_ord < 48 or char_ord > 57:
            break

        int_value = char_ord - 48
        if result is None:
            result = 0
        result = result * 10  + int_value

        if is_negative and -result <= -2 ** 31:
            return -2 ** 31
        elif not is_negative and result >= (2 ** 31) - 1:
            return (2 ** 31) - 1

    if result is None:
        result = 0

    if is_negative:
        result = -result

    return result

# s = "42"
# s = " -042"
# s = "1337c0d3"
# s = "0-1"
# s = "words and 987"
# s = '+-12'
# s ="-2147483647"
# print(my_atoi(s))










