package solution

import "testing"

func TestLongestCommonPrefix(t *testing.T) {
	var tests = []struct {
		s    []string
		want string
	}{
		{[]string{"cat", "cat", "cat"}, "cat"},
		{[]string{"flower", "flow", "flight"}, "fl"},
		{[]string{"dog", "racecar", "car"}, ""},
		{[]string{}, ""},
	}

	for _, c := range tests {
		got := longestCommonPrefix(c.s)
		if got != c.want {
			t.Errorf("longestCommonPrefix(%v) == %s, want %s", c.s, got, c.want)
		}
	}
}
