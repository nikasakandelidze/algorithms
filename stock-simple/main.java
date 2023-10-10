class Solution {
    public int maxProfit(int[] prices) {
        int[] differences = new int[prices.length];
        int currentMax = prices[prices.length-1];
        for(int i=prices.length-1; i>=0; i--){
            differences[i]=currentMax-prices[i];
            currentMax = Math.max(currentMax, prices[i]);
        }
        return Arrays.stream(differences).max().orElse(0);
    }
}
