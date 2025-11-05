from operator import itemgetter


def total_delay(sorted_jobs):
    visited_jobs = {}
    total_time = 0
    max_delay = 0
    for p,q,r in sorted_jobs:
        visited_jobs[p] = 0
    for job,proc_tim,deadline in sorted_jobs:
        total_time = total_time + proc_tim
        buffer_time = deadline - total_time
        visited_jobs[job] = 1
        if deadline < total_time:
            max_delay = max_delay + (total_time-deadline)
            
    # print(f"max_delay -- {max_delay}")
    return max_delay

def minimize_lateness(jobs,N):

    sorted_jobs = sorted(jobs,key=itemgetter(1))
    
    for t in range(len(sorted_jobs)-1):
        if (sorted_jobs[t][2] == sorted_jobs[t+1][2]) and (sorted_jobs[t][1] > sorted_jobs[t+1][1]) :
            sorted_jobs[t],sorted_jobs[t+1] = sorted_jobs[t+1],sorted_jobs[t]
    #Delay with sort by process time
    old_delay_test = total_delay(sorted_jobs)

    buffer_data = {}
    visited_jobs = {}
    for p,q,r in sorted_jobs:
        buffer_data[p] = r-q
        visited_jobs[p] = 0
    print(f"buffer_data -- {buffer_data}")

    old_delay = total_delay(sorted_jobs)
    max_delay = old_delay
    for t in range(len(sorted_jobs)-1):
        sorted_jobs[t],sorted_jobs[t+1] = sorted_jobs[t+1],sorted_jobs[t]

        new_delay = total_delay(sorted_jobs)
        # new_delay = 137
        if new_delay > old_delay:
            sorted_jobs[t+1],sorted_jobs[t] = sorted_jobs[t],sorted_jobs[t+1]
        else:
            old_delay = new_delay
            # old_delay = 137


    return(max_delay,old_delay,sorted_jobs)

if __name__ == "__main__":

    jobs = [
        (0,10,15),
        (1,9,15),
        (2,2,10),
        (3,6,14),
        (4,5,6),
        (5,5,7),
        (6,2,6),
        (7,7,11),
        (8,3,5),
        (9,4,9)
    ]
    N = 2
    max_delay,min_delay,final_job_list = minimize_lateness(jobs,N)
    
    print(f"max_delay with fifo -- {max_delay}")
    print(f"min_delay -- {min_delay}")
    print(f"final_job_list -- {final_job_list}")

 