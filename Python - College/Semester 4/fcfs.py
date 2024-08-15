def fcfs(debug) -> None:
    # Declaring all the necessary values
    Processes = []
    i = 0
    # Inputs Arrival time and Burst time
    if debug:
        Processes = [
            ("P1", 0, 5),  # Process 1 arrives at time 0 and has a burst time of 5
            ("P2", 1, 3),  # Process 2 arrives at time 1 and has a burst time of 3
            ("P3", 2, 2),  # Process 3 arrives at time 2 and has a burst time of 2
            ("P4", 3, 1),  # Process 4 arrives at time 3 and has a burst time of 1
            ("P5", 4, 4),  # Process 5 arrives at time 4 and has a burst time of 4
        ]
        i = len(Processes)
    else:
        while True:
            i += 1
            arr_time = input(f"Arrival Time for {i+1}th process: ")
            if arr_time == "":
                break
            arr_time = int(arr_time)
            burst_time = int(input(f"Burst Time for {i+1}th process: "))
            Processes.append([f"P{i+1}", arr_time, burst_time])
    print(f"Number of Processes : {i}")

    temp_list = Processes.copy()
    Gantt_Chart = []
    current_time = 0
    total_time = 0

    print("Name, AT, BT, CT, TAT, WT")

    # FCFS - First Come First Serve
    while temp_list:
        # Logic Implementation
        least_arrival_time = min(temp_list, key=lambda process: process[1])
        current_time += least_arrival_time[2]
        Gantt_Chart.append((least_arrival_time[0], current_time))
        temp_list.remove(least_arrival_time)

        # Compute the necessary values -> Completion time, Turn Around time, Waiting time
        CT = current_time
        TAT = CT - least_arrival_time[1]
        WT = TAT - least_arrival_time[2]
        index = Processes.index(least_arrival_time)
        Processes[index] = (
            *least_arrival_time,
            CT,
            TAT,
            WT,
        )
        total_time += least_arrival_time[2]
        print(Processes[index])

    # Outputs -> Gantt Chart, Avg TAT, Avg WT
    print("\nGantt Chart :")
    print(Gantt_Chart)

    Avg_TAT = sum(process[-2] for process in Processes) / i
    Avg_WT = sum(process[-1] for process in Processes) / i
    print(f"Average Turn Around Time : {Avg_TAT}\nAverage Waiting Time     : {Avg_WT}")


if __name__ == "__main__":
    debug = True
    fcfs(debug)
