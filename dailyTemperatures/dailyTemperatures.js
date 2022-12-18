//https://leetcode.com/problems/daily-temperatures/description/

const dailyTemperatures = (temperatures) => {
    const result = []
    for(let i=0; i<temperatures.length; i++){
        let skip=false;
        for(let j=i+1; j<temperatures.length; j++){
            if(temperatures[j]>temperatures[i]){
                result.push(j-i)
                skip=true
                break
            }
        }
        !skip && result.push(0)
    }
    return result
};

const temperatures = [73,74,75,71,69,72,76,73]
dailyTemperatures(temperatures)