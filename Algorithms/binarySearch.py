
def binary_search(arr, target):
	first_index = 0
	end_index = len(arr) - 1
	mid_point = 0
	mid_point_value = 0
	
	while first_index <= end_index:
		mid_point = first_index + (end_index - first_index) // 2
		mid_point_value = arr[mid_point]
	
		if mid_point_value == target:
			return mid_point

		elif target < mid_point_value:
			end_index = mid_point - 1
			

		else:
			first_index = mid_point + 1
			

	return None

arr = [5, 6, 7, 18, 20, 25, 20]
target = 20
print(binary_search(arr, target))

