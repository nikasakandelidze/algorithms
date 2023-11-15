/**
 * @param {number[]} nums
 * @return {number}
 */

/* 
    [10,9,2,5,3,7,101,18] 
    [1, 1,1,2,2,3, 4,  4]

*/
var lengthOfLIS = function(nums) {
    const dp = Array(nums.length).fill(1)
    for(let i=0; i<nums.length-1; i++){
        for(let j=i+1; j<nums.length; j++){
            if(nums[j] > nums[i]){
                dp[j] = Math.max(dp[j], dp[i]+1)
            }
        }    
    }
    return Math.max(...dp)
};

console.log(lengthOfLIS([1,2,3]))
console.log(lengthOfLIS([10, 11, 12, 1, 2, 14, 0, 17]))