package containsNearbyAlmostDuplicate

import "testing"

func Test(t *testing.T) {
	var tests = []struct {
		nums []int
		k, t int
		want bool
	}{
		{[]int{}, 1, 1, false},
		{[]int{1}, 1, 1, false},
		{[]int{1}, 3, 1, false},
		{[]int{1, 2, 3, 1}, 3, 0, true},
		{[]int{1, 0, 1, 1}, 1, 2, true},
		{[]int{1, 5, 9, 1, 5, 9}, 2, 3, false},
	}

	for _, c := range tests {
		got := containsNearbyAlmostDuplicate(c.nums, c.k, c.t)
		if got != c.want {
			t.Errorf("containsNearbyAlmostDuplicate(%v, %d, %d) == %t, want %t", c.nums, c.k, c.t, got, c.want)
		}
	}
}
