package main

type Queue []int

type RecentCounter struct {
	queue Queue
	ridx  int
}

func Constructor() RecentCounter {
	return RecentCounter{
		queue: Queue{},
	}
}

func (this *RecentCounter) Ping(t int) int {
	this.queue = append(this.queue, t)
	for this.queue[this.ridx] < t-3000 {
		this.ridx++
	}
	return len(this.queue) - this.ridx
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
