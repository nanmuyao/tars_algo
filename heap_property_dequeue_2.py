# encoding='utf-8'

class MaxHeap:
    heap = []

    @staticmethod
    def insert(num):
        MaxHeap.heap.append(num)
        MaxHeap.shift_up()

    @staticmethod
    def shift_up():
        current_id = len(MaxHeap.heap) - 1
        parent_id = (current_id - 1)//2
        while current_id > 0:
            if MaxHeap.heap[parent_id] >= MaxHeap.heap[current_id]:
                break
            else:
                MaxHeap.heap[parent_id], MaxHeap.heap[current_id] = MaxHeap.heap[current_id], MaxHeap.heap[parent_id]
                current_id = parent_id
                parent_id = (current_id - 1)//2

    @staticmethod
    def delate(num):
        if num == MaxHeap.heap[-1]:
            MaxHeap.heap.pop() 
            return
        temp = MaxHeap.heap.pop()

        ind = MaxHeap.heap.index(num)
        MaxHeap.heap[ind] = temp
        MaxHeap.shift_down(ind)

    @staticmethod
    def shift_down(ind):
        current_id = ind
        child_id_left = current_id * 2 + 1
        child_id_right = current_id * 2 + 2
        while current_id < len(MaxHeap.heap) - 1:
            # �����ǰ�ڵ�ΪҶ�ӽڵ㣬shift_down���
            if current_id * 2 + 1 > len(MaxHeap.heap) - 1:
                break
            # ????????????????????????
            if current_id * 2 + 1 == len(MaxHeap.heap) - 1:
                if MaxHeap.heap[current_id] > MaxHeap.heap[-1]:
                    break
                else:
                    MaxHeap.heap[current_id], MaxHeap.heap[-1] = MaxHeap.heap[-1], MaxHeap.heap[current_id]
                    break
            # ?????????????????????????
            if MaxHeap.heap[current_id] > max(MaxHeap.heap[child_id_left], MaxHeap.heap[child_id_right]):
                break
            else:
                if MaxHeap.heap[child_id_right] > MaxHeap.heap[child_id_left]:
                    MaxHeap.heap[child_id_right], MaxHeap.heap[current_id] = MaxHeap.heap[current_id], MaxHeap.heap[child_id_right]
                    current_id = child_id_right
                    child_id_left = current_id * 2 + 1
                    child_id_right = current_id * 2 + 2
                else:
                    MaxHeap.heap[child_id_left], MaxHeap.heap[current_id] = MaxHeap.heap[current_id], MaxHeap.heap[child_id_left]
                    current_id = child_id_left
                    child_id_left = current_id * 2 + 1
                    child_id_right = current_id * 2 + 2

    @staticmethod
    def extract_max():
        num = MaxHeap.heap[0]
        try:
            MaxHeap.delate(num)
            return num
        except:
            return num

    @staticmethod
    def heap_sort(arr):
        for n in arr:
            MaxHeap.insert(n)
        for i in range(len(arr)):
            arr[i] = MaxHeap.extract_max()

    @staticmethod
    def heapify(arr):
        MaxHeap.heap = arr
        n = (len(arr) - 1)//2
        while n >= 0:
            MaxHeap.shift_down(n)
            n -= 1

    @staticmethod
    def heap_sort2(arr):
        MaxHeap.heapify(arr)
        res = []
        for i in range(len(arr)):
            res.append(MaxHeap.extract_max())
        return res


if __name__ == "__main__":
    h = MaxHeap()
    arr = [90,85,70,60,80,30,20,10,50,40]
    MaxHeap.heap_sort(arr)
    print(arr)
    
    arr = [90,85,70,60,80,30,20,10,50,40]
    arr = MaxHeap.heap_sort2(arr)
    print(arr)
