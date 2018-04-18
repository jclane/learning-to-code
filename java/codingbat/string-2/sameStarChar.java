/*
Returns true if for every '*' (star) in the string, if there are chars 
both immediately before and after the star, they are the same.

sameStarChar("xy*yzz") → true
sameStarChar("xy*zzz") → false
sameStarChar("*xa*az") → true
*/

public boolean sameStarChar(String str) {
  ArrayList strList = new ArrayList();
  for (int i = 0; i < str.length()-1; i++) {
    if (str.charAt(i) == '*') {
      if (i > 0) {
        strList.add(str.substring(i-1,i));
        strList.add(str.substring(i+1,i+2));
      }
    }
  }
  
  return strList.stream().distinct().limit(2).count() <= 1;
}
