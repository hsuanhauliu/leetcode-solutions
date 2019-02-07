package solution

func longestCommonPrefix(strs []string) string {
	short := shortest(strs)

	for i, c := range short {
		for j := 0; j < len(strs); j++ {
			if strs[j][i] != byte(c) {
				return strs[j][:i]
			}
		}
	}

	return short
}

func shortest(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	min := strs[0]
	for _, str := range strs {
		if len(min) > len(str) {
			min = str
		}
	}

	return min
}
