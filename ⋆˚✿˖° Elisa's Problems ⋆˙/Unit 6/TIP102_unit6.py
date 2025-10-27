# Problem 1
'''
class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
        
#top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

node3 = SongNode("Bad Romance")
node2 = SongNode("Party Rock Anthem", node3)
top_hits_2010s  =  SongNode("Uptown Funk", node2) # head

print_linked_list(top_hits_2010s)

''' 

# Problem 2
# Plan:
#- traverse through the list
#- add artists + increment frequency count in dictionary
#- return dictionary
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    artists = {}
    current = playlist
    while current:
        if current.artist not in artists:
            artists[current.artist] = 1
        else:
            artists[current.artist] +=1
        current = current.next
    print(artists)


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)
