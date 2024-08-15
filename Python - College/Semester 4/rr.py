from math import ceil


def rr_scheduling(Processes, quantum):
    queue = []
    time = 0
    Processes = sorted(Processes, key=lambda x: x["arrival"])
    queue.append(Processes[0])
    Processes[0]["remaining"] = Processes[0]["burst"]
    Processes[0]["start"] = -1
    i = 1
    while queue:
        process = queue.pop(0)
        if process["start"] == -1:
            process["start"] = time
        if process["remaining"] > quantum:
            process["remaining"] -= quantum
            time += quantum
            while i < len(Processes) and Processes[i]["arrival"] <= time:
                Processes[i]["remaining"] = Processes[i]["burst"]
                Processes[i]["start"] = -1
                queue.append(Processes[i])
                i += 1
            queue.append(process)
        else:
            time += process["remaining"]
            process["remaining"] = 0
            process["completion"] = time
            while i < len(Processes) and Processes[i]["arrival"] <= time:
                Processes[i]["remaining"] = Processes[i]["burst"]
                Processes[i]["start"] = -1
                queue.append(Processes[i])
                i += 1
    return Processes


# Input from user
debug = True
Processes = [
    {"id": "P1", "arrival": 0, "burst": 5},
    {"id": "P2", "arrival": 1, "burst": 3},
    {"id": "P3", "arrival": 2, "burst": 2},
    {"id": "P4", "arrival": 3, "burst": 1},
    {"id": "P5", "arrival": 4, "burst": 4},
]
quantum = 3
if not debug:
    Processes = []
    n = int(input("Enter the number of Processes: "))
    for _ in range(n):
        pid = int(input("Enter process ID: "))
        arrival = int(input("Enter arrival time: "))
        burst = int(input("Enter burst time: "))
        Processes.append({"id": pid, "arrival": arrival, "burst": burst})
    quantum = int(input("Enter the quantum time: "))

else:
    # Calculate the LCM of all burst times for the quantum in debug mode
    burst_times = [process["burst"] for process in Processes]
    total_burst_time = sum(burst_times)
    average_burst_time = total_burst_time / len(Processes)
    quantum = ceil(average_burst_time)

scheduled_processes = rr_scheduling(Processes, quantum)
for process in scheduled_processes:
    print(
        f"Processes: {process['id']} - Start: {process['start']}, Completion: {process['completion']}"
    )
