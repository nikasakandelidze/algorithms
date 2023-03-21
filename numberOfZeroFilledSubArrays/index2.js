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
    const getNumberOfZeroIslands = (array) => {
        const result = []
        let count = 0
        for(let i=0; i<array.length; i++){
            console.log(array[i], count)
            if(array[i]===0){
                count += 1
            }else{
                if(count!=0){
                    result.push(count)
                    count = 0
                }
            }
        }
        if(count!==0){
            result.push(count)
        }
        return result
    }

    const calculateNumberOfSubArrays = (number) => {
        let result = 0
        while (number>=1) {
            result += number
            number -= 1
        }
        return result
    }

    const numOfZeroIslands = getNumberOfZeroIslands(nums)
    console.log(numOfZeroIslands)
    return numOfZeroIslands.reduce((acc, curr) => {
        return acc + calculateNumberOfSubArrays(curr)
    }, 0)
}
