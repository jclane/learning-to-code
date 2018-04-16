/*
Given 2 ints, a and b, return their sum. However, "teen" values in the range 13..19 inclusive, are extra lucky. 
So if either value is a teen, just return 19.

teenSum(3, 4) → 7
teenSum(10, 13) → 19
teenSum(13, 2) → 19
*/

public int teenSum(int a, int b) {
  if (a <= 19 && a >= 13 || b <= 19 && b >= 13) {
    return 19;
  } else {
    return a+b;
  }
}
