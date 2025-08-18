from itertools import product

memo = {}

def get_measurable_weights(W):
	key = tuple(sorted(W))  # 重りの並び順は関係ない
	if key in memo:
		return memo[key]

	measured = set()
	for signs in product([-1, 0, 1], repeat=len(W)):
		total = sum(w * s for w, s in zip(W, signs))
		if total > 0:
			measured.add(total)

	memo[key] = measured
	return measured

while 1:
	n, m = map(int, input().split())
	if n == 0 and m == 0:
		break

	A = list(map(int, input().split()))
	W = list(map(int, input().split()))
	ma = max(A)
	found = False
	ans = -1

	for new_weight in range(ma):
		if new_weight in W:
			continue
		W.append(new_weight)
		measurable = get_measurable_weights(W)
		if all(a in measurable for a in A):
			ans = new_weight
			found = True
			W.pop()
			break
		W.pop()

	print(ans)
