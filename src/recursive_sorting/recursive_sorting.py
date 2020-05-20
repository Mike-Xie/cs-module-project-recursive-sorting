# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA: list, arrB: list):
	# empty list, a relic of C
	# merged_arr: list = [0] * elements
	merged_arr: list = []

	# initialize counters to increment while going thru arrA
	# and arrB
	a_counter: int = 0
	b_counter: int = 0
	# while neither list is fully consumed
	# if the elem at A is smaller, append to return list
	# increment A, same for eleme at B
	# once one list is fully used up, append rest of other list
	# to return list 
	while a_counter < len(arrA) and b_counter < len(arrB):
		if arrA[a_counter] < arrB[b_counter]:
			merged_arr.append(arrA[a_counter])
			a_counter += 1
		else:  
			merged_arr.append(arrB[b_counter])
			b_counter += 1 
	# once that while loop exits, do this one that adds remaining 
	# elements of non consumed list
	# add remaining elements from a
	while a_counter < len(arrA):
		merged_arr.append(arrA[a_counter])
	while b_counter < len(arrB):
		merged_arr.append(arrB[b_counter])
	return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr: list):
	# base case is len of 1 return at end else do this if
	if len(arr) > 1:
		midpoint: int = len(arr) // 2
		left: list = merge_sort(arr[:midpoint])
		right: list = merge_sort(arr[midpoint:])
		arr = merge(left, right)
	# print("sort")
	# print(arr)
	return arr 


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
	# pointer for start of second list 
	start_second = mid + 1 

	if arr[mid] <= arr[start_second]:
		return
	# while either of the list is not finished processing
	# do nothing if the first is smaller since it'll be right place
	# else have to shift everything
	while (start <= mid and start_second <= end):
		if (arr[start]) <= arr[start_second]:
			start += 1
		else:
			temp_value = arr[start2]
			index = start_second
			# shift everything between the two by one
			while (index != start):
				arr[index] = arr[index - 1]
				index = index - 1 
			arr[start] = temp_value
			# move all pointers by one 
			start += 1
			mid += 1
			start_second += 1 
	return arr


def merge_sort_in_place(arr, l, r):
	# almost same as above except with pointers
	if (l < r):
		mid = l + (r - l) //2
		merge_in_place(arr, l, m)
		merge_in_place(arr, m + 1, r)
		merge_in_place(arr, l, m, r)
	return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
	# Your code here

	return arr
