/*
 * Given a string that contains a single pair of parenthesis, 
 * compute recursively a new string made of only of the parenthesis
 * and their contents, so "xyz(abc)123" yields "(abc)".
 *
 * parenBit("xyz(abc)123") → "(abc)"
 * parenBit("x(hello)") → "(hello)"
 * parenBit("(xy)1") → "(xy)"
 */
 
public String parenBit(String str) {
  if (str.length() == 0) return str;
  
  if (str.charAt(0) == '(') {
    int ndexclose = str.indexOf(")");
    return str.substring(0,ndexclose+1) + parenBit(str.substring(1));
  }
  return parenBit(str.substring(1));
}
