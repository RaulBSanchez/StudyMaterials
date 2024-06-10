
def binary_search(temp, target):
	first_index = 0
	end_index = len(temp) - 1

	while first_index <= end_index:
		mid_point = first_index + (end_index - first_index) // 2
		mid_point_value = temp[mid_point]

		if mid_point_value == target:
			return mid_point

		elif target < mid_point_value:
			end_index = mid_point - 1

		else:
			first_index = mid_point + 1

	return None

temp = [2,4,5,6,7,8,9,10,12,13,14,19,25,91]
target = 91
print(binary_search(temp, target))

