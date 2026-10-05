checksum = 0

with open("checksum_practice_input.txt", "r") as input_file:
    with open("checksum_results.txt", "w") as output_file:
        for line in input_file:
            line = line.strip()

            if line:
                numbers = line.split()
                numbers = [int(number) for number in numbers]

                largest = max(numbers)
                smallest = min(numbers)

                difference = largest - smallest
                checksum += difference

                output_file.write(str(difference) + "\n")

        output_file.write(f"Checksum: {checksum}\n")

print(f"Checksum: {checksum}")