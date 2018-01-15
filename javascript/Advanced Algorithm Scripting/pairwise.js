/*
Given an array arr, find element pairs whose sum equal the second argument 
arg and return the sum of their indices.

If multiple pairs are possible that have the same numeric elements but 
different indices, return the smallest sum of indices. Once an element has 
been used, it cannot be reused to pair with another.

For example pairwise([7, 9, 11, 13, 15], 20) returns 6. The pairs that sum 
to 20 are [7, 13] and [9, 11]. We can then write out the array with their 
indices and values.

Index	0	1	2	3	4
Value	7	9	11	13	15
Below we'll take their corresponding indices and add them.

7 + 13 = 20 → Indices 0 + 3 = 3
9 + 11 = 20 → Indices 1 + 2 = 3
3 + 3 = 6 → Return 6
*/

function pairwise(arr, arg) {
  let i = 0;
  let j = arr.length - 1;
  let pairs = [];

  while (i < j && i < arr.length && j >= 0) {
    var a = arr[i], b = arr[j];
    if (a + b == arg) {
      pairs.push([arr.indexOf(arr[i]), arr.indexOf(arr[j])]);
      while (i < arr.length && arr[i] == a) { i++; }
      while (j >= 0 && arr[j] == b) { j--; }
    } else if (a + b < arg) {
      while (i < arr.length && arr[i++] == a);
    } else {
      while (j >= 0 && arr[j--] == b);
    }
  }
    
  return pairs;
  
  //return arg;
}

// Should return 11.
pairwise([1,4,2,3,0,5], 7);