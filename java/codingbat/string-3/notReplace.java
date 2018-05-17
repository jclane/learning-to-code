/*
 * Given a string, return a string where every appearance of the lowercase word "is" has been replaced with "is not". 
 * The word "is" should not be immediately preceeded or followed by a letter -- so for example the "is" in "this" does not count. 
 * (Note: Character.isLetter(char) tests if a char is a letter.)
 *
 * notReplace("is test") → "is not test"
 * notReplace("is-is") → "is not-is not"
 * notReplace("This is right") → "This is not right"
 */
 
public String notReplace(String str) {
  String result = "";
  int len = str.length();
  
  if (len == 0) return str;
  if (len == 2 && str.substring(0,2).equals("is")) return "is not";
  
  for (int i = 0; i < len; i++) {
    if(i - 1 >= 0 && Character.isLetter(str.charAt(i - 1))
      || i + 2 < len && Character.isLetter(str.charAt(i + 2))) {
      result += str.charAt(i);
    } else if(i + 1 < len && str.substring(i, i + 2).equals("is")) {
      result += "is not";
      i++;
    }
  }
  
  return result;
}
