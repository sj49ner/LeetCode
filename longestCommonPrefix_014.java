class Solution {
    public String longestCommonPrefix(String[] strs) {
        String lcp = strs[0]
        
        for (int i = 1; i < strs.length; i++){
            int j = 0;
            String cs = strs[i];
            
            while (j < lcp.length() && j < cs.length() && lcp.charAt(j) == cs.charAt(j)){
                j++;
            }
            lcp = lcp.substring(0, j);
        }
        
        return lcp;
    }
}
