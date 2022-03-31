def insertSort(nums):

	for x in range(1,len(nums)):
		temp = nums.pop(x)
		for y in range(len(nums[:x])):
			if temp <= nums[0]:
				nums.insert(0, temp)
				break
			elif y == x - 1:
				nums.insert(y+1, temp)
			elif temp > nums[y] and temp <= nums[y + 1]:
				nums.insert(y+1, temp)
				break
	return nums

def mergeSort(nums):
	size = len(nums)
	if size == 0:
		return []
	elif size == 1:
		return [nums[0]]
	else:
		temp1 = mergeSort(nums[:size//2]) + [float('inf')]
		temp2 = mergeSort(nums[size//2:]) + [float('inf')]
		answer = []
		x, y = 0, 0
		while temp1[x] != float('inf') or temp2[y] != float('inf'):
			if temp1[x] <= temp2[y]:
				answer.append(temp1[x])
				x += 1
			else:
				answer.append(temp2[y])
				y += 1
		return answer

def quickSort(nums):
	if len(nums) == 0: 
		return []
	if len(nums) == 1:
		return [nums[0]]
	mid = nums[len(nums)//2]
	lesser = []
	greater = []
	for x in nums:
		if x < mid:
			lesser.append(x)
		else:
			greater.append(x)
	return quickSort(lesser) + quickSort(greater)

test = [9,1,3, 4, 6, 4535, -900]
# print(insertSort(test))
print(mergeSort(test))
# print(quickSort(test))