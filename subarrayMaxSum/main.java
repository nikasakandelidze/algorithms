class Solution {
    /*
        Result: Return largest sum subarray
        - Subarray is a consequtive elements
        - There are negative numbers
        [1,1, -3, 4]
        [-1,-2,-3,-4]
     */
    public int maxSubArray(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }
        int result = Integer.MIN_VALUE;
        int currentSum = 0;
        for (int i=0; i<nums.length; i++){
            if(nums[i]<0){
                if(currentSum==0){
                    result = Math.max(result, nums[i]);
                    currentSum = nums[i];
                }else if(currentSum < 0){
                    result = Math.max(currentSum, Math.max(nums[i], result));
                    currentSum = nums[i];
                }else{
                    result = Math.max(result, currentSum);
                    currentSum += nums[i];
                }
            }else{
                if(currentSum >= 0){
                    currentSum += nums[i];
                }else{
                    currentSum = nums[i];
                }
                result = Math.max(result, currentSum);
            } 
        }
        return result;
    }
}
