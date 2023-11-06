// Objective function
// Constraints

// There are 2 types of knapsack: Fractional and 0-1 Knapsacks

// Solved using greedy algorithm
// Return Maximum total value of items that can be put in the sack ( remember that items here can be fractional ).
const fractionalKnapSack = (weights, prices, size) =>{
    const data = []
    for(let i=0; i<weights.length; i++){
        data.push({w:weights[i], p:prices[i]})
    }
    data.sort((a,b)=>a.p/a.w - b.p/b.w)
    let idx = 0
    let resultAmount = 0
    while (size>0 && idx < data.length){
        const curr = data[idx]
        if(curr.w <= size){
            resultAmount += curr.p
            size -= curr.w
        }else{
            resultAmount += (curr.p/curr.w) * size
            size -= size
        }
        idx += 1
    }
    return resultAmount
}

console.log(fractionalKnapSack([10, 20, 30], [60, 100, 120], 50))