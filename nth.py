

def findKth(list1, start1, end1, current1, list2, start2, end2, current2, k):
    if current1 + current2 + 1 > k: # needs to decrease:
        if list1[current1] > list2[current2]:  # decease list1
            print 'decrease list1'
            new_current1 = int((start1 + current1) / 2)
            findKth(list1, start1, current1, new_current1, list2, start2, end2, current2, k)
        else: #decrease list2
            print 'decrease list2'
            new_current2 = int((start2 + current2) / 2)
            findKth(list1, start1, end1, current1, list2, start2, current2, new_current2, k)
    elif current1 + current2 + 1 < k: #needs to increase:
        if list1[current1] > list2[current2]:  # increase list2
            print 'increase list2'
            new_current2 = int((current2 + end2) / 2)
            findKth(list1, start1, end1, current1, list2, current2, end2, new_current2, k)
        else: # increase list1
            print 'increase list1'
            new_current1 = int((current1 + end1) / 2)
            findKth(list1, current1, end1, new_current1, list2, start2, end2, current2, k)
    else:
        print 'current1 = %d, current2 = %d' % (current1, current2)
        print 'val1 = %d, val2 = %d' % (list1[current1], list2[current2])


if __name__ == '__main__':
    list1 = [1,5,6,7,8,16,23,44,45,60,62,67,70]
    list2 = [2,3,4,9,11,12,40,41,55,56,58,62]
    k = 6 
    findKth(list1, 0, k+1, int((k+1) / 2), list2, 0, k+1, int((k+1)/2), k)

    wholelist = sorted(list1 + list2)
    print 'correct result is %d' % wholelist[k]
