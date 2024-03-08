class removeDuplicate:
    def __init__(self):
        pass
    
    def removeConsecutiveDuplicates(self,inputString):
        result = []
        for char in inputString:
            if len(result) == 0 or char != result[-1]:
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    print("Starting exceution to remove consecutive duplicates from input string ...")
    print("Enter the input string")
    inputString = input()
    obj = removeDuplicate()
    try:
        res = obj.removeConsecutiveDuplicates(inputString)
        print(res)
    except Exception as er:
        raise er #AASDFFGFEEYUUTTEEE