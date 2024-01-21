'''Given a non-negative number represented as an array of digits, add 1 to the number
( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.
NOTE: Certain things are intentionally left unclear in this question which you should practice asking the
interviewer. For example: for this problem, following are some good questions to ask :
• Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
• A : For the purpose of this question, YES
• Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
• A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
Input Format
First argument is an array of digits.
Output Format
Return the array of digits after adding one.
Example Input
Input 1:
[1, 2, 3]
Example Output
Output 1:
[1, 2, 4]
'''

def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits  # No carry-over needed
        digits[i] = 0  # Carry-over

    # If all digits were 9's, create a new array with an extra 1
    return [1] + [0] * n

'''
Given an array of size n, find the majority element. The majority element is the element that
appears more than floor(n/2) times.
You may assume that the array is non-empty, and the majority element always exist in the array.
Example:
Input : [2, 1, 2]
Return : 2 which occurs 2 times which is greater than 3/2.
'''
def find_majority_element(nums):
  """
  Finds the majority element in an array.

  Args:
      nums: A list of integers.

  Returns:
      The majority element, or None if no majority element exists.
  """

  # Boyer-Moore Voting Algorithm
  count = 0
  candidate = None
  for num in nums:
      if count == 0:
          candidate = num
      count += (1 if num == candidate else -1)

  # Verify candidate is majority element
  if nums.count(candidate) > len(nums) // 2:
      return candidate
  else:
      return None

# Example usage
nums = [2, 1, 2, 2, 3, 2, 2]
majority_element = find_majority_element(nums)

if majority_element is not None:
  print(f"The majority element is {majority_element}.")
else:
  print("No majority element exists.")


'''
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
A: a1 → a2
 ↘
 c1 → c2 → c3
 ↗
B: b1 → b2 → b3
begin to intersect at node c1.
Notes:
• If the two linked lists have no intersection at all, return null.
• The linked lists must retain their original structure after the function returns.
• You may assume there are no cycles anywhere in the entire linked structure.
• Your code should preferably run in O(n) time and use only O(1) memory
'''
class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def get_intersection_node(headA, headB):
  """
  Finds the node at which two singly linked lists intersect.

  Args:
      headA: The head node of the first linked list.
      headB: The head node of the second linked list.

  Returns:
      The node at which the lists intersect, or None if they don't intersect.
  """

  # Traverse both lists simultaneously, keeping track of their lengths.
  lenA, lenB = 0, 0
  pA, pB = headA, headB
  while pA and pB:
    lenA += 1
    lenB += 1
    pA = pA.next
    pB = pB.next

  # Advance the longer list by the difference in lengths.
  diff = abs(lenA - lenB)
  if lenA > lenB:
    for _ in range(diff):
      headA = headA.next
  else:
    for _ in range(diff):
      headB = headB.next

  # Traverse both lists again, checking for equality at each step.
  while headA and headB:
    if headA == headB:
      return headA
    headA = headA.next
    headB = headB.next

  # No intersection found.
  return None

'''
Given numRows, generate the first numRows of Pascal's triangle.
Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.
Example:
Given numRows = 5,
Return
[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]
Constraints:
0 <= numRows <= 25'''

def generate_pascal_triangle(numRows):
  """
  Generates the first numRows of Pascal's triangle.

  Args:
      numRows: The number of rows to generate.

  Returns:
      A list of lists representing Pascal's triangle.
  """

  if numRows == 0:
    return []

  triangle = [[1]]

  for _ in range(1, numRows):
    previous_row = triangle[-1]
    current_row = [previous_row[0]]
    for i in range(1, len(previous_row)):
      current_row.append(previous_row[i-1] + previous_row[i])
    current_row.append(previous_row[-1])
    triangle.append(current_row)

  return triangle

# Example usage
numRows = 5
pascal_triangle = generate_pascal_triangle(numRows)

for row in pascal_triangle:
  print(row)


'''Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit
reversed. Negative numbers are not palindromic.
Example :
Input : 12121
Output : 1
Input : 123
Output : 0
'''

def is_palindrome(x):
  """
  Checks if an integer is a palindrome without using extra space.

  Args:
      x: The integer to check.

  Returns:
      True if x is a palindrome, False otherwise.
  """

  if x < 0 or (x % 10 == 0 and x != 0):
    return False

  rev = 0
  while x > rev:
    rev = rev * 10 + x % 10
    x //= 10

  return x == rev or x == rev // 10  # Handle odd/even length cases
