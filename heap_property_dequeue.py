# encoding="utf-8"

class Heap:
    def __init__(self):
        self.stack = [90,80,70,60,40,30,20,10,50]

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
        while True:
            left_index = 2 * root_index + 1
            right_index = 2 * root_index + 2

            if left_index > length and right_index > length:
                # 如果索引越界那么结束
                break
            if left_index <= length and right_index > length:
               if self.stack[left_index] > self.stack[root_index]:
                   self.stack[left_index], self.stack[root_index] = \
                     self.stack[root_index], self.stack[left_index]
                   root_index = left_index

            if left_index > length and right_index <= length:
               if self.stack[right_index] > self.stack[root_index]:
                   self.stack[right_index], self.stack[root_index] = \
                     self.stack[root_index], self.stack[right_index]
                   root_index = right_index
            if left_index <= length and right_index <= length:
               max_value = max(stack[root_index], stack[left_index], stack[right_index])
               if max_value == stack[root_index]:
                   break
               elif max_value == stack[left_index]:
                   stack[left_index], stack[root_index] = stack[root_index], stack[left_index]
                   root_index = left_index
               elif max_value == stack[right_index]:
                   stack[right_index], stack[root_index] = stack[root_index], stack[right_index]
               else:
                   break


if __name__ == "__main__":
    h = Heap()
    h.insert(85)
