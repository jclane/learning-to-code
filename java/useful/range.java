class Range {
  int low = 0;
  int high = 0;
  
  // Constructor
  public Range(int low, int high) {
    this.low = low;
    this.high = high;
  }
  
  // Returns true of false in num is in range.
  public contains(int num) {
    return num >= this.low && num <= this.high;
  }
}
