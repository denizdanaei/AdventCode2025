# secret entrance
import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    return [line.strip() for line in lines]

def parse_instructions(file_path):
    """
    Parse the input file and return a list of tuples.
    Each tuple contains (direction, distance) where direction is 'L' or 'R'
    and distance is an integer.
    
    Example:
        Input file:
            L23
            R47
        Output:
            [('L', 23), ('R', 47)]
    """
    lines = read_input(file_path)
    result = []
    
    for line in lines:
        if line:  # Skip empty lines
            direction = line[0]  # First character ('L' or 'R')
            distance = int(line[1:])  # Rest of the line as integer
            result.append((direction, distance))
    
    return result


def decode_password(instructions, start_position=50):
    password = 0
    position = start_position
    
    for direction, distance in instructions:
        if direction == 'L':
            position -= distance
        elif direction == 'R':
            position += distance
        
        position %= 100  # Wrap around 0-99
        
        if position == 0:
            password += 1
    
    return password
    

def decode_password_click_zero(instructions, start_position=50):
    password = 0
    position = start_position
    
    for direction, distance in instructions:
        if direction == 'R':
            # Moving right: how many times do we pass through 0?
            new_position = position + distance
            password += new_position // 100
            position = new_position % 100
        else:  # direction == 'L'
            # Moving left: how many times do we pass through 0?
            # We only cross 0 if we start from a positive position and reach 0 or go negative
            if position > 0 and position - distance <= 0:
                # We crossed from positive to 0 or negative (through 0)
                # Count: 1 for the initial crossing + additional full circles
                new_position = position - distance
                password += (abs(new_position) // 100) + 1
            elif position == 0 and distance >= 100:
                # Special case: starting at 0, going left by 100+ steps
                # We pass through 0 after each full circle
                password += (distance - 1) // 100
            position = (position - distance) % 100
    
    return password
    

if __name__ == "__main__":
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, 'puzzle_input.txt')
    
    instructions = parse_instructions(input_file)

    password = decode_password_click_zero(instructions)
    print(f"Decoded password: {password}")