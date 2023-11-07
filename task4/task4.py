import sys

def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        return numbers
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

# Получаем путь к файлу из аргументов командной строки
if len(sys.argv) == 2:
    file_path = sys.argv[1]
    nums = read_numbers_from_file(file_path)
    if nums:
        print(min_moves_to_equal_elements(nums))
    else:
        print("Failed to read numbers from file.")
else:
    print("Please provide the file path as an argument.")
