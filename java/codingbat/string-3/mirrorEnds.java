/*
 * Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string. 
 * In other words, zero or more characters at the very begining of the given string, and at the very end of the 
 * string in reverse order (possibly overlapping). For example, the string "abXYZba" has the mirror end "ab".
 *
 * mirrorEnds("abXYZba") → "ab"
 * mirrorEnds("abca") → "a"
 * mirrorEnds("aba") → "aba"
 */
 
public String mirrorEnds(String string) {
    String result = "";
    String reverse = new StringBuilder(string).reverse().toString();
    int len = string.length();
    
    if (len == 1) return string;
    
    if (string.equals(reverse)) return string;
    
    for (int i = 0; i <= len / 2; i++) {
      for (int j = len / 2; j < len; j++) {
        String start = new StringBuilder(string.substring(0,i)).reverse().toString();
        if (start.equals(string.substring(j))) {
          result = string.substring(0, i);
        }
      }
    }
    
    return result;
}
