def generate_name_pattern():
    name = "RISHNA"
    numbers = list(range(1, 8))  # A range for the numbers that will appear in the pattern.
    name_length = len(name)

    # Create the pattern for the top part (first half)
    for i in range(name_length):
        # Creating spaces before the characters to align
        spaces = ' ' * i
        # Create the substring of letters for this row
        substring = ' '.join(name[i:name_length])

        # Generate the numbers in reverse order for each row
        num_list = ' '.join(map(str, numbers[i:name_length - i]))
        
        # Print the current row
        print(f"{spaces}{substring} {num_list}")

    # Create the pattern for the bottom part (second half)
    for i in range(name_length - 2, -1, -1):
        spaces = ' ' * i
        substring = ' '.join(name[i:name_length])

        # Generate the numbers
        num_list = ' '.join(map(str, numbers[i:name_length - i]))

        # Print the current row
        print(f"{spaces}{substring} {num_list}")

# Call the function to print the pattern
generate_name_pattern()