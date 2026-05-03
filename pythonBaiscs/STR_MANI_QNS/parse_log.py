def log_parser(log_file):
    count = 0
    try:
        with open(log_file, "r") as file:
            for line in file:
                if "ERROR" in line:
                    count += 1
                    print(f"ERROR in line : {line.strip()}")
        return count
    except FileNotFoundError:
        print(f"file not found")


error_count = log_parser("error.log")
print(f"TOTAL ERROR COUNT IS : {error_count}")
