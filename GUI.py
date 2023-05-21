# import tkinter as tk
# from tkinter import filedialog
# import matplotlib.pyplot as plt
# import random
# from itertools import permutations


# pi = []


   
#  # Generate processing times
# def generate_processing_times(n):
#     global pi
#     pi = [random.randint(1, 1000) for _ in range(n)]



# # Function to calculate makespan
# def ppcmax(n1, m1, k,pi):
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
   

    
#     makespan = max(machinesTimes)
#     return makespan
    
# # plot the gantt chart
# def plot_schedule(abk, machines, resultri):
#     num_tasks = len(abk)
#     num_machines = len(machines)
#     colors = plt.get_cmap('tab20')(range(num_tasks))
#     plt.figure(figsize=(10, 5))
#     for m in range(num_machines):
#         y = num_machines - m
#         for i, task in enumerate(machines[m]):
#             x = resultri[task]
#             plt.barh(y, resultri[task], left=sum([resultri[t] for t in machines[m][:i]]), color=colors[abk.index(task)], align='center', edgecolor='white')
#     plt.yticks(range(1, num_machines+1), ['Machine {}'.format(i) for i in range(1, num_machines+1)])
#     plt.xlabel('Time')
#     plt.ylabel('Machine')
#     plt.title('Optimal Job Schedule')

#     plt.show()
       
# # Function to print schedule to text file
# def print_schedule(pi):
#     n = int(n1_entry.get())
#     m = int(m1_entry.get())
#     k = int(k_entry.get())
    
#     resultri = {f"T{i + 1}": pi[i] for i in range(n)}
#     AK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[:k])
#     BK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[k:])
#     ak = list(AK.keys())
#     bk = list(BK.keys())
#     All = list(permutations(ak))
#     abk = ak + bk
#     machines = [[] for _ in range(m)]
#     machinesTimes = [0] * m

#     for job in bk:
#         machine_index = min(range(len(machinesTimes)), key=machinesTimes.__getitem__)
#         machines[machine_index].append(job)
#         machinesTimes[machine_index] += BK[job]

#     file_path = filedialog.asksaveasfilename(defaultextension=".txt")
#     with open(file_path, 'w') as f:
#         f.write("Optimal k permutation: {}\n".format(machinesTimes))
#         f.write("Job assignments:\n")
#         for i, assignments in enumerate(machines):
#             f.write("Machine {}: {}\n".format(i + 1, assignments))
#         makespan = pcmax(n, m, k)
#         f.write("Makespan: {}\n".format(makespan))
#     print("Schedule written to file.")


   



# def pcmax(n1, m1, k):
#     n = int(n1)
#     m = int(m1)
    
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
   

    
#     makespan = max(machinesTimes)
#     return makespan



# # Create GUI window
# root = tk.Tk()
# root.title("Makespan Calculator")

# # Add input fields
# n1_label = tk.Label(root, text="Jobs (n):")
# n1_label.grid(row=0, column=0)
# n1_entry = tk.Entry(root)
# n1_entry.grid(row=0, column=1)

# m1_label = tk.Label(root, text="Machines (m):")
# m1_label.grid(row=1, column=0)
# m1_entry = tk.Entry(root)
# m1_entry.grid(row=1, column=1)

# k_label = tk.Label(root, text="k:")
# k_label.grid(row=2, column=0)
# k_entry = tk.Entry(root)
# k_entry.grid(row=2, column=1)
 

# makespan_label = tk.Label(root, text="Makespan:")
# makespan_label.grid(row=4, column=0)

# makespan_value = tk.Label(root, text="")
# makespan_value.grid(row=4, column=1)


# calculate_button = tk.Button(root, text="Solve", command=lambda: calculate())
# calculate_button.grid(row=3, column=2)

# def calculate():
#     n = int(n1_entry.get())
#     generate_processing_times(n)
#     makespan = pcmax(n, int(m1_entry.get()), int(k_entry.get()))
#     makespan_value.config(text=str(makespan))
   






