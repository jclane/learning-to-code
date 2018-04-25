/*
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

firstHalf("WooHoo") → "Woo"
firstHalf("HelloThere") → "Hello"
firstHalf("abcdef") → "abc"
*/

public String firstHalf(String str) {
  if (str.length() % 2 == 0) {
    return str.substring(0,(str.length()/2));
  }
  return str;
}
