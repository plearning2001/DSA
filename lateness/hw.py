
'''
Added buffer to current tasks to check how delay get affect
'''

def check_completed_line(job,usedtime):
    job = job
    usedtime = usedtime
    for k in usedtime:
        if usedtime[k] == 0:
            return False
        if usedtime[k] + job[1] <= job[2]:
            print(f"availableeee in {k}")
            return str(k)


def minimizeLateness(N, jobs):
    sortedL = sorted(jobs, key=lambda x:(x[2], x[1], x[0]))
    print(sortedL)

    optimum = [ [] for i in range(N) ]
    print(f"optimum --{optimum}")
    usedtime = { i:0 for i in range(N) }
    print(f"usedtime --{usedtime}")
    i = 0
    delay = 0
    while i < len(sortedL):
        used_line = check_completed_line(sortedL[i],usedtime)
        if used_line != False:
            freeline = int(used_line)
        else:
            freeline = min(usedtime, key=lambda x:usedtime[x])
        print(f"freeline --{freeline}")
        optimum[freeline].append(sortedL[i][0])
        print(f"optimum --{optimum}")
        usedtime[freeline] += sortedL[i][1]
        print(f"usedtime --{usedtime}\n")
        buf2 = usedtime[freeline] - sortedL[i][2]
        if buf2 < 0:
            buf2=0
        else:
            buf2=buf2
        delay = delay+buf2
        i += 1
    print(f"Total-delay with No buffer -- {delay}")
    sum = 0
    for k in range(len(sortedL)):
        buf = (sortedL[k][1] - sortedL[k][2])
        if buf < 0:
            buf = 0
        sum = sum + buf
        
    print(f"+++ {sum}")
    return optimum

jobs_old = [
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
N = 11
jobs = []
for p,q,r in jobs_old:
    jobs.append((p,q,r))
    
print(minimizeLateness(N, jobs))