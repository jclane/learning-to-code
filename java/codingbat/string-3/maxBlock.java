/*
 * Given a string, return the length of the largest "block" in the string. 
 * A block is a run of adjacent chars that are the same.
 *
 * maxBlock("hoopla") → 2
 * maxBlock("abbCCCddBBBxx") → 3
 * maxBlock("") → 0
 */
 
public int maxBlock(String str) {
  int result = 0;
  int currCount = 1;
  
  for (int i = 0; i < str.length()-1;) {
    if (str.charAt(i) == str.charAt(i+1)) {
      currCount++;
      i++;
    } else {
      currCount = 1;
      i++;
    }
    if (currCount > result) result = currCount;
  }
  return result;
}
