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

'''----------------------------------------------------------------------------------
Problem 1: New Horizons 
'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

# instantiate your villager here 
apollo = Villager('Apollo', 'Eagle', 'pah')

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 


''' ----------------------------------------------------------------------------------
Problem 2: Greet Player
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# instantiate your villager here 
apollo = Villager('Apollo', 'Eagle', 'pah')
bones = Villager('Bones', 'Dog', 'yip yip')

print(bones.greet_player('Tram'))


''' ----------------------------------------------------------------------------------
Problem 3: Update Catchphrase
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# instantiate your villager here 
apollo = Villager('Apollo', 'Eagle', 'pah')
bones = Villager('Bones', 'Dog', 'yip yip')

# update bones catchphrase 
bones.catchphrase = 'ruff it up'

print(bones.greet_player('Samia'))


''' ----------------------------------------------------------------------------------
Problem 4: Set Character

Understand the problem:
- input: one parameter - new catchphrase 
- output: - Catchphrase updates or Invalid Catchphrase
- constraints: less than 20 chars and contain only letters/whitespace
- edge cases: just input space, no input 


Match the problem:
- identify the appropriate data structure/algo


Plan a solution step-by-step:
- define set_catchphrase with one param: new catchphrase
- check if input is < 20 
- interate thru input and verify each char is either alphabet or spaces
- if true, update catchphrase and return true phrase
-  if false, dont update and false return phrase 


Implement the solution

Review the Code:
- check for errors, edge cases, and opportunities to optimize

Evaluate the results:
- ensure solution meets problems requirements and handles edge cases
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20:
            if all(char.isalpha() or char.isspace() for char in new_catchphrase):
                self.catchphrase = new_catchphrase 
                print(("Catchphrase updated!"))
                return 
        print("Invalid catchphrase")

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)

alice.set_catchphrase("#?!")
print(alice.catchphrase)