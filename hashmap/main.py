from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for x in range(self.array_size)]
    
  def compress(self, hash_value):
    return hash_value % self.array_size
  
  def hash(self, key):
    return sum(key.encode())
  
  def assign(self, key, value):
    index_value = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[index_value]
    for x in list_at_array:
      if x[0] == key:
        x[1] = value
    list_at_array.insert(payload)
  
  def retrieve(self, key):
    index_value = self.compress(self.hash(key))
    list_at_index = self.array[index_value]

    for x in list_at_index:
      if x[0] == key:
        return x[1]
      
    return None
        
blossom = HashMap(len(flower_definitions))
for value in flower_definitions:
  blossom.assign(value[0], value[1])

print(blossom.retrieve('poppy'))
