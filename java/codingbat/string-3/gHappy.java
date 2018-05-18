/*
 * We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right. 
 * Return true if all the g's in the given string are happy.
 *
 * gHappy("xxggxx") → true
 * gHappy("xxgxx") → false
 * gHappy("xxggyygxx") → false
 */

public boolean gHappy(String str) {
  boolean result = false;
  
  if (str.length() == 0) return true;
  if (str == "gg") return true;
  if (str == "g") return false;
  
  for (int i = 0; i <= str.length()-1; i++) {
    if (i + 1 < str.length() && i - 1 > 0) {
      if (str.charAt(i) == 'g') {
        if (str.charAt(i-1) == 'g' || str.charAt(i+1) == 'g') {
          result = true; 
        } else { 
          result = false;
        }
      }
    }
    if (str.charAt(str.length()-1) == 'g' && str.charAt(str.length()-2) != 'g') result = false;
  }
  return result;
}
