# encoding="utf-8"
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
        
    # 方式2
    # 建立堆
    # _first_root = first_root
    # while _first_root >= 0:
    #     build(arr, _first_root, n-1)
    #     _first_root-=1
        
    print('build after', arr)
    for end in range(n - 1, 0, -1): 
        # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，
        # 然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作
        arr[0], arr[end] = arr[end], arr[0]
        # 这一行代码太秒了 amazing，利用桶排序原地把排序做了，空间复杂度O(1)
        build(arr, 0, end - 1)
        

# if __name__ == "__main__":
#     arr = [5, 8, 1, 0, 3, 7, 6, 2, 9]
#     heap_sort(arr)
#     print(arr)
    
# 参考视频，老实讲的太棒了
# https://www.bilibili.com/video/BV1Et411v7cN/?spm_id_from=333.788.videocard.0

    
    
arr = [6, 3, 8, 4, 9, 7, 2, 1]
# 建堆前 [6, 3, 8, 4, 9, 7, 2, 1]
# 建堆后 [9, 6, 8, 4, 3, 7, 2, 1]
# 排序后 [1, 2, 3, 4, 6, 7, 8, 9]

def build1(arr, root, end):
    # end 这个参数也很秒啊，控制排序使用
    while True:
        left = 2 * root + 1
        right = 2 * root + 2
        max = left
        if left > end:
            break
        if right <= end and arr[right] > arr[left]:
            max = right
        if arr[max] > arr[root]:
            arr[max], arr[root] = arr[root], arr[max]
        else:
            break
        
def sort():
    first_root = len(arr) // 2 -1
    end = len(arr) - 1
    print("before build heap", arr)
    for root in range(first_root, -1, -1):
        build1(arr, root, end)
    print('after build heap', arr)
    
    for end in range(len(arr) - 1, -1, -1):
        # 这里倒数的是end，因为每一次建堆swap后end都有序
        arr[end], arr[0] = arr[0], arr[end]
        build1(arr, 0, end - 1)
    print("after sorted heap", arr)

if __name__ == "__main__":
    sort()
    
    
