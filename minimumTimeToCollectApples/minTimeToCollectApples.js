/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
//https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
const edgesToAdjList = (edges, n) => {
    const result = {}
    for(let i=0; i<n; i++){
        result[i]=[]
    }
    for(const [from, to] of edges){
        result[from].push(to)
    }
    return result
}

var minTime = function(n, edges, hasApple) {
    const adj = edgesToAdjList(edges, n)
    const appleIds = hasApple.reduce((accumulator, curr, idx)=>{
        curr && accumulator.push(idx);
        return accumulator
    }, [])
    const seenNodes = new Set()
    const getPath = (node) => {
        const stack = [[0, []]]
        while(stack.length){
            const [element, path]=stack.pop()
            if(element===node){
                path.forEach(elem=>{
                    seenNodes.add(elem)
                })
                return path.length
            }
            for(const neighbour of adj[element]){
                let newPath = [...path]
                if(!seenNodes.has(neighbour)){
                    newPath.push(neighbour)
                }else{
                    newPath = path
                }
                stack.push([neighbour, newPath])
            }
        }
        return 0
    }
    const resultPaths = {}
    appleIds.forEach(index=>{
        const path = getPath(index)
        resultPaths[index]=path
    })
    return Object.values(resultPaths).reduce((acc, curr)=>acc+curr,0)*2
};