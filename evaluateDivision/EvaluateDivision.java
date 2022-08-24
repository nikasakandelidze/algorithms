// https://leetcode.com/problems/evaluate-division/

class Pair{
    double weight;
    String to;

    public Pair(double weight, String to){
        this.weight = weight;
        this.to = to;
    }

    public String toString(){
        return "weight: "+weight + ", to: "+to;
    }
}

class AdjMap{
    Map<String, List<Pair>> adjMap = new HashMap<>();

    public AdjMap(List<List<String>> equations, double[] values){
        for(int i = 0; i< equations.size(); i++){
            String from = equations.get(i).get(0);
            String to = equations.get(i).get(1);
            double val = values[i];
            if (adjMap.containsKey(from)){
                adjMap.get(from).add(new Pair(val, to));
            }else{
                List<Pair> ls = new ArrayList<>();
                ls.add(new Pair(val, to));
                adjMap.put(from, ls);
            }
            if (adjMap.containsKey(to)){
                adjMap.get(to).add(new Pair(1.0/val, from));
            }else{
                List<Pair> ls = new ArrayList<>();
                ls.add(new Pair(1.0/val, from));
                adjMap.put(to, ls);
            }
        }
    }
}

class Solution {

    public double dfs(AdjMap adjMap, List<String> query){
        String start = query.get(0);
        String end = query.get(1);
        if(!adjMap.adjMap.containsKey(start)){
            return -1;
        }
        Queue<Pair> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.add(new Pair(1, start));
        visited.add(start);
        while (!queue.isEmpty()){
            Pair p = queue.poll();
            if (p.to.equals(end)){
                return p.weight;
            }
            List<Pair> neighbours = adjMap.adjMap.get(p.to);
            if(neighbours == null){
                return -1;
            }
            for(Pair n : neighbours){
                if(!visited.contains(n.to)){
                    queue.add(new Pair(p.weight * n.weight, n.to));
                    visited.add(n.to);
                }
            }
        }
        return -1;
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        var adjMap = new AdjMap(equations, values);
        return queries.stream()
            .map(query -> (double)dfs(adjMap, query))
            .mapToDouble(Double::doubleValue)
            .toArray();
    }

  // add tests later
}