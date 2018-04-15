# Given a string, return a version without the first 2 chars. 
# Except keep the first char if it is 'a' and keep the second char if it is 'b'. 
# The string may be any length. Harder than it looks.
#
# deFront("Hello") → "llo"
# deFront("java") → "va"
# deFront("away") → "aay"

public String deFront(String str) {   
  String result = "";
  
  if (str.startsWith("a")) {
    result += str.substring(0,1);
  }
  
  if (str.substring(1,2).equals("b")) {
    result += str.substring(1,2);
  }

    return result + str.substring(2,str.length());
}
