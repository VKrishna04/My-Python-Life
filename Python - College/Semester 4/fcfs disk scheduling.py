def fcfs_disk_scheduling(requests, head):
    seek_sequence = []
    seek_count = 0
    current_position = head

    for request in requests:
        seek_sequence.append(request)
        seek_count += abs(current_position - request)
        current_position = request

    return seek_sequence, seek_count


# Input from user
requests = list(map(int, input("Enter the disk requests (space-separated): ").split()))
initial_head = int(input("Enter the initial head position: "))

sequence, count = fcfs_disk_scheduling(requests, initial_head)
print(f"Seek Sequence: {sequence}")
print(f"Total Seek Operations: {count}")
