from array import array


try:
    a=list(map(float, input("Введите последовательность чисел через пробел:").split()))
    b=float(input("Введите чисело: "))
except:
    ValueError: print ("Введено не число!")
def selection(sort_nums):  
    for i in range(len(sort_nums)):
        index = i
        for j in range(i + 1, len(sort_nums)):
            if sort_nums[j] < sort_nums[index]:
                index = j
        sort_nums[i], sort_nums[index] = sort_nums[index], sort_nums[i]
def binary_search(array,element,left,right):
    if left>right:
        return right
    middle=(right+left)//2
    if array[right]<element or array[left]>element:
        print("Число выходит за границы последовательности")
        return
    if array[middle]==element:
        return middle
    elif element < array[middle]:
        return binary_search(array,element,left,middle-1)
    else:
        return binary_search(array,element,middle+1,right)
selection(a)
c=binary_search(a,b,0,len(a)-1)
print(f"Номер индекса искомой позиции {c}")
