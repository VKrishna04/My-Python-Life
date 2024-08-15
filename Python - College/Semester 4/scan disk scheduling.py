def scan_disk_scheduling(requests, head, disk_size):
    seek_sequence = []
    seek_count = 0
    direction = "left"

    requests.append(head)
    requests.append(0)
    requests.append(disk_size - 1)
    requests.sort()

    head_index = requests.index(head)

    if direction == "left":
        for i in range(head_index, -1, -1):
            seek_sequence.append(requests[i])
            if i > 0:
                seek_count += abs(requests[i] - requests[i - 1])
        for i in range(head_index + 1, len(requests)):
            seek_sequence.append(requests[i])
            if i < len(requests) - 1:
                seek_count += abs(requests[i] - requests[i + 1])
    else:
        for i in range(head_index, len(requests)):
            seek_sequence.append(requests[i])
            if i < len(requests) - 1:
                seek_count += abs(requests[i] - requests[i + 1])
        for i in range(head_index - 1, -1, -1):
            seek_sequence.append(requests[i])
            if i > 0:
                seek_count += abs(requests[i] - requests[i - 1])

    return seek_sequence, seek_count


# Input from user
requests = list(map(int, input("Enter the disk requests (space-separated): ").split()))
initial_head = int(input("Enter the initial head position: "))
disk_size = int(input("Enter the disk size: "))

sequence, count = scan_disk_scheduling(requests, initial_head, disk_size)
print(f"Seek Sequence: {sequence}")
print(f"Total Seek Operations: {count}")
