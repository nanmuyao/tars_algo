# encoding="utf-8"

class Heap:
    def __init__(self):
        self.stack = [90,85,70,60,80,30,20,10,50,40]

    def insert(self, num):
        self.stack.append(num)
        self.shift_up()
        print(self.stack)

    def shift_up(self):
        stack = self.stack
        current_index = len(self.stack) - 1
        parent_index = (current_index) // 2
        while current_index > 0:
            if stack[parent_index] >= stack[current_index]:
                break
            else:
                stack[parent_index], stack[current_index] = \
                    stack[current_index], stack[parent_index]
                # 这里要把两个指针移动起来
                current_index = parent_index
                # 索引为i的父节点索引为（i-1）//2
                parent_index = (current_index - 1) // 2

    def d(self):
        value = self.pop()
        self.shift_down()
        return value

    def pop(self):
        self.stack[0], self.stack[-1] = self.stack[-1], self.stack[0]
        return self.stack.pop()

    def shift_down(self):
        root_index = 0
        length = len(self.stack) - 1
        stack = self.stack
        while root_index < length:
            left_index = 2 * root_index + 1
            right_index = 2 * root_index + 2
            max = left_index
            if left_index > length:
                break
            if right_index <= length and stack[left_index] < stack[right_index]:
                max = right_index
            
            if stack[root_index] < stack[max]:
                stack[root_index], stack[max] = stack[max], stack[root_index]
                root_index = max
            else:
                break
            
                        
# heap_sort 代码实现
def build(arr, root, end):
    while True:
        left = 2 * root + 1 # 左子节点的位置
        right =  2 * root + 2
        max = left
        if left > end: # 若左子节点超过了最后一个节点，则终止循环
            # 这里很秒，只有这个写法很简洁
            break
        if (right <= end) and (arr[right] > arr[left]): 
            # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
            max = right
        if arr[max] > arr[root]: 
            # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
            arr[max], arr[root] = arr[root], arr[max]
            root = max
        else:
            break

def heap_sort(arr):
    print('build before', arr)
    n = len(arr)
    # 这里是第一个非堆节点
    first_root = n // 2 - 1 
    # 确认最深最后的那个根节点的位置
    for root in range(first_root, -1, -1): 
        # 由后向前遍历所有的根节点，建堆并进行调整
        build(arr, root, n - 1)
        
    print('build after', arr)
    for end in range(n - 1, 0, -1): 
        # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，
        # 然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作
        arr[0], arr[end] = arr[end], arr[0]
        build(arr, 0, end - 1)
        

if __name__ == "__main__":
    # h = Heap()
    # h.insert(85)
    # print(h.stack)
    # print(h.d())
    # print(h.stack)

    arr = [5, 8, 1, 0, 3, 7, 6, 2, 9]
    heap_sort(arr)
    print(arr)