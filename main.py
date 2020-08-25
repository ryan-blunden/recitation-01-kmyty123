"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
  """ done. """
  return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  if right >= left:
    mid = (left + right)//2
    if mylist[mid] == key:
      return mid

    elif mylist[mid] > key:
      return _binary_search(mylist, key, left, mid-1)

    else:
      return _binary_search(mylist, key, mid+1, right)

  else:
    return -1

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1,2,3,4,5], 3) == 2
	assert binary_search([1,2,3,4,5],1) == 0


def time_search(search_fn, mylist, key):
  start=time.time()
  search_fn(mylist,key)
  end=time.time()
  totaltime=(end-start)*1000
  return totaltime
  
	### TODO

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	time_search_list = []
	for size in sizes:
		mylist = list(range(size))
		binary_search_time = time_search(binary_search, mylist,-1)
		linear_search_time = time_search(linear_search, mylist,-1)
		time_search_list.append((size, binary_search_time, linear_search_time))
	return time_search_list

"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""



def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
