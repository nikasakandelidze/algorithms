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
        p1 = m-1
        p2 = n-1
        p=len(nums1)-1
        while p>=0:
            if p1 < 0:
                nums1[p] = nums2[p2] 
                p2 -= 1
            elif p2 < 0:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                first = nums1[p1]
                second = nums2[p2]
                if first > second:
                    nums1[p] = first
                    p1 -= 1
                else:
                    nums1[p] = second
                    p2 -= 1
            p -= 1
                
            
       
