def count_inversions(data, threshold):
    def sort_and_count(seq, aux, lo, hi):
        if lo >= hi:
            return 0
        mid = (lo + hi) // 2
        total = sort_and_count(seq, aux, lo, mid)
        total += sort_and_count(seq, aux, mid + 1, hi)
        total += merge_and_count(seq, aux, lo, mid, hi)
        return total

    def merge_and_count(seq, aux, lo, mid, hi):
        left, right, idx, inv_count = lo, mid + 1, lo, 0
        while left <= mid and right <= hi:
            if seq[left] > seq[right] + threshold:
                inv_count += (mid - left + 1)
                right += 1
            else:
                left += 1

        left, right = lo, mid + 1
        while left <= mid and right <= hi:
            if seq[left] <= seq[right]:
                aux[idx] = seq[left]
                left += 1
            else:
                aux[idx] = seq[right]
                right += 1
            idx += 1

        while left <= mid:
            aux[idx] = seq[left]
            left += 1
            idx += 1

        while right <= hi:
            aux[idx] = seq[right]
            right += 1
            idx += 1

        for i in range(lo, hi + 1):
            seq[i] = aux[i]

        return inv_count

    temp = [0] * len(data)
    return sort_and_count(data, temp, 0, len(data) - 1)

with open("input.txt") as file:
    size, limit = map(int, file.readline().split())
    numbers = list(map(int, file.readline().split()))
    print(count_inversions(numbers, limit))
