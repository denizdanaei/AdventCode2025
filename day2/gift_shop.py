import os


def read_file(filename):
    """
    Reads a file and parses the content into a list split by commas.
    
    Args:
        filename: Path to the file to read
        
    Returns:
        List of strings parsed by comma delimiter
    """
    with open(filename, 'r') as f:
        content = f.read().strip()
        return [item.strip() for item in content.split(',')]


def parse_range(range_string):
    """
    Parses a string with dash delimiter into two integers.
    
    Args:
        range_string: String in format "num1-num2" (e.g., "11-22")
        
    Returns:
        Tuple of two integers (num1, num2)
    """
    parts = range_string.split('-')
    return int(parts[0]), int(parts[1])


def find_mirrored_numbers(range_string):
    """
    Finds all mirrored numbers within a given range using mathematical pattern generation.
    
    Args:
        range_string: String in format "num1-num2" (e.g., "11-22")
        
    Returns:
        List of integers that have mirrored halves when converted to strings
    """
    start, end = parse_range(range_string)
    mirrored = []
    
    num_digits_start = len(str(start))
    num_digits_end = len(str(end))
    
    for total_digits in range(num_digits_start, num_digits_end + 1):
        if total_digits % 2 != 0:
            continue
        
        half_digits = total_digits // 2
        
        for pattern in range(10**(half_digits-1), 10**half_digits):
            candidate = int(str(pattern) * 2)
            
            if start <= candidate <= end:
                mirrored.append(candidate)
    
    return mirrored


def find_repeated_pattern_numbers(range_string):
    """
    Finds all numbers within a range that consist of a repeated pattern.
    Pattern can be repeated 2, 3, 4, or more times depending on the length.
    
    Args:
        range_string: String in format "num1-num2" (e.g., "95-115")
        
    Returns:
        List of integers made of repeated patterns (e.g., 99=9*2, 111=1*3)
    """
    start, end = parse_range(range_string)
    repeated = []
    
    num_digits_start = len(str(start))
    num_digits_end = len(str(end))
    
    for total_digits in range(num_digits_start, num_digits_end + 1):
        for pattern_length in range(1, total_digits):
            if total_digits % pattern_length != 0:
                continue
            
            repetitions = total_digits // pattern_length
            
            for pattern in range(10**(pattern_length-1), 10**pattern_length):
                candidate = int(str(pattern) * repetitions)
                
                if start <= candidate <= end:
                    repeated.append(candidate)
    
    return sorted(set(repeated))


def main():
    """Main function to read input.txt and find mirrored numbers for each range."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, 'input.txt')
    items = read_file(input_file)
    
    all_mirrored = []
    for item in items:
        mirrored = find_mirrored_numbers(item)
        all_mirrored.extend(mirrored)
    

    print(f"\nSum of mirrored numbers from part one: {sum(all_mirrored)}")
    
    
    all_repeated = []
    for item in items:
        repeated = find_repeated_pattern_numbers(item)
        all_repeated.extend(repeated)
    
    print(f"\nSum of mirrored numbers from part two: {sum(all_repeated)}")


if __name__ == '__main__':
    main()
