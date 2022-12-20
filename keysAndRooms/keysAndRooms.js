/**
    https://leetcode.com/problems/keys-and-rooms/description/
 */
var canVisitAllRooms = function(rooms) {
    // This looks like a graph problem to me
    // start node: 0
    const visited = new Set()
    visited.add(0)
    const queue = [rooms[0]]
    while(queue.length > 0){
        const placesToGo = queue.pop()
        for(let toGo of placesToGo){
            if(!visited.has(toGo)){
                queue.push(rooms[toGo])
                visited.add(toGo)
            }
        }
    }
    return visited.size === rooms.length
};