/*
Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'. 
Return a string where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".

zipZap("zipXzap") → "zpXzp"
zipZap("zopzop") → "zpzp"
zipZap("zzzopzop") → "zzzpzp"
*/

public String zipZap(String str) {
  String newStr = "";
  
  if (str.length() <= 2) return str;
  
  for (int i = 0; i < str.length(); i++) {
    if (i == str.length() - 2) {
      newStr += str.substring(i,i+2);
      break;
    } else if (str.substring(i, i + 3).startsWith("z") && str.substring(i, i + 3).endsWith("p")) {
      newStr += str.substring(i, i + 1) + str.substring(i+2, i + 3);
      i += 2;
    } else {
      newStr += str.substring(i,i+1);
    }
  }

  return newStr;
}
