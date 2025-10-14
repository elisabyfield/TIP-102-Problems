'''
Problem 1: NFT Name Extractor
You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.

Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Understand the problem:
- input: list of nft dictionaries
- output: list of the nft names
- constraints: time and space complexity 
- edge cases: empty list

Match the problem:
- identify the appropriate data structure/algo 

Plan a solution step-by-step:
- iterate thru each name in each dictionary in the list and return names


Implement the solution


Review the Code:
- check for errors, edge cases, and opportunities to optimize


Evaluate the results:
- ensure solution meets problems requirements and handles edge cases


def extract_nft_names(nft_collection):
    return [nft['name'] for nft in nft_collection]

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

'''

# ---------------------------------------------
'''
Problem 2: NFT Collection Review 
You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

Task:

1. Review the provided code and identify the bug(s).

2. Explain what the bug is and how it affects the output.

3. Refactor the code to fix the bug(s) and provide the correct implementation.

'''

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# ---------------------------------------------
'''
Problem 3: Identify Popular Creators

You have been tasked with identifying the most popular NFT creators in your collection. A creator is considered "popular" if they have created more than one NFT in the collection.

Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

understand: so bascilly we need to count the number of times the creator is mentioned? and if its more than 1 we can put it in the popular list
plan: i think you could just use a dictonary and put name as the key and count as the value

'''


'''
Example Output:

['ArtByAlex']
['SpaceArt']
[]

'''