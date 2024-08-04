
class IterativeSearchAlgorithm:
    def __init__(self, data):
        self.data = data

    def iterative_search(self, target):
        for index, value in enumerate(self.data):
            if value == target:
                return index
        return -1  # Target not found

# Example usage
sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_algorithm = IterativeSearchAlgorithm(sample_data)
result = search_algorithm.iterative_search(5)
print(f'Target found at index: {result}')
