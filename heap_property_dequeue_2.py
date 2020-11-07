class MaxHeap:
    heap = [90,80,70,60,40,30,20,10,50]
 
    @staticmethod
    def insert(num):
        MaxHeap.heap.append(num)
        MaxHeap.shift_up()
        print(MaxHeap.heap)
        
    @staticmethod
    def shift_up():
        current_id = len(MaxHeap.heap) - 1
        parent_id = (current_id - 1)//2
        while current_id > 0:
            if MaxHeap.heap[parent_id] >= MaxHeap.heap[current_id]:
                break
            else:
                MaxHeap.heap[parent_id], MaxHeap.heap[current_id] = \
                    MaxHeap.heap[current_id], MaxHeap.heap[parent_id]
                current_id = parent_id
                parent_id = (current_id -1)//2
                
if __name__ == "__main__":
    h = MaxHeap()
    h.insert(85)