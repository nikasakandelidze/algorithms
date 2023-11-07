const scheduleRoom = (activities) => {
    let result = []
    activities.sort((a,b)=>a.end-b.end)
    let idx = 0
    let lastFinishTime = 0
    while(idx < activities.length){
        const current = activities[i]
        if(lastFinishTime===0){
            result.push(current)
            lastFinishTime = current.end
        }else{
            if(current.start >= lastFinishTime){
                result.push(current)
            }
        }
        idx += 1
    }
}