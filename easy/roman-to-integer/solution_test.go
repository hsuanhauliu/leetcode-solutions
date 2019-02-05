package solution

import "testing"

func TestRomanToInt(t *testing.T) {
	var tests = []struct {
		s    string
		want int
	}{
		{"III", 3},
		{"IV", 4},
		{"IX", 9},
		{"LVIII", 58},
		{"MCMXCIV", 1994},
	}

	for _, c := range tests {
		got := romanToInt(c.s)
		if got != c.want {
			t.Errorf("romanToInt(%s) == %d, want %d", c.s, got, c.want)
		}
	}
}
