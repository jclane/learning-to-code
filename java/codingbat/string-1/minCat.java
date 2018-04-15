# Given two strings, append them together (known as "concatenation") and return the result. 
# However, if the strings are different lengths, omit chars from the longer string so it is 
# the same length as the shorter string. So "Hello" and "Hi" yield "loHi". 
# The strings may be any length.
#
# minCat("Hello", "Hi") → "loHi"
# minCat("Hello", "java") → "ellojava"
# minCat("java", "Hello") → "javaello"

public String minCat(String a, String b) {
  int diff = Math.abs(a.length() - b.length());

  if (a.length() > b.length()) {
    a = a.substring(diff,a.length());
  }
  
  if (b.length() > a.length()) {
    b = b.substring(diff,b.length());
  } 
  
  return a + b;
}
