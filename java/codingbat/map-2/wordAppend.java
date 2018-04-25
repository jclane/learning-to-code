/*
 * Loop over the given array of strings to build a result string like this: when a string appears 
 * the 2nd, 4th, 6th, etc. time in the array, append the string to the result. 
 * Return the empty string if no string appears a 2nd time.
 * 
 * wordAppend(["a", "b", "a"]) → "a"
 * wordAppend(["a", "b", "a", "c", "a", "d", "a"]) → "aa"
 * wordAppend(["a", "", "a"]) → "a"
 */
 
public String wordAppend(String[] strings) {
  String result = "";
  
  Map<String, Integer> map = new HashMap<String, Integer>();
  for (String s : strings) {
    if (s.length() > 0 && !map.containsKey(s)) {
      map.put(s,1);
    } else if (s.length() > 0) {
      int count = map.get(s);
      map.put(s,count+1);
    }
    
    if (map.containsKey(s) && map.get(s) % 2 == 0) {
      result += s;
    }
  }
  return result;
}
