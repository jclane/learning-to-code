/*
Given an array of ints of odd length, look at the first, last, and middle values 
in the array and return the largest. The array length will be a least 1.

maxTriple([1, 2, 3]) → 3
maxTriple([1, 5, 3]) → 5
maxTriple([5, 2, 3]) → 5
*/

public int maxTriple(int[] nums) {
  int[] arr = new int[3];
  arr[0] = nums[0];
  arr[1] = nums[nums.length/2];
  arr[2] = nums[nums.length-1];
  Arrays.sort(arr);
  return arr[2];
}
