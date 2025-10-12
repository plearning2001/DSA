#First create a Queue

class Queue():
  
  def __init__(self):
    self.queue = []
  
  def is_empty(self):
    return(self.queue == [])
  
  def enque(self,vertex):
    self.queue.append(vertex)
  
  def dequeue(self):
    v = None
    if not self.is_empty():
      v = self.queue[0]
      self.queue = self.queue[1:]
      print(f"Inside deque - {self.queue}")
    return(v)

  def get_queue(self):
    return(str(self.queue))


def bsf_algo(adj_list,start_node):
  visited_nodes = {}
  for key in adj_list:
    visited_nodes[key] = False
  print(f"Initial Visited nodes -- {visited_nodes}")
  
  queue = Queue()
  print(f"Empty queue -- {queue}")
  
  queue.enque(start_node)
  visited_nodes[start_node] = True  
  print(f"Visited nodes after start -- {visited_nodes}")

  while(not queue.is_empty()):
    print("Not empty")
    current_node = queue.dequeue()
    updated_queue = queue.get_queue()
    print(f"Updated queue -- {updated_queue}")


    adj_nodes = adj_list[current_node]
    
    for single_node in adj_nodes:
      if (not visited_nodes[single_node]):
        visited_nodes[single_node] = True
        queue.enque(single_node)
  
  
  return(visited_nodes)



adj_list = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

#Pass list and starting node
print(bsf_algo(adj_list,2))
