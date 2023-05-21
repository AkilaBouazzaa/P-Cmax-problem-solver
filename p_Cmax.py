import random
from itertools import permutations
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator


# def pcmax(n1, m1, k):
#     n = int(n1)
#     m = int(m1)
#     #generate random processing times for the n given tasks  
#     pi = [random.randint(1, 1000) for _ in range(n)]
    
#     #assign each processing time to a task 
#     resultri = {f"T{i+1}": pi[i] for i in range(n)}
#     #sorts the items in  resultri by their values in descending order, then takes the first k items from the sorted list (last k items in BK) and creates a new dictionary AK containing those k items.

#     AK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[:k])
#     BK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[k:])
#     ak = list(AK.keys())
#     bk = list(BK.keys())
#     # generate all possible permutations of ak
#     All = list(permutations(ak))
#     abk=ak+bk
#     machines = [[] for _ in range(m)]
#     machinesTimes = [0] * m
    
#     BRUTTE = {}
#     for u in range(len(All)):
#         completion_times = [0] * m
#         c = 0
#         for i in All[u]:
#             completion_times[c] += AK[i]
#             c = (c + 1) % m
#         makespan = max(completion_times)
#         BRUTTE[u] = makespan
    
#     r = min(BRUTTE, key=BRUTTE.get)
#     PartSol = All[r]
    
#     for job in bk:
#         machine_index = min(range(len(machinesTimes)), key=machinesTimes.__getitem__)
#         machines[machine_index].append(job)
#         machinesTimes[machine_index] += BK[job]
   
#     #print(abk)
#     # print(machinesTimes)
#     # print(max(machinesTimes))
#     print("Optimal finish times for each machine:", machinesTimes)
#     print("Makespan:", max(machinesTimes) )
#     print("schedule:")
#     for i, assignments in enumerate(machines):
#             print("Machine", i+1, ":", assignments)

#     # with open("output.txt", "a") as f:
#     #     print("Optimal permutation:", machinesTimes , file=f)
#     #     print("Optimal cmax:", makespan , file=f)
#     #     print("Job assignments:", file=f)
#     #     for i, assignments in enumerate(machines):
#     #         print("Machine", i+1, ":", assignments, file=f)



    
#     plot_schedule(abk, machines,resultri)
#     return max(machinesTimes)
# # plot the gantt chart
# def plot_schedule(job, machines, pi):
#     num_tasks = len(job)
#     num_machines = len(machines)
    
#     # Create a list of colormaps
#     colormaps = ['ocean_r', 'viridis', 'plasma_r', 'inferno', 'twilight_r', 'hsv_r', 'PiYG_r']
    
#     plt.figure(figsize=(10, 5))
#     for m in range(num_machines):
#         y = num_machines - m
        
#         # Use a different colormap for each machine
#         colors = plt.get_cmap(colormaps[m % len(colormaps)])(range(num_tasks))
        
#         for i, task in enumerate(machines[m]):
#             x = pi[task]
#             plt.barh(y, x, left=sum([pi[t] for t in machines[m][:i]]), color=colors[job.index(task)], align='center', edgecolor='white')
#     plt.yticks(range(1, num_machines+1), ['Machine {}'.format(i) for i in range(1, num_machines+1)])
#     plt.xlabel('Time')
#     plt.ylabel('Machine')
#     plt.title('Optimal Job Schedule')
#     plt.show()
# # ask the user for the inputs
# n = int(input("Enter the number of jobs: "))
# m = int(input("Enter the number of machines: "))
# k = int(input("Enter k (<= 10): "))
# while k > 10:
#     print("Invalid number . Please enter a number k in [5..10].")
#     k = int(input("Enter k (<= 10): "))

# pcmax(n,m,k)

