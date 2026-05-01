def count_error(file):
    try:
        count = 0
        with open(file, "r") as errorFile:
            for line in errorFile:
                if "ERROR" in line:
                    count += 1
                    print(f" found error in line {line}")
        return count
    except FileNotFoundError:
        print("file not found")
    except PermissionError:
        print("No read permission")


error_count = count_error("file1.txt")
print(f"total error count is : {error_count}")
