// The function should return max Subarray sum
// [-1, 3, 4, -5, 9, -2]
// Divide and Conquer
// Simplest Case: If the length of the array is 1 it's itself the value
//  
// Try divide and conquer
// O(N^2)
const maxSubArrayBad  = (arr) => {
    let result = -1;
    for(let i=0; i<arr.length; i++){
        let temp = 0
        for(let j=i; j<arr.length; j++){
            temp += arr[j]
            result = Math.max(temp, result)
        }    
    }
    return result
}

console.log(maxSubArrayBad([-1, 3, 4, -5, 9, -2])===11)
console.log(maxSubArrayBad([-1, 3, 4, 5, 9])===21)
console.log(maxSubArrayBad([-1, -3, -4, -5, -9])===-1)


const maxSubArrayNotTooBad = (arr) => {
    /*
        On each recurrence, further recursive function calls tell us if there are max results in sub problems themselves
        and we still need to calculate if starting from mid going to both sides there is crossing maximum result
    */
    const crossingMaxSum = (arr, left, mid, right) => {
        console.log(left, mid, right, arr)
        let leftResult = -Infinity
        let temp = 0
        let l = mid
        while(l>=left){
            temp += arr[l]
            leftResult = Math.max(leftResult, temp)
            l-=1
        }
        let rightResult = -Infinity
        temp = 0
        let r = mid+1
        while(r<=right){
            temp += arr[r]
            rightResult = Math.max(rightResult, temp)
            r+=1
        }
        console.log(leftResult, rightResult )
        return Math.max(leftResult, rightResult, leftResult + rightResult)
    }

    const helper = (arr, start, end) => {
        if(start===end){
            return arr[start]
        }
        const mid = Math.floor((start+end)/2)
        const left = helper(arr, start, mid)
        const right = helper(arr, mid+1, end)
        const crossing = crossingMaxSum(arr, start, mid, end)
        const res = Math.max(left, right, crossing)
        return res
    }

    return helper(arr, 0, arr.length-1)
}

console.log(maxSubArrayNotTooBad([-1, 3, 4])===7)