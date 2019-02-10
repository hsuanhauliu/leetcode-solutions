package solution

func isValid(s string) bool {
	length := len(s)
	stack := make([]byte, length)
	curr := 0

	for i := 0; i < length; i++ {
		char := s[i]

		switch char {
		case '(':
			stack[curr] = char + 1
			curr++
		case '[', '{':
			stack[curr] = char + 2
			curr++
		case ')', ']', '}':
			if curr > 0 && stack[curr-1] == char {
				curr--
			} else {
				return false
			}
		}
	}

	return curr == 0
}
