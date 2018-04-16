/*
Given a string of even length, return a string made of the middle two chars, so the string "string" yields "ri". 
The string length will be at least 2.

middleTwo("string") → "ri"
middleTwo("code") → "od"
middleTwo("Practice") → "ct"
*/
  
public String middleTwo(String str) {
  if (str.length() % 2 == 0) {
    int length = str.length();
    return str.substring(length/2-1,length/2+1);
  }
  return str;
}
