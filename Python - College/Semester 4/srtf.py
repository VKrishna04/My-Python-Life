def sjf_preemptive(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort processes by arrival time

    remaining_time = [proc[2] for proc in processes]  # Remaining burst times
    complete = 0
    t = 0
    minm = float("inf")
    shortest = 0
    check = False

    waiting_time = [0] * n
    turnaround_time = [0] * n

    while complete != n:
        for j in range(n):
            if (
                processes[j][1] <= t
                and remaining_time[j] < minm
                and remaining_time[j] > 0
            ):
                minm = remaining_time[j]
                shortest = j
                check = True

        if not check:
            t += 1
            continue

        remaining_time[shortest] -= 1
        minm = remaining_time[shortest]
        if minm == 0:
            minm = float("inf")

        if remaining_time[shortest] == 0:
            complete += 1
            check = False
            finish_time = t + 1
            waiting_time[shortest] = (
                finish_time - processes[shortest][2] - processes[shortest][1]
            )
            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0

        t += 1

    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]

    average_waiting_time = sum(waiting_time) / n
    average_turnaround_time = sum(turnaround_time) / n

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(
            f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}"
        )

    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")


# Example list of processes with their IDs, arrival times, and burst times
Processes = [
    ("P1", 0, 5),  # Process 1 arrives at time 0 and has a burst time of 5
    ("P2", 1, 3),  # Process 2 arrives at time 1 and has a burst time of 3
    ("P3", 2, 2),  # Process 3 arrives at time 2 and has a burst time of 2
    ("P4", 3, 1),  # Process 4 arrives at time 3 and has a burst time of 1
    ("P5", 4, 4),  # Process 5 arrives at time 4 and has a burst time of 4
]
sjf_preemptive(Processes)