def job_scheduling_lpt(n1, m1, k):
    # Generate random processing times for each job
    P = {f'T{i}': random.randint(1, 1000) for i in range(1, n1 + 1)}

    # Order the processing times in descending order
    p_sorted = sorted(P.items(), key=lambda x: x[1], reverse=True)
    ak = [job for job, _ in p_sorted[:k]]

    # Find the corresponding jobs for ak
    opt_perm = ak

    # Initialize variables for storing the optimal permutation and its cmax
    opt_cmax = float('inf')
    opt_assignments = [[] for _ in range(m1)]  # list of job assignments for each machine
    kcmax = float('-inf')  # initialize kcmax with negative infinity

    # Assign the first k jobs optimally
    machine_times = [0] * m1
    assignments = [[] for _ in range(m1)]
    for job in opt_perm:
        min_machine = machine_times.index(min(machine_times))
        machine_times[min_machine] += P[job]
        assignments[min_machine].append(job)

    # Calculate cmax for the first k-job assignment
    kcmax = max(machine_times)

    # Remaining jobs (n - k) assignment using LPT algorithm
    remaining_jobs = p_sorted[k:]
    machine_times_remaining = machine_times.copy()
    assignments_remaining = assignments.copy()

    for job, time in remaining_jobs:
        min_machine = machine_times_remaining.index(min(machine_times_remaining))
        machine_times_remaining[min_machine] += time
        assignments_remaining[min_machine].append(job)

    # Calculate cmax for the complete assignment (n jobs)
    cmax = max(machine_times_remaining)
    opt_cmax = cmax

    # Format schedules in the format "Ti: Pi"
    optimal_schedule = [[f"{job}: {P[job]}" for job in machine_assignment] for machine_assignment in assignments_remaining]

    return opt_perm, optimal_schedule, opt_cmax, kcmax


def job_scheduling_lpt(n1, m1, k):
    # Generate random processing times for each job
    P = {f'T{i}': random.randint(1, 1000) for i in range(1, n1 + 1)}

    # Order the processing times in descending order
    p_sorted = sorted(P.items(), key=lambda x: x[1], reverse=True)
    ak = [job for job, _ in p_sorted[:k]]

    # Find the corresponding jobs for ak
    opt_perm = ak

    # Initialize variables for storing the optimal permutation and its cmax
    opt_cmax = float('inf')
    opt_assignments = [[] for _ in range(m1)]  # list of job assignments for each machine
    kcmax = float('-inf')  # initialize kcmax with negative infinity

    # Assign the first k jobs optimally
    machine_times = [0] * m1
    assignments = [[] for _ in range(m1)]
    for job in opt_perm:
        min_machine = machine_times.index(min(machine_times))
        machine_times[min_machine] += P[job]
        assignments[min_machine].append(job)

    # Calculate cmax for the first k-job assignment
    kcmax = max(machine_times)

    # Remaining jobs (n - k) assignment using LPT algorithm
    remaining_jobs = p_sorted[k:]
    machine_times_remaining = machine_times.copy()
    assignments_remaining = assignments.copy()

    for job, time in remaining_jobs:
        min_machine = machine_times_remaining.index(min(machine_times_remaining))
        machine_times_remaining[min_machine] += time
        assignments_remaining[min_machine].append(job)

    # Calculate cmax for the complete assignment (n jobs)
    cmax = max(machine_times_remaining)
    opt_cmax = cmax

    # Format schedules in the format "Ti: Pi"
    optimal_schedule = [[f"{job}: {P[job]}" for job in machine_assignment] for machine_assignment in assignments_remaining]

    # Plot the Gantt chart
    fig, ax = plt.subplots()
    for i, machine_assignment in enumerate(assignments_remaining):
        for j, job in enumerate(machine_assignment):
            start_time = sum(P[job] for job in machine_assignment[:j])
            ax.barh(i, P[job], left=start_time, height=0.5, align='center', alpha=0.8, label=job)
    
    ax.set_yticks(range(m1))
    ax.set_yticklabels([f'Machine {i}' for i in range(1, m1 + 1)])
    ax.set_xlabel('Time')
    ax.set_ylabel('Machine')
    ax.set_title('Gantt Chart - Job Scheduling')
    ax.grid(True)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
    
    return opt_perm, optimal_schedule, opt_cmax, kcmax
n1 = 10  # Number of jobs
m1 = 3   # Number of machines
k = 4    # Number of initial jobs to assign optimally

opt_perm, optimal_schedule, opt_cmax, kcmax = job_scheduling_lpt(n1, m1, k)
