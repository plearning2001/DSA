
'''
meetings = [[0,30], [5,10], [15,20]]
meetings = sorted(meetings,key = lambda x:x[0])
new_list = [meetings[0]]

for curr_meet in meetings[1:]:

    prev_meet = new_list[-1]

    if prev_meet[1] > curr_meet[0]:
        new_list.append(curr_meet)

print(len(new_list))
'''



import heapq

def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x[0])
    heap = []

    for start, end in meetings:
        print(f"\nMeeting [{start},{end}]")
        print(f"  Heap before = {heap}")

        if heap and heap[0] <= start:
            freed = heapq.heappop(heap)
            print(f"  Room free! (was busy till {freed}) ♻️")

        heapq.heappush(heap, end)
        print(f"  Heap after  = {heap}")
        print(f"  Rooms used  = {len(heap)}")

    print(f"\n✅ Min rooms needed = {len(heap)}")
    return len(heap)

meetings = [[0,30],[5,10],[15,20]]
min_meeting_rooms(meetings)