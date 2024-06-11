def quickSort(sequence):
	length = len(sequence)

	if length <= 1:
		return sequence
	else:
		pivot = sequence.pop()

	items_greater = []
	items_lower = []

	for item in sequence:
		if item > pivot:
			items_greater.append(item)

		else:
			items_lower.append(item)


	return quickSort(items_lower) + [pivot] + quickSort(items_greater)




print(quickSort([3,6,1,0,100,39,3,9,-10,20]))