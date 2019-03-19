def bubble_sort(items):
    length = len(items) - 1
    sorted = False
    while not sorted:
        sorted = True
        for element in range(0,length):
            if items[element] > items[element + 1]:
                 hold = items[element + 1]
                 items[element + 1] = items[element]
                 items[element] = hold
                 sorted = False
    return items



def merge_sort(items):
   x = len(items) // 2
    if not x: # length is 1
        return items
    else:
        return merge(merge_sort(items[:x]), merge_sort(items=[x:]))




def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        return quick_sort([x for x in items[1:]if x < items[0]])+/
        [items[0]]+ quick_sort([x for x in items=[1:]if x> = items[0]])
