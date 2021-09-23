def prob(arr, q) :
    
    start = 0
    end = len(arr) - 1
    while(start <= end) :

        mid = start + (end - start) // 2
        
        if(arr[mid] == q) :
            return mid
        
        elif(arr[mid] >= arr[start]) :

            if(arr[start] <= q and q <= arr[mid]):
                end = mid - 1
            else :
                start = mid + 1
            
        else :
            if(arr[end] >= q and q >= arr[mid]) :
                start = mid + 1
            else :
                end = mid - 1

    return -1   


if __name__ == "__main__":

    n = int(input())
    arr = []
    for i in range(0, n):
        t = int(input())
        arr.append(t)

    no_of_queries = int(input())

    for i in range(0, no_of_queries):
        q = int(input())
        print(prob(arr, q))