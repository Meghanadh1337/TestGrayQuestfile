def isBinaryAnagram(first, second):
    firstBinary=bin(first)[2:]
    secondBinary=bin(second)[2:]    
    return sorted(firstBinary)==sorted(secondBinary)

def find_pair_with_sum(arr, target):
    n = len(arr)
    # Step 1: Find the smallest element
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break
    low = (i + 1) % n  # Index of smallest element
    high = i           # Index of largest element
    # Step 2: Use two pointers to find the pair
    while low != high:
        current_sum = arr[low] + arr[high]
        if current_sum == target:
            return True  # Pair found
        elif current_sum < target:
            low = (low + 1) % n  # Move to next higher value
        else:
            high = (high - 1 + n) % n  # Move to next lower value
    return False  # No pair found

def count_lines_in_file(file_path):
    line_count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lineCount += 1
        return lineCount
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'.")
        return None
# Example Usage
file_path = "example.txt"  # Replace with your file path
total_lines = count_lines_in_file(file_path)
if total_lines is not None:
    print(f"The total number of lines: {total_lines}")


class Rectangle:
    def __init__(self, length, breadth):
        if not isinstance(length, int) or not isinstance(breadth, int):
            raise ValueError("Length and breadth must be integers.")
        if length <= 0 or breadth <= 0:
            raise ValueError("Length and breadth must be greater than zero.")
        
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def is_square(self):
        return self.length == self.breadth


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_numbers(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    result = []
    
    for num in range(2, n + 1):
        if not is_prime(num):
            for p1 in primes:
                for p2 in primes:
                    if p1 + p2 == num:
                        result.append(num)
                        break
                if num in result:
                    break
    print(", ".join(map(str, result)))
    
def main():
    print("Testing isBinaryAnagram:")
    first, second = 5, 10  # Binary: '101' and '1010'
    print(f"Is {first} binary anagram of {second}? {isBinaryAnagram(first, second)}\n")

    print("Testing find_pair_with_sum:")
    arr = [11, 15, 6, 8, 9, 10]
    target = 16
    print(f"Array: {arr}, Target Sum: {target}")
    print(f"Is there a pair with sum {target}? {find_pair_with_sum(arr, target)}\n")

    print("Testing count_lines_in_file:")
    file_path = "input.txt"  
    total_lines = count_lines_in_file(file_path)
    if total_lines is not None:
        print(f"The total number of lines in '{file_path}': {total_lines}\n")

    print("Testing Rectangle class:")
    try:
        rect = Rectangle(5, 4)
        print(f"Rectangle Length: {rect.length}, Breadth: {rect.breadth}")
        print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}, Is Square: {rect.is_square()}\n")
    except ValueError as e:
        print(f"Error creating rectangle: {e}")

    print("Testing find_numbers:")
    n = 20
    print(f"Non-prime numbers <= {n} that are sum of two primes:")
    find_numbers(n)


if __name__ == "__main__":
    main()
