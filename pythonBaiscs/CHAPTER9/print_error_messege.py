def print_error(log_file):
    with open(log_file, "r") as file:
        for line in file:
            if 'ERROR' in line:
                print(f"{line.strip()}")


print_error("file1.txt")
