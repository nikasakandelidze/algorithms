// https://leetcode.com/problems/jump-game/description/
 // [2,3,1,1,4]
 // [3,2,1,0,4]
var canJump = function(nums) {
    const elems = nums.map(_=>false)
    elems[0]=true
    for(let i=0; i<nums.length; i++){
        if(elems[i]){
            if(i===nums.length-1) return true
            const maxJump=nums[i]
            for(let j=i; j<=i+maxJump; j++){
                elems[j]=true
            }
        }
    }
    return false
};