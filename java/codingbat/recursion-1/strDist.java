/*
 * Given a string and a non-empty substring sub, compute recursively the largest
 * substring which starts and ends with sub and return its length.
 *
 * strDist("catcowcat", "cat") → 9
 * strDist("catcowcat", "cow") → 3
 * strDist("cccatcowcatxx", "cat") → 9
 */
 
public int strDist(String str, String sub) {
  if (str.length() < sub.length()) return 0;
  
  if (str.startsWith(sub)) {
    return str.substring(0, str.lastIndexOf(sub)+sub.length()).length();
  }
  return strDist(str.substring(1), sub);
}
