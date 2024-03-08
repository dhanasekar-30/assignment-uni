class unionIntersection:
    def __init__(self):
        pass
    
    ### Approach 1 ###
    def findUnionIntersection(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)        
        
        union = list(set1.union(set2))
        
        intersection = list(set1.intersection(set2))
        
        return union, intersection
    
    ### Approach 2 ###
    def unionIntersection(list1, list2):
        union = []
        intersection = []
        for item in list1:
            if item not in union:
                union.append(item)
            if item in list2 and item not in intersection:
                intersection.append(item)
        for item in list2:
            if item not in union:
                union.append(item)
            if item in list1 and item not in intersection:
                intersection.append(item)        
        return union, intersection
    
if __name__ == '__main__':
    obj = unionIntersection()
    list1 = [7, 8, 9, 10, 7, 9]
    list2 = [5, 6, 7, 1, 4, 8, 3]
    union, intersection = obj.findUnionIntersection(list1,list2)
    print("Union:", sorted(union))
    print("Intersection:", sorted(intersection))