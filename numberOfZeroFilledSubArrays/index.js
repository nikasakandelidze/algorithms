/**
 * @param {number[]} nums
 * @return {number}
 */
 /*
    For each element in array:
        Start going to the right till the element is zero:
            increment for each 0 found

    0 0 0 0  = 1*4 + 2*3 + 3*2 + 4 *1
    0 0 0    = 1*3 + 2*2 + 3*1
    0 0      = 
  */
var zeroFilledSubarray = function(nums) {
    let result = 0
    for(let i=0; i<nums.length; i++){
       const curr = nums[i]
       if(curr===0){
           result += 1
           for(let j=i+1; j<nums.length; j++){
               if(nums[j]===0){
                   result += 1
               }else{
                   break
               }
           }
       }
    }
    return result
};
