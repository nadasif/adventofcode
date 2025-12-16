# Use loadDataNew from mylib.py and Counter class from mylib.py
from lib.mylib import loadDataNew, Counter

class InvalidIDFinder:
    def __init__(self, data):
        left, right = data.split("-")
        self.start = int(left)
        self.end = int(right)

    def find_invalid_ids2(self):
        invalid_ids = []
        for number in range(self.start, self.end + 1):
            if self.is_valid_id2(number):
                invalid_ids.append(number)
        return invalid_ids

    def find_invalid_ids(self):
        invalid_ids = []
        for number in range(self.start, self.end + 1):
            if not self.is_valid_id(number):
                invalid_ids.append(number)
        return invalid_ids

    def is_valid_id(self, number):
        # Convert into string for easier digit manipulation
        num_str = str(number)

        # if the length is not even it is good
        if len(num_str) % 2 != 0:
            return True
        
        # Now divide into two halves and compare both to be same
        mid = len(num_str) // 2
        first_half = num_str[:mid]
        second_half = num_str[mid:]
        return first_half != second_half


    def is_valid_id2(self, number):
        # Convert into string for easier digit manipulation
        s = str(number)
        if not s:
            return False

        n = len(s)

        # Check every possible prefix length from 1 up to half the string length
        for prefix_length in range(1, n // 2 + 1):
            if n % prefix_length == 0:
                prefix = s[:prefix_length]
                repetitions = n // prefix_length
                if prefix * repetitions == s:
                    return True



# main function
def main():
    ranges = loadDataNew().split(",")

    print("\nPart 1")
    invalid_ids_list = []
    for data in ranges:
        finder = InvalidIDFinder(data)
        invalid_ids = finder.find_invalid_ids()
        invalid_ids_list.extend(invalid_ids)
    
    # Print the sum of invlalid ids list
    print(f"Sum of invalid IDs {sum(invalid_ids_list)}")   
    
    print("\nPart 2")
    invalid_ids_list = []
    for data in ranges:
        finder = InvalidIDFinder(data)
        invalid_ids = finder.find_invalid_ids2()
        invalid_ids_list.extend(invalid_ids)

    # Print the sum of invlalid ids list
    print(f"Sum of invalid IDs {sum(invalid_ids_list)}")   
   


# Call main
main()
