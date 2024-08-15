def priority_scheduling(processes):
    time = 0
    gantt = []
    completed_processes = []
    burst_times = {p["id"]: p["burst"] for p in processes}

    # Sort processes by arrival time first, then by priority
    processes = sorted(processes, key=lambda x: (x["arrival"], x["priority"]))

    while processes:
        # Get the processes that have arrived by the current time
        available_processes = [p for p in processes if p["arrival"] <= time]

        if not available_processes:
            # If no process has arrived, increment time
            gantt.append("Idle")
            time += 1
            continue

        # Select the process with the highest priority (smallest priority number)
        process = min(available_processes, key=lambda x: x["priority"])

        # Remove the selected process from the list
        processes.remove(process)

        # Simulate the process execution
        gantt.append(process["id"])
        time += process["burst"]
        process["completion"] = time
        process["turnaround"] = time - process["arrival"]
        process["waiting"] = process["turnaround"] - burst_times[process["id"]]
        completed_processes.append(process)

    return completed_processes, gantt


# Input from user
n = int(input("Enter the number of processes: "))
processes = []
for _ in range(n):
    pid = int(input("Enter process ID: "))
    arrival = int(input("Enter arrival time: "))
    burst = int(input("Enter burst time: "))
    priority = int(input("Enter priority: "))
    processes.append(
        {"id": pid, "arrival": arrival, "burst": burst, "priority": priority}
    )

scheduled_processes, gantt_chart = priority_scheduling(processes)

print("\nGantt Chart:")
print(" -> ".join(map(str, gantt_chart)))

print("\nProcess details:")
for process in scheduled_processes:
    print(
        f"Process {process['id']} - Arrival: {process['arrival']}, Burst: {process['burst']}, Priority: {process['priority']}, Completion: {process['completion']}, Turnaround: {process['turnaround']}, Waiting: {process['waiting']}"
    )

# Calculate average turnaround and waiting times
avg_turnaround = sum(p["turnaround"] for p in scheduled_processes) / n
avg_waiting = sum(p["waiting"] for p in scheduled_processes) / n

print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
print(f"Average Waiting Time: {avg_waiting:.2f}")
