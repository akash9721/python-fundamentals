def print_by_http_status(nginx_log, status):
    with open(nginx_log, "r") as file:
        for line in file:
            parts = line.split('"')
            if len(parts) >= 2:
                request_string = parts[1]
                if request_string.startswith(status):
                    print(f"{parts[1]}")


print_by_http_status("nginx_log", "POST")
