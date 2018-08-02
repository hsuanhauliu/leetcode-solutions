// Helper function for backspaceCompare to retrieve a character according
// to the input index.
func getChar(str string, curr_index int) (char byte, next_index int) {
	if curr_index < 0 {
		char = ' '
		next_index = -1
		return
	}

	char = str[curr_index]
	next_index = curr_index

	if char == '#' {
		skip_counter := 1

		for skip_counter >= 0 {
			next_index--	// shift by one character

			// make sure we don't go out of range
			if next_index < 0 {
				char = ' '
				next_index = -1
				return
			}

			if str[next_index] == '#' {
				skip_counter++
			} else {
				skip_counter--
			}
		}
		char = str[next_index]
	}
	next_index--	// update index

	return
}

// Main function that we are writing.
// Runtime complexity: O(N)
// Space complexity: O(1)
func backspaceCompare(S string, T string) bool {
	curr_index_s, curr_index_t := len(S) - 1, len(T) - 1
	var curr_char_s, curr_char_t byte

	for curr_index_s > -1 || curr_index_t > -1 {
		curr_char_s, curr_index_s = getChar(S, curr_index_s)
		curr_char_t, curr_index_t = getChar(T, curr_index_t)
		if curr_char_s != curr_char_t { return false }
	}

	return true
}
