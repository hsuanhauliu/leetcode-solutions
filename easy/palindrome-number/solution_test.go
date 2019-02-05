package solution

import "testing"

func TestIsPalidrome(t *testing.T) {
	var tests = []struct {
		n    int
		want bool
	}{
		{121, true},
		{11, true},
		{1234554321, true},
		{-121, false},
		{10, false},
		{0, true},
	}

	for _, c := range tests {
		got := isPalindrome(c.n)
		if got != c.want {
			t.Errorf("isPalindrome(%d) == %t, want %t", c.n, got, c.want)
		}
	}
}
