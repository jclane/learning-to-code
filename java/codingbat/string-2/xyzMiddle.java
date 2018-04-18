/*
Given a string, does "xyz" appear in the middle of the string? 
To define middle, we'll say that the number of chars to the left 
and right of the "xyz" must differ by at most one. 
This problem is harder than it looks.

xyzMiddle("AAxyzBB") → true
xyzMiddle("AxyzBB") → true
xyzMiddle("AxyzBBB") → false
*/

public boolean xyzMiddle(String str) {
  if (str.length() < 3) return false;
  if (str.length() == 3 && str.equals("xyz")) return true;
  
  for (int i = 0; i < str.length() - 3; i++) {
    int front = str.substring(0,i).length();
    String midAndBack = str.substring(i,str.length());
    
    if (midAndBack.startsWith("xyz") && Math.max(front,midAndBack.length()-3) - Math.min(front,midAndBack.length()-3) <= 1) {
      return true;
    }
  }
  return false;
}
