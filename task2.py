def longest_increasing_streak(nums: list[int]) -> dict:
    if not nums:
        return {"length": 0, "streak": []}

    best_start, best_len = 0, 1
    cur_start, cur_len = 0, 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur_len += 1
        else:
            cur_start, cur_len = i, 1
        if cur_len > best_len:
            best_len, best_start = cur_len, cur_start

    if best_len < 2:
        return {"length": 0, "streak": []}
    return {"length": best_len, "streak": nums[best_start:best_start + best_len]}


if __name__ == "__main__":
    print(longest_increasing_streak([1, 3, 2, 5, 8, 4, 7]))
