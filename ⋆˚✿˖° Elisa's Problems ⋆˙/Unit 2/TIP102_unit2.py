'''
Problem 1: Festival Lineup
Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).


Understand the problem:
- input: artists and set_times
- output: dictionary lineup
- constraints: time complexity (aim for O(n))
- edge cases: empty list of artists/set_times
- one of values not string

Plan a solution step-by-step:
- considering artist - key and set time - value , build a dictionary of {string:string}
- iterat

Implement the solution:
'''

def lineup(artists, set_times):
    n = len(artists)
    lineup = {}
    for i in range(n):
        lineup[artists[i]] = set_times[i]

    return lineup

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

'''
Problem 2: Planning App
You are designing an app for your festival to help attendees have the best experience possible! As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

U:
- input: artist and festival_schedule dictionary
- output: dictionary; day, time, and stage for given artist
- constraints: time complexity (aim for O(n))
    - artist does no exist, return dictionary {"message": "Artist not found"}
- edge cases: multiple bookings for same artists (for more advanced cased but not for this problem)

P:
return the existing dictionary value for the respective artist. if the artist does not exist, return error message.{"message": "Artist not found"}
I;
'''
def get_artist_info(artist, festival_schedule):
    error_msg = {"message":"Artist not found!"}
    if artist in festival_schedule.keys():
        return festival_schedule[artist]
     
    return error_msg

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule)) 

'''
Problem 3: Ticket Sales
A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

U:
inputs: ticket_sales
outputs: sum of ticket sold (values)
constraints:
edge cases:

P: iterate through dictionary, add values, and return sum

I:
'''
def total_sales(ticket_sales):
    sum = 0
    for i in ticket_sales.values():
        sum += i
    return sum

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))


#-----------------
'''
Problem 4: Scheduling Conflict
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs that are the same in each schedule.


def identify_conflicts(venue1_schedule, venue2_schedule):
    new_dict = {}
    for artist in venue1_schedule.keys():
        if artist in venue2_schedule.keys():
            if venue1_schedule[artist] == venue2_schedule[artist]
                new_dict[artistam,]

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
'''
'''
 Session 2: 
 Problem 3: Navigating the Research Station
 u:
inputs: station_layout, observations
outputs: total time it takes to visit all obserbation points 
constraints: observations may not be same length as station layout
edge cases: observation not liste within station

p: iterate through stations_layout to see if current obervation key matches station, count how many indexes it takes to visit all observation points
 '''
def navigate_research_station(station_layout, observations):
    count = 0
    for i, char in enumerate(observations ,start=0):
        if observations[i] in station_layout:
            count+=station_layout.index(char)
        else:
            print("observation point not within station layout")
    return count

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))