# calculate_button = tk.Button(root, text="Solve", command=lambda: calculate())
# print_button = tk.Button(root, text="Print Schedule to File", command=lambda: print_schedule(pi))
# calculate_button.grid(row=3, column=1)
# print_button.grid(row=3, column=2)


# plot_button = tk.Button(root, text="Plot Schedule", command=lambda: plot_schedule(abk, machines, resultri))

# plot_button.grid(row=3, column=3)


# # Start GUI event loop
# root.mainloop()

import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import random
import itertools
from itertools import permutations
import matplotlib.cm as cm



P={}
   
 # Generate processing times
def generate_processing_times(n):
    global P
    P = {f'T{i}': random.randint(1, 1000) for i in range(1, n + 1)}


    
  



def print_schedule():
    n = int(n1_entry.get())
    m = int(m1_entry.get())
    k = int(k_entry.get())

    machines = [[] for _ in range(m)]

    # Order the processing times in descending order
    P_sorted = sorted(P.items(), key=lambda x: x[1], reverse=True)
    ak = [job for job, _ in P_sorted[:k]]

    # Find the corresponding jobs for ak
    opt_perm = ak

    # Generate all possible permutations of ak
    perms = itertools.permutations(ak)

    # Initialize variables for storing the optimal permutation and its cmax
    opt_cmax = float('inf')
    opt_assignments = [[] for _ in range(m)]  # list of job assignments for each machine
    kcmax = float('-inf')  # initialize kcmax with negative infinity

    # Loop through each permutation
    for perm in perms:
        # Assign jobs to machines in order of the permutation
        machine_times = [0] * m  # current total processing time for each machine
        assignments = [[] for _ in range(m)]  # job assignments for each machine
        for job in perm:
            min_machine = machine_times.index(min(machine_times))
            machine_times[min_machine] += P[job]
            assignments[min_machine].append(job)

            # Calculate cmax for this permutation
            cmax = max(machine_times)

            # Check if this permutation is optimal
            if cmax < opt_cmax:
                opt_perm = perm
                opt_cmax = cmax
                opt_assignments = assignments
                kcmax = cmax  # update kcmax with the cmax of the k-job assignment

    # Remaining jobs (n - k) assignment using LPT algorithm
    remaining_jobs = P_sorted[k:]
    machine_times_remaining = [sum(P[job] for job in machine) for machine in opt_assignments]
    assignments_remaining = opt_assignments.copy()

    for job, _ in remaining_jobs:
        min_machine = machine_times_remaining.index(min(machine_times_remaining))
        machine_times_remaining[min_machine] += P[job]
        assignments_remaining[min_machine].append(job)

    # Format schedules in the format "Ti: Pi"
    optimal_schedule = [[f" {job}: {P[job]}" for job in machine_assignment] for machine_assignment in assignments_remaining]

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as f:
        f.write("Optimal k permutation: {}\n".format(opt_perm))
        f.write("Job assignments:\n")
        for i, machine_assignment in enumerate(optimal_schedule):
            f.write("Machine {}: {}\n".format(i+1, ", ".join(machine_assignment)))
        makespan = max(machine_times_remaining)
        f.write("Makespan: {}\n".format(makespan))
    print("Schedule written to file.")






