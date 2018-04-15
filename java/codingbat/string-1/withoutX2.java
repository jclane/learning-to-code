# Given a string, if one or both of the first 2 chars is 'x', return the string without those 'x' chars, and 
# otherwise return the string unchanged. This is a little harder than it looks.
#
# withoutX2("xHi") → "Hi"
# withoutX2("Hxi") → "Hi"
# withoutX2("Hi") → "Hi"

public String withoutX2(String str) {
  
  if (str.length() <= 2 && str.startsWith("x") && str.endsWith("x")) {
    return "";
  }
  
  if (str.length() >= 2 && str.substring(1,2).equals("x")) {
    str = str.substring(0,1) + str.substring(2,str.length());
  }

  if (str.length() >= 2 && str.startsWith("x")) {
    str = str.substring(1);
  }
  
  if (str.length() >= 2 && str.substring(0,1).equals("x")) {
    str = str.substring(1);
  }

  return str;
}
