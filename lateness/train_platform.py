#Check how many platforms are require for given trains
# Q - There is aschedule of trains and we need to build a platforms on station so that no train will wait
from datetime import time

def minimum_platform(train_list):
    trains_schedule_dict = {}
    train_time_list = []
    start_time = {}
    end_time = {}
    platforms = [{}]


    for l,m,n in train_list:
        trains_schedule_dict[l] = (m,n)
        start_h,start_m  = map(int,m.split(':'))
        end_h,end_m  = map(int,n.split(':'))

        start_time[l] = time(start_h,start_m)
        end_time[l] = time(end_h,end_m)


    for key in trains_schedule_dict.keys():
        new_require = True
        done = False
        for pl in platforms:
            if done:
                break
            if not pl:
                pl[key] = end_time[key]
                new_require = False
                done = True
                break
            else:
                for k,v in pl.items():
                    if end_time[k]<start_time[key]:
                        pl.pop(k)
                        pl[key] = end_time[key]
                        new_require = False
                        done = True
                        break
                    else:
                        break
                
        if new_require:
            platforms.append({key:end_time[key]})

    print(f"trains_schedule_dict -- {trains_schedule_dict}")
    return len(platforms)




if __name__ == "__main__":
    train_list = [
        (1,'9:00','9:10'),(2,'9:40','12:00'),(3,'9:50','11:20'),(4,'11:00','11:30'),(5,'11:40','12:10'),(6,'12:05','19:00'),(7,'12:06','13:00'),(8,'13:05','14:00'),(9,'14:05','15:00'),(10,'18:00','20:00')
    ]
    print(minimum_platform(train_list)) 


