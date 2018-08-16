import "sort"

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	// k = maximum difference between indices
	// t = miximum difference between values

	if len(nums) < 2 && k < 1 && t < 0 {
		return false
	}

	// make sure the length of subset is not out of range
	diff := k + 1
	if k + 1 > len(nums) {
		diff = len(nums)
	}

	// make a copy of the array
	subset := make([]int, diff)
	copy(subset[:], nums[:diff])
	sort.Ints(subset[:])

	// keep track of the first number and the the next unchecked number
	first_num_index := 0

	// compare the differences between each pair with t
	for i := 0; i + 1 < len(subset); i++ {
		if subset[i + 1] - subset[i] <= t {
			return true
		}
	}

	for next_num_index := diff; next_num_index < len(nums); next_num_index++ {
		pos := replaceAndSort(subset, nums[first_num_index], nums[next_num_index])
		if (pos + 1 < diff && subset[pos + 1] - subset[pos] <= t) ||
			(pos - 1 > -1 && subset[pos] - subset[pos - 1] <= t) {
			return true
		}
		first_num_index++
	}

	return false
}

// find the target and replace it with another number.
// return the position where the updated number is moved to.
func replaceAndSort(nums []int, find int, replace_with int) int {
	// find the element in the array then replace it with the new number
	pos := 0
	for i := len(nums) - 1; i > -1; i-- {
		if nums[i] == find {
			nums[i] = replace_with
			pos = i
			break
		}
	}

	if find > replace_with {
		for ; pos > 0; pos-- {
			if nums[pos - 1] > nums[pos] {
				temp := nums[pos - 1]
				nums[pos - 1] = nums[pos]
				nums[pos] = temp
			} else {
				return pos
			}
		}
	} else if find < replace_with {
		for ; pos + 1 < len(nums); pos++ {
			if nums[pos] > nums[pos + 1] {
				temp := nums[pos]
				nums[pos] = nums[pos + 1]
				nums[pos + 1] = temp
			} else {
				return pos
			}
		}
	}
	return pos
}
