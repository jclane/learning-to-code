public class ninetyNineBottles {
    public static void main(String args[]) {
        for (int i = 99; i > 0; i--) {
            String bottleOrBottles = " bottles";
            
            if (i == 1) { bottleOrBottles = " bottle"; }
            
            System.out.println(i + bottleOrBottles + " of beer on the wall.");
            System.out.println("Take one down, pass it around.");
            if (i == 1) { System.out.println("No bottles of beer on the wall!"); }
            
        }
    }
}
