'''
Understand the problem:
- input: list of strings (suits)
- output: the total number(counting to it)
- constraints: 
first function: iteratively
second function: recursively
no use of len func for both
- edge cases: empty suits


Match the problem:
- identify the appropriate data structure/algo
loops 

Plan a solution step-by-step:
for the interative function:
- set count to 0 
- iterate thru all suits
- increment count by 1
- return count 

for the recursive:
    if count == len(suits)
return count

else:
    count_suits_recursive(len(suits) - 1)


Implement the solution

Review the Code:
- check for errors, edge cases, and opportunities to optimize

Evaluate the results:
- ensure solution meets problems requirements and handles edge cases
'''


'''
Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of suits in the list.

1. Implement the solution iteratively without the use of the len() function.
2. Implement the solution recursively.
3. Discuss: what are the similarities between the two solutions? What are the differences?
'''
'''
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count +=1
    return count


def count_suits_recursive(suits):
    if suits == []:
        return 0
    else:
       return 1 + count_suits_recursive(suits[1:])
        # keep counting until list end

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

# Example Output:
# 3
# 3

'''


'''
Problem 2: Collecting Infinity Stones 
Thanos is collecting Infinity Stones. Given an array of integers stones representing the power of each stone, return the total power using a recursive approach.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

U:
input: array of integers (stones)
output:in integer representing the total power 
conostraints: has to be recursive, time complexity 
edge cases: empty array, 

M: recursion
P: 
- make variable sum
- if the array is empty, return 0
- else: return sum + the function(1:)
I:
R:
E:
'''

def sum_stones(stones):
    sum = 0 # sum approach first
    if stones == []:
        return 0
    else:
        sum = stones[0]
        return sum + sum_stones(stones[1:]) 

# current time complexity: o(n^2)
    
# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

#Example Output:
#105
#68
'''
Problem 3: Counting Distinct Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of distinct suits in the list.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
def count_suits_iterative(suits):
    pass
'''

#U: 
#outputs: total number of distinct suits
#inputs: a list of srings --> each representing a suit
#constraints: need to count DISTINCT suits, iterative and recursive 
#edge cases: no duplicates 

#M:
#- iteration 
#- recursion

#P:
# iterative 
#- create a empty new list 
# - or create dictionary with keys = to the strings given and value would be the count
#- iterate through each suit 
# append each distinct suit
# count suits in new list


# recursive 
# - 

def count_suits_iterative(suits):
    newlist =[]
    count = 0
    for string in suits:
        if string not in newlist:
            newlist.append(string) 
            count += 1
        else: 
            pass
    return count


def count_suits_recursive(suits):
    

            
#I:
#R:
#E:


print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

#Example Output:

#2
#2
'''
💡 Hint: Multiple Recursive Cases

Problem 4: Calculating Groot's Growth
Groot grows according to a pattern similar to the Fibonacci sequence. Given n, find the height of Groot after n months using a recursive method.

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def fibonacci_growth(n):
    pass
Example Usage:

print(fibonacci_growth(5))
print(fibonacci_growth(8))
Example Output:

5
21

Problem 5: Calculating the Power of the Fantastic Four
The superhero team, The Fantastic Four, are training to increase their power levels. Their power level is represented as a power of 4. Write a recursive function that calculates the result of 4 raised to the nth power to determine their training level.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def power_of_four(n):
    pass
Example Usage:

print(power_of_four(2))
print(power_of_four(-2))
Example Output:

16
Example 1 Explanation: 4 to the 2nd power (4 * 4) is 16. 
.0625
Example 2 Explanation: 4 to the power of -2 is 1/(4 * 4), which is 0.0625.

Problem 6: Strongest Avenger
The Avengers need to determine who is the strongest. Given a list of their strengths, find the maximum strength using a recursive approach without using the max() function.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def strongest_avenger(strengths):
    pass
Example Usage:

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))
Example Output:

100
Example 1 Explanation: The maximum strength among the Avengers is 100.

90
Example 2 Explanation: The maximum strength among the Avengers is 90.

Problem 7: Counting Vibranium Deposits
In Wakanda, vibranium is the most precious resource, and it is found in several deposits. Each deposit is represented by a character in a string (e.g., "V" for vibranium, "G" for gold, etc.)

Given a string resources, write a recursive function count_deposits() that returns the total number of distinct vibranium deposits in resources.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def count_deposits(resources):
    pass
Example Usage:

print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))
Example Output:

5
2
Example 2 Explanation: There are two characters "V" in the string "VXVYGA", 
therefore there are two vibranium deposits in the string.

Problem 8: Merging Missions
The Avengers are planning multiple missions, and each mission has a priority level represented as a node in a linked list. You are given the heads of two sorted linked lists, mission1 and mission2, where each node represents a mission with its priority level.

Implement a recursive function merge_missions() which merges these two mission lists into one sorted list, ensuring that the combined list maintains the correct order of priorities. The merged list should be made by splicing together the nodes from the first two lists.

Return the head of the merged mission linked list.

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    pass
Example Usage:

mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))
1 -> 1 -> 2 -> 3 -> 4 -> 4

Problem 9: Merging Missions II
Below is an iterative solution to the merge_missions() function from the previous problem. Compare your recursive solution to the iterative solution below.

Discuss with your podmates. Which solution do you prefer?

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions_iterative(mission1, mission2):
    temp = Node()  # Temporary node to simplify the merging process
    tail = temp

    while mission1 and mission2:
        if mission1.value < mission2.value:
            tail.next = mission1
            mission1 = mission1.next
        else:
            tail.next = mission2
            mission2 = mission2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if mission1:
        tail.next = mission1
    elif mission2:
        tail.next = mission2

    return temp.next  # Return the head of the merged linked list

    '''