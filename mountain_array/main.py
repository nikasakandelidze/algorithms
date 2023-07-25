class Solution:
    #   
    #   i exists such that arr[j] < arr[i] for j < i  and arr[k] > arr[i] for k > i
    #   We can use binary search, since    
    #   Technically we have 2 sub-arrays, both sorted: 1st one ascending and the second one descending
    #      
    #
    # [1,2,4,5,4,3,2,1]
    # [1,2,3]
    #   Does it mean that binary search in array is basically possible because we know some kind
    #   of a relation between all elements and their neighbours that allows us to decide which part to
    #   forget and where to continue searching. Meaning that there might be also other cases of arrays
    #   that are not directly sorted such as mountain array but are still usable for binary search
    #
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)-1
        while start <= end:
            curr_idx = (start + end)//2
            curr = arr[curr_idx]
            if curr_idx > 0 and curr_idx < len(arr)-1:
                prev = arr[curr_idx-1]
                nxt = arr[curr_idx+1]
                if prev < curr and curr > nxt:
                    return curr_idx
                elif prev < curr and curr < nxt:
                    start = curr_idx
                elif prev > curr and curr > nxt:
                    end = curr_idx
            else:
               break

        return -1



