import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import random
from itertools import permutations


# Function to calculate makespan
def ppcmax(n1, m1, k):
    n = int(n1)
    m = int(m1)
    #generate random processing times for the n given tasks  
    pi = [random.randint(1, 1000) for _ in range(n)]
    
    #assign each processing time to a task 
    resultri = {f"T{i+1}": pi[i] for i in range(n)}
    #sorts the items in  resultri by their values in descending order, then takes the first k items from the sorted list (last k items in BK) and creates a new dictionary AK containing those k items.

    AK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[:k])
    BK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[k:])
    ak = list(AK.keys())
    bk = list(BK.keys())
    # generate all possible permutations of ak
    All = list(permutations(ak))
    abk=ak+bk
    machines = [[] for _ in range(m)]
    machinesTimes = [0] * m
    
    BRUTTE = {}
    for u in range(len(All)):
        completion_times = [0] * m
        c = 0
        for i in All[u]:
            completion_times[c] += AK[i]
            c = (c + 1) % m
        makespan = max(completion_times)
        BRUTTE[u] = makespan
    
    r = min(BRUTTE, key=BRUTTE.get)
    PartSol = All[r]
    
    for job in bk:
        machine_index = min(range(len(machinesTimes)), key=machinesTimes.__getitem__)
        machines[machine_index].append(job)
        machinesTimes[machine_index] += BK[job]
   

    plot_schedule(abk, machines,resultri)
    makespan = max(machinesTimes)
    return makespan
    
# plot the gantt chart
def plot_schedule(abk, machines, resultri):
    num_tasks = len(abk)
    num_machines = len(machines)
    colors = plt.get_cmap('tab20')(range(num_tasks))
    plt.figure(figsize=(10, 5))
    for m in range(num_machines):
        y = num_machines - m
        for i, task in enumerate(machines[m]):
            x = resultri[task]
            plt.barh(y, x, left=sum([resultri[t] for t in machines[m][:i]]), color=colors[abk.index(task)], align='center', edgecolor='white')
    plt.yticks(range(1, num_machines+1), ['Machine {}'.format(i) for i in range(1, num_machines+1)])
    plt.xlabel('Time')
    plt.ylabel('Machine')
    plt.title('Optimal Job Schedule')
    plt.show()
       
# Function to print schedule to text file

     
def print_schedule(n1, m1, k):
    n = int(n1)
    m = int(m1)
    pi = [random.randint(1, 1000) for _ in range(n)]
    resultri = {f"T{i + 1}": pi[i] for i in range(n)}
    AK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[:k])
    BK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[k:])
    ak = list(AK.keys())
    bk = list(BK.keys())
    All = list(permutations(ak))
    abk = ak + bk
    machines = [[] for _ in range(m)]
    machinesTimes = [0] * m

    for job in bk:
        machine_index = min(range(len(machinesTimes)), key=machinesTimes.__getitem__)
        machines[machine_index].append(job)
        machinesTimes[machine_index] += BK[job]

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as f:
        f.write("Optimal k permutation: {}\n".format(machinesTimes))
        
        f.write("Job assignments:\n")
        for i, assignments in enumerate(machines):
            f.write("Machine {}: {}\n".format(i + 1, assignments))
        cmax = max(machinesTimes)
        f.write("makespan: {}\n".format(pcmax(n1, m1, k)))


        f.close()


def pcmax(n1, m1, k):
    n = int(n1)
    m = int(m1)
    #generate random processing times for the n given tasks  
    pi = [random.randint(1, 1000) for _ in range(n)]
    
    #assign each processing time to a task 
    resultri = {f"T{i+1}": pi[i] for i in range(n)}
    #sorts the items in  resultri by their values in descending order, then takes the first k items from the sorted list (last k items in BK) and creates a new dictionary AK containing those k items.

    AK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[:k])
    BK = dict(sorted(resultri.items(), key=lambda item: item[1], reverse=True)[k:])
    ak = list(AK.keys())
    bk = list(BK.keys())
    # generate all possible permutations of ak
    All = list(permutations(ak))
    abk=ak+bk
    machines = [[] for _ in range(m)]
    machinesTimes = [0] * m
    
    BRUTTE = {}
    for u in range(len(All)):
        completion_times = [0] * m
        c = 0
        for i in All[u]:
            completion_times[c] += AK[i]
            c = (c + 1) % m
        makespan = max(completion_times)
        BRUTTE[u] = makespan
    
    r = min(BRUTTE, key=BRUTTE.get)
    PartSol = All[r]
    
    for job in bk:
        machine_index = min(range(len(machinesTimes)), key=machinesTimes.__getitem__)
        machines[machine_index].append(job)
        machinesTimes[machine_index] += BK[job]
   

    
    makespan = max(machinesTimes)
    return makespan



# Create GUI window
root = tk.Tk()
root.title("Makespan Calculator")

# Add input fields
n1_label = tk.Label(root, text="Jobs (n):")
n1_label.grid(row=0, column=0)
n1_entry = tk.Entry(root)
n1_entry.grid(row=0, column=1)

m1_label = tk.Label(root, text="Machines (m):")
m1_label.grid(row=1, column=0)
m1_entry = tk.Entry(root)
m1_entry.grid(row=1, column=1)

k_label = tk.Label(root, text="k:")
k_label.grid(row=2, column=0)
k_entry = tk.Entry(root)
k_entry.grid(row=2, column=1)
 

makespan_label = tk.Label(root, text="Makespan:")
makespan_label.grid(row=4, column=0)

makespan_value = tk.Label(root, text="")
makespan_value.grid(row=4, column=1)


calculate_button = tk.Button(root, text="Solve", command=lambda: calculate())
calculate_button.grid(row=3, column=2)

def calculate():
    makespan = pcmax(int(n1_entry.get()), int(m1_entry.get()), int(k_entry.get()))
    makespan_value.config(text=str(makespan))


print_button = tk.Button(root, text="Print Schedule to File",
                          command=lambda: print_schedule(int(n1_entry.get()),
                                                         int(m1_entry.get()),
                                                         int(k_entry.get())))
print_button.grid(row=3, column=1)


plot_button = tk.Button(root, text="Plot Schedule",
                         command=lambda: ppcmax(int(n1_entry.get()),
                                                                 int(m1_entry.get()),
                                                                 int(k_entry.get())))
plot_button.grid(row=3, column=3)

# Start GUI event loop
root.mainloop()