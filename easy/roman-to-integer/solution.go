package solution

func romanToInt(s string) int {
	m := make(map[string]int)
	m["I"] = 1
	m["V"] = 5
	m["X"] = 10
	m["L"] = 50
	m["C"] = 100
	m["D"] = 500
	m["M"] = 1000

	total := 0
	prev := m[string(s[0])]

	for i := 0; i < len(s); i++ {
		curr := m[string(s[i])]

		if curr > prev {
			total = total - 2*prev
		}
		total += curr
		prev = curr
	}
	return total
}
