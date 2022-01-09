def countingSort(arr):
    max_num = 0
    
    for i in arr:
        if arr[i] > max_num:
            max_num = arr[i]
    print(max_num)
    
    cnt = [0] * (max_num+1)
    print(cnt)
    
    for j in arr:
        print(f"j: {j}")
        cnt[j] += 1
        print(cnt)
    return cnt

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
