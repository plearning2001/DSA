#Check how many platforms are require for given trains

from datetime import time





train_list = [
    (1,'9:00','9:10'),(2,'9:40','12:00'),(3,'9:50','11:20'),(4,'11:00','11:30'),(5,'11:40','12:10'),(6,'12:05','19:00'),(7,'12:06','13:00'),(8,'13:05','14:00'),(9,'14:05','15:00'),(10,'18:00','20:00')
]
trains_schedule_dict = {}
train_time_list = []
start_time = {}
end_time = {}
platforms = [{}]


for l,m,n in train_list:
    trains_schedule_dict[l] = (m,n)
    start  = map(int,m.split(':'))

    start_time[l] = time(start)
    end_time[l] = time(end)


for key in trains_schedule_dict.keys():
    for pl in platforms:
        if not pl:
            pl[key] = end_time[key]


print(f"trains_schedule_dict -- {trains_schedule_dict}")
print(f"trains_time_list -- {train_time_list}")

