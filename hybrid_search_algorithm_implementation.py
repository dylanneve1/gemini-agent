
class HybridSearchAlgorithm:
    def __init__(self, data):
        self.data = data

    def hybrid_search(self, target):
        # First, try the iterative search
        for index, value in enumerate(self.data):
            if value == target:
                return index
        # If not found, try the recursive search
        return self.recursive_search(target)

    def recursive_search(self, target, left=0, right=None):
        if right is None:
            right = len(self.data) - 1
        if left > right:
            return -1  # Base case: target not found
        mid = (left + right) // 2
        if self.data[mid] == target:
            return mid
        elif self.data[mid] < target:
            return self.recursive_search(target, mid + 1, right)
        else:
            return self.recursive_search(target, left, mid - 1)

# Example usage
sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_algorithm = HybridSearchAlgorithm(sample_data)
result = search_algorithm.hybrid_search(5)
print(f'Target found at index: {result}')
