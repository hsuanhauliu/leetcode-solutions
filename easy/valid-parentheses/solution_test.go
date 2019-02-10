package solution

import "testing"

func TestIsValid(t *testing.T) {
	var tests = []struct {
		s    string
		want bool
	}{
		{"()", true},
		{"()[]{}", true},
		{"(]", false},
		{"([)]", false},
		{"{[]}", true},
		{"(", false},
		{"", true},
	}

	for _, c := range tests {
		got := isValid(c.s)
		if got != c.want {
			t.Errorf("isValid(%s) == %t, want %t", c.s, got, c.want)
		}
	}
}
