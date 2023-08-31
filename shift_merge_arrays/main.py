class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        Solution #1:
            If we are not allowed to allocate new memory blocks, then we can use shifting of 
            array elements. The shifting of elements would be a big problem in context of time
            complexity since in the worst case scenario we'd have to shift n elements m times. 
            [a,b,c,0,0,0]  [d,e,f]
            Meaning that time complexity would become: O(N^2) but since we have hard limits
            placed on m & n shifting operation becomes a constant factor and we don't have to worry
            about it any more
            
            Algo:
                Take 2 pointers for both arrays and start iterating:
                    If first <= second:
                        increment first idx
                    if first > second:
                        shift all elements of first array starting from first idx to the right
                        place to the first idx position element from second array second idx
                        increment second idx
                After iteration is complete:
                    If second index has not gone to the end, dump all these elements at the end of
                    the first array.
            ---------------------------------------
            [1,2,2,3,4,0] [X,5]
        """
        
        def shift_right(arr, from_idx):
            end_idx = len(arr)-1
            for k in range(end_idx-1, from_idx-1, -1):
                arr[k+1]=arr[k]
                
        i = 0
        j = 0
        original_arr_bound = m
        while i<original_arr_bound and j<n:
            left = nums1[i]
            right = nums2[j]
            if left <= right:
                i += 1
            else:
                shift_right(nums1, i)
                nums1[i]=nums2[j]
                original_arr_bound += 1
                j += 1
        while j < n:
            nums1[original_arr_bound] = nums2[j]
            j += 1
            original_arr_bound += 1
                
            
        
