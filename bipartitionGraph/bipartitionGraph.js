/**
 * @param {number} n
 * @param {number[][]} dislikes
 * @return {boolean}
 */

//https://leetcode.com/problems/possible-bipartition/description/
// This problem can be rephrased as a BiPartition graph problem
// BiPartition graph is a graph that: Doesn't contain cycles or Contains only even length-d ones
const getAdjMatrix = (edges) => {
    const data = {}
    const getArray=(key)=>{
        return data[key] ? data[key] :[]
    }
    for (const [a,b] of edges){
        const tempa=getArray(a)
        const tempb=getArray(b)
        tempa.push(b)
        tempb.push(a)
        data[a]=tempa
        data[b]=tempb
    }
    return data
}

const NONE='NONE'
const BLACK='BLACK'
const RED='RED'

class DisjointSet{
    data={}
    constructor(n){
        for(let i=1; i<n+1; i++){
            this.data[i]=i
        }
    }

    find(x){
        const temp=this.data[x]
        if(temp===x){
            return x
        }
        return this.find(temp)
    }

    union(x,y){
        const rootX=this.find(x)
        const rootY=this.find(y)
        if(rootX!==rootY){
            this.data[rootX]=rootY
        }
    }

    connected(x,y){
        return this.find(x)===this.find(y)
    }
}

var possibleBipartition = function(n, dislikes) {
    if(dislikes.length===0){
        return true
    }
    const adjMatrix = getAdjMatrix(dislikes)
    const uf = new DisjointSet(n)
    for(let i=1; i<=n; i++){
        const neighbours=adjMatrix[i]
        if(!neighbours || neighbours.length===0) continue
        const mainNeighbour=neighbours.shift()
        for(const n of neighbours){
            if(uf.connected(i, n)){
                return false
            }
            uf.union(mainNeighbour,n)
        }
    }
    return true

};