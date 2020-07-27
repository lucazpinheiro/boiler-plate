
def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_position = int(abs(len(arr)/2))
        pivot = arr[pivot_position]
        left_arr = [i for i in arr if i < pivot]
        right_arr = [i for i in arr if i > pivot]
        return qsort(left_arr) + [pivot] + qsort(right_arr)


class Stack():
    def __init__(self):
        self.items = []
        self.count = 0

    def log(self):
        print(self.items)
        return self.items

    def size(self):
        print(self.count)
        return self.count

    def push(self, element):
        self.items.append(element)
        self.count += 1
        return self.count - 1

    def pop(self):
        self.items.pop(self.count - 1)
        self.count -= 1
        return self.count - 1

    def sort(self):
        def qsort(arr):
            if len(arr) < 2:
                return arr
            else:
                pivot_position = int(abs(len(arr)/2))
                pivot = arr[pivot_position]
                left_arr = [i for i in arr if i < pivot]
                right_arr = [i for i in arr if i > pivot]
                return qsort(left_arr) + [pivot] + qsort(right_arr)

        self.items = qsort(self.items)
        return self.items


st = Stack()

st.push(100)
st.push(75)
st.push(8)
st.push(301)
st.push(53)

st.log()
st.size()

print('\n')

st.sort()
st.log()
# print(st.items)
# print(st.count)
