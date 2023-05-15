import random
from itertools import permutations
import matplotlib.pyplot as plt


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
   
    #print(abk)
    # print(machinesTimes)
    # print(max(machinesTimes))
    print("Optimal finish times for each machine:", machinesTimes)
    print("Makespan:", max(machinesTimes) )
    print("schedule:")
    for i, assignments in enumerate(machines):
            print("Machine", i+1, ":", assignments)

    # with open("output.txt", "a") as f:
    #     print("Optimal permutation:", machinesTimes , file=f)
    #     print("Optimal cmax:", makespan , file=f)
    #     print("Job assignments:", file=f)
    #     for i, assignments in enumerate(machines):
    #         print("Machine", i+1, ":", assignments, file=f)



    
    plot_schedule(abk, machines,resultri)
    return max(machinesTimes)
# plot the gantt chart
def plot_schedule(job, machines, pi):
    num_tasks = len(job)
    num_machines = len(machines)
    
    # Create a list of colormaps
    colormaps = ['ocean_r', 'viridis', 'plasma_r', 'inferno', 'twilight_r', 'hsv_r', 'PiYG_r']
    
    plt.figure(figsize=(10, 5))
    for m in range(num_machines):
        y = num_machines - m
        
        # Use a different colormap for each machine
        colors = plt.get_cmap(colormaps[m % len(colormaps)])(range(num_tasks))
        
        for i, task in enumerate(machines[m]):
            x = pi[task]
            plt.barh(y, x, left=sum([pi[t] for t in machines[m][:i]]), color=colors[job.index(task)], align='center', edgecolor='white')
    plt.yticks(range(1, num_machines+1), ['Machine {}'.format(i) for i in range(1, num_machines+1)])
    plt.xlabel('Time')
    plt.ylabel('Machine')
    plt.title('Optimal Job Schedule')
    plt.show()
# ask the user for the inputs
n = int(input("Enter the number of jobs: "))
m = int(input("Enter the number of machines: "))
k = int(input("Enter k (<= 10): "))
while k > 10:
    print("Invalid number . Please enter a number k in [5..10].")
    k = int(input("Enter k (<= 10): "))

pcmax(n,m,k)


