def bucket_sort(arr):
      if len(arr) == 0:
            return arr

      min_val = min(arr)
      max_val = max(arr)

      num_buckets = max_val - min_val + 1
      buckets = [[] for _ in range(num_buckets)]

      for num in arr:
        index = num - min_val
        buckets[index].append(num)

      sorted_buckets = []
      for bucket in buckets:
        sorted_buckets.extend(sorted(bucket))

      return sorted_buckets

arr = [13, 36, 16, 8, 22, 74]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
