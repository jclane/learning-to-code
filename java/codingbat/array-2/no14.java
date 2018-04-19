/*
 * Given an array of ints, return true if it contains no 1's or it contains no 4's.
 * 
 * no14([1, 2, 3]) → true
 * no14([1, 2, 3, 4]) → false
 * no14([2, 3, 4]) → true
 */

public boolean no14(int[] nums) {
  int count1 = 0;
  int count4 = 0;
  
  for (int n : nums) {
    if (n == 1) count1++;
    if (n == 4) count4++;
  }
  return count1 == 0 || count4 == 0;
}
