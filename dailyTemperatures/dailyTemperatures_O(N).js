//https://leetcode.com/problems/daily-temperatures/description/

// This solution uses assumption that every temperature/number in the array has max value of 100

var dailyTemperatures = function(temperatures) {
    const tempIndexes = Array.from(Array(101).keys()).map(_=>-1)
    const answers = temperatures.map(_=>0)
    for(let i=temperatures.length-1; i>=0; i--){
        const currentTemp = temperatures[i]
        let nextBiggerTempIdx=0
        for (let temp=currentTemp+1; temp<=100; temp++){
            const idxForNextBiggerTemp=tempIndexes[temp]
            if(idxForNextBiggerTemp!==-1){
                if(nextBiggerTempIdx===0){
                    nextBiggerTempIdx=idxForNextBiggerTemp
                }else{
                    nextBiggerTempIdx=Math.min(idxForNextBiggerTemp, nextBiggerTempIdx)
                }
            }
        }
        answers[i] = nextBiggerTempIdx===0 ? 0 : nextBiggerTempIdx-i
        tempIndexes[currentTemp]=i
    }
    return answers
};