'''
Problem 1:
NFT name Extractor - COME BACK

Understand the problem:
- input: list of NFT dictionaires structured as list, creator, and current value
- output: all nft names from each dictionary in list
- constraints: time complexity
- edge cases: empty list 

Match the problem:
- identify the appropriate data structure/algo 
- simple iteration

Plan a solution step-by-step:
- interate thru each name in each dictionary in the list and return names

Implement the solution


Review the Code:
- check for errors, edge cases, and opportunities to optimize


Evaluate the results:
- ensure solution meets problems requirements and handles edge cases

def extract_nft_names(nft_collection):
    return [nft['name'] for nft in nft_collection]

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

# ---------------------------------------------------------------------------------------
'''
Problem 2: NFT Collection Review
You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

Task:

1. Review the provided code and identify the bug(s).
should use .append()

2. Explain what the bug is and how it affects the output.
 should use .append()
 
3. Refactor the code to fix the bug(s) and provide the correct implementation.

DONT NEED TO DO? 

Understand the problem:
- input: list of NFT dictionaries
- output: return names in list
- constraints: 
- edge cases: 

Match the problem:
- identify the appropriate data structure/algo 

Plan a solution step-by-step:
- create empty list called nft_names
- iterate thru each dictionary in list 
- used .append() instead of +=
- return nft_names

Implement the solution


Review the Code:
- check for errors, edge cases, and opportunities to optimize


Evaluate the results:
- ensure solution meets problems requirements and handles edge cases
'''

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
       nft_names.append(nft["name"])#nft_names += nft["name"]
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

# time complexity o(n)