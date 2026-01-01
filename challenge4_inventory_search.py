import heapq

def kthSmallest(matrix, k):
    n = len(matrix)

    # Min heap will store tuples: (value, row, col)
    heap = []

    # Step 1: Push first element of each row
    for r in range(n):
        heapq.heappush(heap, (matrix[r][0], r, 0))

    # Step 2: Pop k-1 elements
    for _ in range(k - 1):
        value, r, c = heapq.heappop(heap)

        # Push next element from same row (if exists)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

    # Step 3: kth popped element
    return heapq.heappop(heap)[0]

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))  # Output: 13


# ✅ Approach A — Min Heap (Priority Queue)

# Treat each row like a sorted list.
# We merge sorted rows like merging k sorted lists.

# 🧠 Key Idea

# Push first element of each row into a min-heap

# Repeatedly:

# Pop the smallest (this is next smallest overall)

# Push the next element from that row

# The kᵗʰ removed element = answer

# ⏱ Complexity

# Time → O(k log n)

# Space → O(n)