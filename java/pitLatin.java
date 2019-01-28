import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

class Main {
  public static void main(String[] args) {
    Scanner reader = new Scanner(System.in);
    String str = " ";
    while (!str.equals("")) {
      System.out.println("Enter string: ");
      str = reader.nextLine();
      String[] strArr = str.split(" ");
      StringBuilder sb = new StringBuilder(str.length());
      for (String word : strArr) {
        if (startsWithVowel(word)) {
          sb.append(word + "yay ");
        } else if (startsWithConCluster(word)) { 
          String conCluster = getConCluster(word);
          sb.append(word.substring(conCluster.length()) + conCluster + "ay");
        } else {
          sb.append(word.substring(1) + word.charAt(0) + "ay ");
        }
      }
      System.out.println(sb.toString());
    }
    reader.close();
  }

  private static boolean startsWithVowel(String str) {
    return str.matches("[AEIOUaeiou]$");
  }

  private static boolean startsWithConCluster(String str) {
    return str.toLowerCase().matches("(sh|sm|sn|st|sw|sk|sl|sp|sph|thw|dw|tw|thr|dr|tr|qu|cr|cl|pr|fr|br|gr|pl|fl|bl|gl|shr).*");
  }

  private static String getConCluster(String str) {
    boolean strCase = Character.isUpperCase(str.charAt(0));
    String ignoreCase = str.toLowerCase();
    Pattern MY_PATTERN = Pattern.compile("(sh|sm|sn|st|sw|sk|sl|sp|sph|thw|dw|tw|thr|dr|tr|qu|cr|cl|pr|fr|br|gr|pl|fl|bl|gl|shr).*");
    Matcher m = MY_PATTERN.matcher(ignoreCase);
    if (m.find()) {
      return (strCase ? m.group(1).substring(0, 1).toUpperCase() + m.group(1).substring(1) : m.group(1));
    }
    return "ERROR";
  }
}
