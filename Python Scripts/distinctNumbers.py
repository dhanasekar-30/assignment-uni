def count_distinct_numbers(arr, N, K):
    distinct_counts = []
    window_counts = {}
    distinct_count = 0

    for i in range(K):
        if arr[i] not in window_counts or window_counts[arr[i]] == 0:
            distinct_count += 1
        window_counts[arr[i]] = window_counts.get(arr[i], 0) + 1
    distinct_counts.append(distinct_count)

    for i in range(K, N):
        window_counts[arr[i - K]] -= 1
        if window_counts[arr[i - K]] == 0:
            distinct_count -= 1
        if arr[i] not in window_counts or window_counts[arr[i]] == 0:
            distinct_count += 1
        window_counts[arr[i]] = window_counts.get(arr[i], 0) + 1
        distinct_counts.append(distinct_count)
    return distinct_counts


arr = [1, 2, 1, 3, 4, 2, 3]
N = 7
K = 4

distinct_counts = count_distinct_numbers(arr, N, K)

for i, count in enumerate(distinct_counts):
    print(f"{i + 1}. {count}")