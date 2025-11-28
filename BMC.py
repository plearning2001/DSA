'''
        if actual_values[i] and predicted_values[i]:
            TP += 1
        elif actual_values[i] and predicted_values[i] == 0:
            FN += 1
        elif actual_values[i] ==0 and predicted_values[i]:
            FP += 1        
        elif actual_values[i] ==0 and predicted_values[i] == 0:
            TN += 1    
'''


def get_positive_patients(threashold,prob_isolate_map):
    # TP + FP
    positives = 0
    for i in prob_isolate_map.keys():
        if threashold <= prob_isolate_map[i]:
            positives += 1
    return positives

prob_isolate = [0.931,0.646,0.982,0.690,0.269,0.957,0.668]
threashold = 0.3
bed_capacity = 6

prob_isolate_map = {
    "a":0.931,
    "b":0.646,
    "c":0.982,
    "d":0.690,
    "e":0.269,
    "f":0.957,
    "g":0.668
}
actual_values = {
    "a":1,
    "b":0,
    "c":1,
    "d":0,
    "e":0,
    "f":1,
    "g":1
}
TP = 0
TN = 0
FP = 0
FN = 0
predicted_values = {}


old_threashold = None
while True:
    positive_patients = get_positive_patients(threashold,prob_isolate_map)
    
    if bed_capacity<positive_patients:
        if old_threashold:
            print(f"Minimum threashould should be -- {old_threashold}.")
        else:
            print(f"Threashold {threashold} is very high.")
        break
    old_threashold = threashold
    threashold = round(old_threashold - 0.1,1)