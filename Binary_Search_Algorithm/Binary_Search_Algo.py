def binary_search(a_list,item):
    #a_list is a sorted array/list
    # item number that is supposed to be searched

    first = 0
    last = len(a_list) - 1
    while first<=last:
        mid = int((first+last)/2)
        if a_list[mid] == item:
            print(f"the {item} is found at {mid}")
            break
        elif a_list>[mid]>item:
            last = mid-1
        elif a_list[mid]<item:
            first = mid +1 
    else:
        print(f"The {item} not found")



if __name__ == "__main__":
    binary_search([1,4,6,8,39,77,36,57,93,95,889],77)
