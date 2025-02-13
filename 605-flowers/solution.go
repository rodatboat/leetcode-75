func canPlaceFlowers(flowerbed []int, n int) bool {
	size := len(flowerbed)
	r := 0
	for idx, i := range flowerbed {
		var hasNextZ bool = func() bool {
			if idx == size-1 || flowerbed[idx+1] == 0 {
				return true
			}
			return false
		}()
		var hasPrevZ bool = func() bool {
			if idx == 0 || flowerbed[idx-1] == 0 {
				return true
			}
			return false
		}()

		if i == 0 && hasNextZ && hasPrevZ {
			r += 1
			flowerbed[idx] = 1
		}
	}

	return r >= n
}