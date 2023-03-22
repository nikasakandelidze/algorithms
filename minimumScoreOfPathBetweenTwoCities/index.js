/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */

// The cities graph is not necessarily connected.
/*
    

*/
var minScore = function(n, roads) {
    const getAdjList = (roads, n) => {
        const result = new Map()
        for(let i=1; i<=n; i++){
            result.set(i, [])
        }
        for(const [from, to, cost] of roads){
            result.get(from).push([to, cost])
            result.get(to).push([from, cost])
        }
        return result
    }

    const bfsMin = (start, end, adjList) => {
        let result = Number.MAX_SAFE_INTEGER;
        const nodes = [ [start, Number.MAX_SAFE_INTEGER, new Set()] ]
        while(nodes.length){
            const [element, cost, visited] = nodes.shift()
            visited.add(element)
            if(element===end){
                result = Math.min(cost, result)
                continue
            }
            const neighbours = adjList.get(element)
            for(const [node, pathCost] of neighbours){
                if(!visited.has(node) || 
                (node===start || node === end)){
                    nodes.push(
                        [node,
                        Math.min(cost, pathCost),
                        new Set([...visited])]
                    )
                }
            }
        }
        return result
    }

    const adjList = getAdjList(roads, n)
    return bfsMin(1, n, adjList)
};
