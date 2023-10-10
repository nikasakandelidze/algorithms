class Solution {
    public int maxProfit(int[] prices) {
        Map<String, Integer> cache = new HashMap<>();
        return recursiveHelper(prices, 0, true, cache);

    }

    // [x, y, z]
    private int recursiveHelper(int[] prices, int idx, boolean canBuy, Map<String, Integer> cache){
        if(idx == prices.length){
            return 0;
        }
        if(cache.containsKey(canBuy+"_"+idx)){
            return cache.get(canBuy+"_"+idx);
        }
        if(canBuy){
            int result1 = recursiveHelper(prices, idx+1, !canBuy, cache) - prices[idx];
            int result2 = recursiveHelper(prices, idx+1, canBuy, cache);
            int result = Math.max(result1, result2);
            cache.put(canBuy+"_"+idx, result);
            return result;
        }else{
            int result1 = recursiveHelper(prices, idx+1, !canBuy, cache) + prices[idx];
            int result2 = recursiveHelper(prices, idx+1, canBuy, cache);
            int result = Math.max(result1, result2);
            cache.put(canBuy+"_"+idx, result);
            return result;
        }
    }

