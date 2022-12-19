
//https://leetcode.com/problems/find-if-path-exists-in-graph/description/
const tranformToNeighbouringDict = (edges) => {
    const result = {}
    for(let [start, end] of edges){
        if(result[start]){
            result[start].push(end)
        }else{
            result[start]=[end]
        }
        if(result[end]){
            result[end].push(start)
        }else{
            result[end]=[start]
        }
    }
    return result
}

var validPath = function(n, edges, source, destination) {
    const neighbours = tranformToNeighbouringDict(edges)
    const visited = new Set()
    const queue = []
    queue.push(source)
    while (queue.length > 0){
        const current = queue.pop()
        if(current===destination){
            return true
        }
        for(let n of neighbours[current]){
            if(!visited.has(n)){
                visited.add(n)
                queue.push(n)
            }
        }
    }
    return false
};