def pcmax(n1, m1, k):
    
    n = int(n1_entry.get())
    m = int(m1_entry.get())
    k = int(k_entry.get())

   # Order the processing times in descending order
    p_sorted = sorted(P.values(), reverse=True)
    pk = p_sorted[:k]

    # Find the corresponding jobs for pk
    opt_perm = [job for job, time in P.items() if time in pk]

    # Generate all possible permutations of pk
    perms = itertools.permutations(pk)

    # Initialize variables for storing the optimal permutation and its cmax
    makespan= float('inf')
    opt_assignments = [[] for _ in range(m)]  # list of job assignments for each machine
    kcmax = float('-inf')  # initialize kcmax with negative infinity

    # Loop through each permutation
    for perm in perms:
        # Assign jobs to machines in order of the permutation
        machine_times = [0] * m  # current total processing time for each machine
        assignments = [[] for _ in range(m)]  # job assignments for each machine
        for job_time in perm:
            min_machine = machine_times.index(min(machine_times))
            machine_times[min_machine] += job_time
            assignments[min_machine].append(job_time)

            # Calculate cmax for this permutation
            cmax = max(machine_times)

            # Check if this permutation is optimal
            if cmax < makespan:
                opt_perm = [job for job, time in P.items() if time in perm]
                makespan = cmax
                opt_assignments = assignments
                kcmax = cmax  # update kcmax with the cmax of the k-job assignment
                #break

    # Remaining jobs (n - k) assignment using LPT algorithm
    remaining_jobs = p_sorted[k:]
    machine_times_remaining = [sum(machine) for machine in opt_assignments]
    assignments_remaining = opt_assignments.copy()

    for job_time in remaining_jobs:
        min_machine = machine_times_remaining.index(min(machine_times_remaining))
        machine_times_remaining[min_machine] += job_time
        assignments_remaining[min_machine].append(job_time)
    # Calculate cmax for the complete assignment (n jobs)
    C_max = max(machine_times_remaining)
    makespan = C_max
    # Format schedules in the format "Ti: Pi"
    optimal_schedule = []
    for machine_assignment in assignments_remaining:
        schedule = [job for job, time in P.items() for job_time in machine_assignment if time == job_time]
        optimal_schedule.append(schedule)
    return makespan
   


def plot_gantt_chart(assignments):
    fig, ax = plt.subplots(figsize=(10, 5))
    y_ticks = list(range(len(assignments)))
    y_labels = [f'Machine {i + 1}' for i in range(len(assignments))]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)

    num_tasks = sum(len(machine_assignment) for machine_assignment in assignments)
    colors = plt.get_cmap('tab20', num_tasks)
    

    current_task = 0

    for i, machine_assignment in enumerate(assignments):
        machine_color = plt.get_cmap('tab20')(i % 10)
        for j, job in enumerate(machine_assignment):
            start_time = sum(P[j] for j in machine_assignment[:j])
            end_time = start_time + P[job]
            plt.barh(i, end_time - start_time, left=start_time, height=0.5, color=colors(current_task), edgecolor='white')
            current_task += 1
    #plt.figure(figsize=(10, 5))
    plt.xlabel('Time')
    plt.ylabel('Machines')
    plt.title('Gantt Chart')
    plt.grid(axis='x')
    plt.show()
# # plot the gantt chart
# def plot_schedule(abk, machines, resultri):
#     num_tasks = len(abk)
#     num_machines = len(machines)
#     colors = plt.get_cmap('tab20')(range(num_tasks))
#     plt.figure(figsize=(10, 5))
#     for m in range(num_machines):
#         y = num_machines - m
#         for i, task in enumerate(machines[m]):
#             x = resultri[task]
#             plt.barh(y, resultri[task], left=sum([resultri[t] for t in machines[m][:i]]), color=colors[abk.index(task)], align='center', edgecolor='white')
#     plt.yticks(range(1, num_machines+1), ['Machine {}'.format(i) for i in range(1, num_machines+1)])
#     plt.xlabel('Time')
#     plt.ylabel('Machine')
#     plt.title('Optimal Job Schedule')

#     plt.show()

