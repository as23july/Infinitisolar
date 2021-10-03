# def printf(arr,n):
#     if n==len(arr):
#         return
#     man
def rec(n):
    if n==1:
        return 1
    fac = rec(n-1)
    mul = n * fac
    return mul
def disarr(arr , i):
    if i==len(arr):
        return 
    print(arr[i])
    disarr(arr, i+1)


def reverse_arr(arr , i):
    if i==len(arr):
        return 
    
    reverse_arr(arr, i+1)
    print(arr[i])


def max_arr(arr,i):
    if i==len(arr) -1:
        return arr[i]
    num = max_arr(arr,i+1)
    if num>arr[i]:
        return num
    else:
        return arr[i]


def index_find(arr, data, i):
    if i== 0:
        return
    if arr[i]==data:
        return i+1
    else:
        num = index_find(arr, data,i-1)
        return num

# print(rec(5))
arr=[10,20,30,40,90,60,90,70]
# disarr(arr,0)
# reverse_arr(arr,0)
# print(max_arr(arr, 0))
print(index_find(arr, 90,7))

