/*
Given 2 int arrays, a and b, return a new array length 2 containing, as much as will fit, 
the elements from a followed by the elements from b. The arrays may be any length, including 0, 
but there will be 2 or more elements available between the 2 arrays.

make2([4, 5], [1, 2, 3]) → [4, 5]
make2([4], [1, 2, 3]) → [4, 1]
make2([], [1, 2]) → [1, 2]
*/

public int[] make2(int[] a, int[] b) {

  int[] arr = new int[2];
  
  if (a.length >= 2) {
    arr[0] = a[0];
    arr[1] = a[1];
  } else if (a.length == 1 && b.length > 0) {
    arr[0] = a[0];
    arr[1] = b[0];
  } else if (a.length < 2) {
    arr[0] = b[0];
    arr[1] = b[1];
  }
  
  return arr;
}
