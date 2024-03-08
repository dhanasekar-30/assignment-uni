class arrayTraverse:
    def __init__(self):
        pass

    def segregateZerosOnes(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            while arr[left] == 0 and left < right:
                left += 1
            while arr[right] == 1 and left < right:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return arr
if __name__ == '__main__':
    obj = arrayTraverse()
    arr = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
    res = obj.segregateZerosOnes(arr)
    print(res)