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

        print(f"start_times -- {start_time}")
        print(f"end_times -- {end_time}")
        # print(f"platforms -- {platforms}")



    for key in trains_schedule_dict.keys():
        print(f"platforms -- {platforms}")
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
                    if end_time[k]<=start_time[key]:
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
    train_list = [(1,'09:00','13:10'),(2,'09:40','12:00'),(3,'09:50','12:20'),(4,'11:00','11:50'),(5,'11:40','12:10')]

    print(f"Total platforms -- {minimum_platform(train_list)}") 


