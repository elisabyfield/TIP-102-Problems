'''
Understand the problem:
- input:
- output:
- constraints:
- edge cases:


Match the problem:
- identify the appropriate data structure/algo


Plan a solution step-by-step:

Implement the solution


Review the Code:
- check for errors, edge cases, and opportunities to optimize


Evaluate the results:
- ensure solution meets problems requirements and handles edge cases
'''

'''Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.

Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, and returns a list with the name of all friends the current villager and new_contact have in common.

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        pass

Understand the problem: 
- input: new_contact 
- output: list of mutuals between current name and the new contact
- constraints: time complexity
- edge cases: no mutuals, invalid input, duplicates 


Match the problem:
- identify the appropriate data structure/algo :(using a list, )


Plan a solution step-by-step:
- create the method get_mutuals that takes in one parameter, new_contact
- iterate through friends attribute of current and new contact
- create set() of mutuals
- return the names of the mutuals

Implement the solution


Review the Code:
- check for errors, edge cases, and opportunities to optimize


Evaluate the results:
- ensure solution meets problems requirements and handles edge cases

-----
'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    # alternate     
    def get_mutuals(self, new_contact):
        mutuals = []
        for friend in self.friends:
            if friend in new_contact.friends:
                mutuals.append(friend.name)
        return mutuals

'''
# better time complexity 
    def get_mutuals(self, new_contact):
        mutuals = set(self.friends) & set(new_contact.friends)
        return [friend.name for friend in mutuals]
'''

bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))

# -----------------------------------------------------------------------------------------------
'''
Problem 2: Linked Up
A linked list is a data structure that, similar to a normal list or array, allows us to store pieces of data sequentially. The key difference is how the elements are stored in memory.

In a normal list, elements are stored in adjacent memory locations. If we know the location of the first element, we can easily access any other element in the list.

In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Instead, each node stores a reference or pointer to the next node in the list, allowing us to traverse the list.

Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.

Example Output:

K.K. Slider -> Harriet -> Saharah -> Isabelle


Understand the problem:
- input: head of linked list
- output: return the printed connected values on the list given 
- constraints: time complexity
- edge cases: existing 


Match the problem:
- identify the appropriate data structure/algo
--> linked lists 

Plan a solution step-by-step:
- start at head
- traverse through the list and print value of list
- return 

Implement the solution

'''

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


kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# add code here to link the above nodes

kk_slider.next= harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider)
