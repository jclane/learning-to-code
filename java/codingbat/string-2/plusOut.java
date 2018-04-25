/*
Given a string and a non-empty word string, return a version of the original String where 
all chars have been replaced by pluses ("+"), except for appearances of the word string 
which are preserved unchanged.

plusOut("12xy34", "xy") → "++xy++"
plusOut("12xy34", "1") → "1+++++"
plusOut("12xy34xyabcxy", "xy") → "++xy++xy+++xy"
*/

public String plusOut(String str, String word) {
  int wlen = word.length();
  int len = str.length();
  int i = 0;
  String newStr = "";
  
  while (i < len) {
    if (str.substring(i).startsWith(word)) {
      newStr += word;
      i += wlen;
    } else {
      newStr += "+";
      i++;
    }
  }
  return newStr;
}
