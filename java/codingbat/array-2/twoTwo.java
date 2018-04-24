/*
 * Given an array of ints, return true if every 2 that appears in the array is next to another 2.
 * 
 * twoTwo([4, 2, 2, 3]) → true
 * twoTwo([2, 2, 4]) → true
 * twoTwo([2, 2, 4, 2]) → false
 */
 
public boolean twoTwo(int[] nums) {
  
  if (nums.length < 1) return true;
  if (nums.length == 1 && nums[0] == 2) {
    return false;
  }
  
  for (int i = 0; i < nums.length; i++) {
    if (i == 0 && nums[i] == 2 && nums[i+1] != 2) return false;
    if (i > 0 && i < nums.length-1 && nums[i] == 2) {
      if (nums[i-1] != 2 && nums[i+1] != 2) return false;
    }
    if (i == nums.length-1 && nums[i] == 2) {
      if (nums[i-1] != 2) return false;
    }
  }
  return true;
}
