# problem 1: Finding perfect song 
'''
- binary search = set left snf right 
- check middle value, return if length
- if less than, go left and repeat
- if greater than, go right and repeat 
- return -1 if not in playlist
'''
def find_perfect_song(playlist, length):
	left = 0
	right = len(playlist) - 1

	while left <= right:
		mid = (left + right) // 2

		if length == playlist[mid]:
			return mid
		elif length < playlist[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return -1

#print(find_perfect_song([101, 102, 103, 104, 105], 103))
#print(find_perfect_song([201, 202, 203, 204, 205], 206))


# problem 2: finding tour dates
'''
o(log n) means binary search
false otherwise 
return true if you can attend
'''
def can_attend(tour_dates, available):
	if not tour_dates:
		return False
	
	mid = len(tour_dates)//2

	if tour_dates[mid] == available:
		return True
	elif available < tour_dates[mid]:
		return can_attend(tour_dates[:mid], available)
	else:
		return can_attend(tour_dates[mid+1:], available)
	

print(can_attend([1, 3, 7, 10, 12], 12))
print(can_attend([1, 3, 7, 10, 12], 5)) 

# problem 3: sqrt(x)
'''

constarints: return squareroot down to nearest non-negative integer
edge cases: x = 0 or 1, then sqrt is itself
'''
def my_sqrt(x):
	if x < 2:
		return x
	left, right = 0,x
	result = 0

	while left <= right:
		mid = (left + right) // 2 
		square = mid * mid 
		if square == x:
			return mid
		elif square < x:
			result = mid # store current mid as possible sqrt
			left = mid + 1
		else:
			right = mid - 1
	return result

print(my_sqrt(4))
print(my_sqrt(8))
