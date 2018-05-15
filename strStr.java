class Solution {
    public int strStr(String haystack, String needle) {
        int len = needle.length();
        if (len == 0)
            return 0;
        
        for (int i = 0; i < haystack.length(); i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                int endindex = i + len;
                if (endindex < haystack.length() + 1 &&
                    haystack.substring(i, endindex).equals(needle))
                    return i;
            }
        }
            
        return -1;
    }
}