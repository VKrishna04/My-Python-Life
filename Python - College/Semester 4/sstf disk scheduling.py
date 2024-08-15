def sstf_disk_scheduling(requests, head):
    seek_sequence = []
    seek_count = 0
    current_position = head
    while requests:
        closest_index = min(
            range(len(requests)), key=lambda i: abs(requests[i] - current_position)
        )
        closest_request = requests.pop(closest_index)
        seek_sequence.append(closest_request)
        seek_count += abs(current_position - closest_request)
        current_position = closest_request
    return seek_sequence, seek_count


# Input from user
requests = list(map(int, input("Enter the disk requests (space-separated): ").split()))
initial_head = int(input("Enter the initial head position: "))

sequence, count = sstf_disk_scheduling(requests, initial_head)
print(f"Seek Sequence: {sequence}")
print(f"Total Seek Operations: {count}")
