def binary_search(arr1, target):
	first_index = 0
	end_index = len(arr) - 1

	while first_index <= end_index:
		mid_point = first_index + (end_index - first_index) //2
		mid_point_value = arr[mid_point]

		if mid_point_value == target:
			return mid_point

		elif item < mid_point_value:
			end_index = mid_point - 1

		else:
			begin_index = mid_point + 1

	return None


arr = [1, 3, 10, 15, 18, 20, 30, 49]
target = 20

print(binary_search(arr,target))