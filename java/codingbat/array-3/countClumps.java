/*
 * Say that a "clump" in an array is a series of 2 or more adjacent elements
 * of the same value. Return the number of clumps in the given array.
 *
 * countClumps([1, 2, 2, 3, 4, 4]) → 2
 * countClumps([1, 1, 2, 1, 1]) → 2
 * countClumps([1, 1, 1, 1, 1]) → 1
 */
 
public int countClumps(int[] nums) {
  int clumps = 0;
  int currNum = -1;  
  
  for (int i = 0; i < nums.length - 1; i++) {
    if (currNum != nums[i]) {
      currNum = nums[i];
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] == nums[j]) {
          clumps++;
          i++;
          break;
        }
      }
    }
  }
  return clumps;
}
