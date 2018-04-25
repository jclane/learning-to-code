/*
Given 2 int arrays, each length 2, return a new array length 4 containing all their elements.

plusTwo([1, 2], [3, 4]) → [1, 2, 3, 4]
plusTwo([4, 4], [2, 2]) → [4, 4, 2, 2]
plusTwo([9, 2], [3, 4]) → [9, 2, 3, 4]
*/

public int[] plusTwo(int[] a, int[] b) {
  int[] arr = new int[(a.length + b.length)];
  
  for (int i = 0; i < 2; i++) {
    arr[i] = a[i];
    arr[i+2] = b[i];
  }
  
  return arr;
}
