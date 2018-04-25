/*
Return a version of the given string, where for every star (*) in the string the star 
and the chars immediately to its left and right are gone. So "ab*cd" yields "ad" and 
"ab**cd" also yields "ad".

starOut("ab*cd") → "ad"
starOut("ab**cd") → "ad"
starOut("sm*eilly") → "silly"
*/

public String starOut(String str) {
  String newStr = "";
  
  for (int i = 0; i < str.length(); i++) {
    if (i == 0 && str.charAt(i) != '*') newStr += str.charAt(i);
    if (i > 0 && str.charAt(i) != '*' && str.charAt(i-1) != '*') newStr += str.charAt(i);
    if (i > 0 && str.charAt(i) == '*' && str.charAt(i-1) != '*') newStr = newStr.substring(0,newStr.length()-1);
  }

  return newStr;
}
