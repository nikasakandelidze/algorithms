/*
    Problem: You're given a set of jobs, where each job has a deadline and a profit if it is completed before the deadline.
    The goal: sequence the jobs to maximize total profit.

    We need to maximize the profit.


    Scheduling strategy: Schedule at the last possible time of the deadline.

    Argument aas to why choose latest possible scheduling time: 
        The other strategy i was mainly thinking about was scheduling at the earliest possible time slot available at the moment ( not surpassing the deadline ).
        But that strategy fails to work correctly when at first high profit job with high deadline comes and later, another well profited job arrives with as low deadline as possible.
        The first job might have easily blocked the first job when there was possibility to schedule both of them.

        When you have jobs sorted by their profits, the later you schedule a job the better, since scheduling from start and scheduling from end,
        just seem to be symmetrical activities but they aren't. If you start from the start, there is no available space lower then start(0). Thus you are already
        potentially introducing collisions and reducing the chance of getting anywhere. But if you start from the end, there is always possibility that some new profit
        with higher deadline comes in and you won't have to adjust anything, since higher deadlines are automatically available.
*/
const jobSequencing = (jobs) => {
    jobs.sort((a,b)=>b.profit - a.profit)
    const usedTimes = {}
    const result = []
    for(const job of jobs){
        for(let i=job.deadline-1; i>=0; i--){
            if(!usedTimes[i]){
                usedTimes[i]=job
                result.push(job)
                break
            }
        }
    }
    return result
}

let jobs = [{id: 'k', deadline: 1, profit: 200},
            {id: 'a', deadline: 2, profit: 100},
            {id: 'c', deadline: 9, profit: 27},
            {id: 'b', deadline: 5, profit: 26},
            {id: 'd', deadline: 4, profit: 25}];

//[200,100,27,26,]

[100,27,15,25,26]
console.log(jobSequencing(jobs))