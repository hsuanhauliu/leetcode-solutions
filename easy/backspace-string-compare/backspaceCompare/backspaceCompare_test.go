/* A testing script written for backspaceCompare function */

package backspaceCompare

import "testing"

func Test(t *testing.T) {
	var tests = []struct {
		s, t string
		want bool
	}{
		{"ab#c", "ad#c", true},
		{"ab##", "c#d#", true},
		{"a##c", "#a#c", true},
		{"a#c", "b", false},
		{"", "aaaaa#####", true},
		{"gggg###", "aaaaa#####", false},
	}

	for _, c := range tests {
		got := BackspaceCompare(c.s, c.t)
		if got != c.want {
			t.Errorf("BackspaceCompare(%q, %q) == %t, want %t", c.s, c.t, got, c.want)
		}
	}
}