def ppcmax():
    n = int(n1_entry.get())
    m = int(m1_entry.get())
    k = int(k_entry.get())

    machines = [[] for _ in range(m)]

    # Order the processing times in descending order
    P_sorted = sorted(P.items(), key=lambda x: x[1], reverse=True)
    ak = [job for job, _ in P_sorted[:k]]

    # Find the corresponding jobs for ak
    opt_perm = ak

    # Generate all possible permutations of ak
    perms = itertools.permutations(ak)

    # Initialize variables for storing the optimal permutation and its cmax
    opt_cmax = float('inf')
    opt_assignments = [[] for _ in range(m)]  # list of job assignments for each machine
    kcmax = float('-inf')  # initialize kcmax with negative infinity

    # Loop through each permutation
    for perm in perms:
        # Assign jobs to machines in order of the permutation
        machine_times = [0] * m  # current total processing time for each machine
        assignments = [[] for _ in range(m)]  # job assignments for each machine
        for job in perm:
            min_machine = machine_times.index(min(machine_times))
            machine_times[min_machine] += P[job]
            assignments[min_machine].append(job)

            # Calculate cmax for this permutation
            cmax = max(machine_times)

            # Check if this permutation is optimal
            if cmax < opt_cmax:
                opt_perm = perm
                opt_cmax = cmax
                opt_assignments = assignments
                kcmax = cmax  # update kcmax with the cmax of the k-job assignment

    # Remaining jobs (n - k) assignment using LPT algorithm
    remaining_jobs = P_sorted[k:]
    machine_times_remaining = [sum(P[job] for job in machine) for machine in opt_assignments]
    assignments_remaining = opt_assignments.copy()

    for job, _ in remaining_jobs:
        min_machine = machine_times_remaining.index(min(machine_times_remaining))
        machine_times_remaining[min_machine] += P[job]
        assignments_remaining[min_machine].append(job)

    # Format schedules in the format "Ti: Pi"
    optimal_schedule = [[f" {job}: {P[job]}" for job in machine_assignment] for machine_assignment in
                        assignments_remaining]

    plot_gantt_chart(assignments_remaining)





    
    

  



# Create GUI window
root = tk.Tk()
root.title("P||Cmax solver")
root.configure(bg="#F7F9FA")

# Add input fields
n1_label = tk.Label(root, text="Jobs (n):", bg="#F7F9FA", font=("Arial", 12))
n1_label.grid(row=0, column=0, padx=10, pady=10)
n1_entry = tk.Entry(root, font=("Arial", 12))
n1_entry.grid(row=0, column=1, padx=10, pady=10)

m1_label = tk.Label(root, text="Machines (m):", bg="#F7F9FA", font=("Arial", 12))
m1_label.grid(row=1, column=0, padx=10, pady=10)
m1_entry = tk.Entry(root, font=("Arial", 12))
m1_entry.grid(row=1, column=1, padx=10, pady=10)

k_label = tk.Label(root, text="k(<=n):", bg="#F7F9FA", font=("Arial", 12))
k_label.grid(row=2, column=0, padx=10, pady=10)
k_entry = tk.Entry(root, font=("Arial", 12))
k_entry.grid(row=2, column=1, padx=10, pady=10)

makespan_label = tk.Label(root, text="Makespan:", bg="#F7F9FA", font=("Arial", 12))
makespan_label.grid(row=4, column=0, padx=10, pady=10)

makespan_value = tk.Label(root, text="", bg="#F7F9FA", font=("Arial", 12))
makespan_value.grid(row=4, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Solve", command=lambda: calculate(), relief=tk.RAISED, bg="#FFA500", fg="white", font=("Arial", 12), padx=10, pady=5, bd=0, borderwidth=0, highlightthickness=0, cursor="hand2")
calculate_button.grid(row=3, column=1, padx=10, pady=10)

print_button = tk.Button(root, text="Print Schedule to a text file", command=lambda: print_schedule(), relief=tk.RAISED, bg="#FF5733", fg="white", font=("Arial", 12), padx=10, pady=5, bd=0, borderwidth=0, highlightthickness=0, cursor="hand2")
print_button.grid(row=3, column=2, padx=10, pady=10)

plot_button = tk.Button(root, text="Plot Gantt chart", command=lambda: ppcmax(), relief=tk.RAISED, bg="#C70039", fg="white", font=("Arial", 12), padx=10, pady=5, bd=0, borderwidth=0, highlightthickness=0, cursor="hand2")
plot_button.grid(row=3, column=3, padx=10, pady=10)

def calculate():
    n = int(n1_entry.get())
    generate_processing_times(n)
    makespan = pcmax(n, int(m1_entry.get()), int(k_entry.get()))
    makespan_value.config(text=str(makespan))

# Start GUI event loop
root.mainloop()
