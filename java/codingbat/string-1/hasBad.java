# Given a string, return true if "bad" appears starting at index 0 or 1 in the string, 
# such as with "badxxx" or "xbadxx" but not "xxbadxx". The string may be any length, 
# including 0. Note: use .equals() to compare 2 strings.
#
# hasBad("badxx") → true
# hasBad("xbadxx") → true
# hasBad("xxbadxx") → false

public boolean hasBad(String str) {
  String target = "bad";
  
  if (str.equals("bad")) {
    return true;
  } else if (str.length() >= 4) {
    String ndex0 = str.substring(0,3);
    String ndex1 = str.substring(1,4);
    return (ndex0.equals(target) || ndex1.equals(target));
  }
  return false;
}
