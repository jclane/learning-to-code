/*
Given an int array, return true if the array contains 2 twice, or 3 twice. The array will be length 0, 1, or 2.

double23([2, 2]) → true
double23([3, 3]) → true
double23([2, 3]) → false
*/

public boolean double23(int[] nums) {
  for (int i = 0; i < nums.length-1; i++) {
    if (nums[i] == 2 || nums[i] == 3) {
      if (nums[i] == nums[i+1]) {
        return true;
      }
    }
  }
  return false;
}
