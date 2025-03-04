package main

type Queue []int

func (q *Queue) Append(i int) {
	*q = append(*q, i)
}

func (q *Queue) Popleft() int {
	if len(*q) == 0 {
		return 99999999
	}
	i := (*q)[0]
	*q = (*q)[1:]
	return i
}

func predictPartyVictory(senate string) string {
	n := len(senate)
	var r Queue
	var d Queue
	for idx, i := range senate {
		if i == 'D' {
			d.Append(idx)
		} else {
			r.Append(idx)
		}
	}

	for len(r) > 0 && len(d) > 0 {
		r_idx := r.Popleft()
		d_idx := d.Popleft()
		if r_idx < d_idx {
			r.Append(r_idx + n)
		} else {
			d.Append(d_idx + n)
		}
	}

	if len(r) > 0 {
		return "Radiant"
	} else {
		return "Dire"
	}
}
