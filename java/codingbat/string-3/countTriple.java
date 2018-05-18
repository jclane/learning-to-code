/*
 * We'll say that a "triple" in a string is a char appearing three times in a row. 
 * Return the number of triples in the given string. The triples may overlap.
 * 
 * countTriple("abcXXXabc") → 1
 * countTriple("xxxabyyyycd") → 3
 * countTriple("a") → 0
 */

public int countTriple(String str) {
  int count = 0;
  
  if (str.length() < 3) return 0;
  
  for (int i = 0; i <= str.length()-3; i++) {
    String c = str.substring(i,i+1);
    String query = c + c + c;
    if (str.substring(i,i+3).equals(query)) count++;
  }
  return count;
}
