/*
 * Given two strings, base and remove, return a version of the base string where all instances 
 * of the remove string have been removed (not case sensitive). You may assume that the remove 
 * string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing 
 * "xx" leaves "x".
 *
 * withoutString("Hello there", "llo") → "He there"
 * withoutString("Hello there", "e") → "Hllo thr"
 * withoutString("Hello there", "x") → "Hello there"
 */
 
public String withoutString(String base, String remove) {
  int remLen = remove.length();
  int baseLen = base.length();
  String result = "";

  for (int i = 0; i < baseLen;) {
    if(!(i + remLen > baseLen) && base.substring(i, i + remLen).equalsIgnoreCase(remove)) {
      i +=remLen;
      continue;
    } else {
      result += base.substring(i, i + 1);
      i++;
    }
  } 
   return result;
}
