import java.util.Arrays;
import java.util.ArrayList;

public class meanMedianMode {
    
    static String findMean(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return String.valueOf(sum / nums.length);
    }
    
    static String findMedian(int[] nums) {
        Arrays.sort(nums);
        
        if (nums.length % 2 == 1) {
            int[] result = {nums[(nums.length - 1) / 2]};
            return String.valueOf(result[0]);
        } else {
            int[] result = {nums[(nums.length - 1) / 2], nums[(nums.length - 1) / 2 + 1]};
            return String.valueOf(result[0]) + ", " + String.valueOf(result[1]);
        }
    }
    
    static String findMode(int[] nums) {
        long currentHighest = 1;
        ArrayList<Integer> result = new ArrayList<Integer>();
            int count = 0;
            for (int i = 0; i < nums.length - 1; i++) {
                if (nums[i] == nums[i+1]) {
                    count++;
                    if (count >= currentHighest) {
                        currentHighest = count;
                        result.add(nums[i]);
                    }
                }
            }
        return String.valueOf(result);
    }
    
    public static void main(String args[]) {
        int[] nums = {1,2,3,4,2,6};
        //System.out.println("Mean = " + findMean(nums));
        //System.out.println("Median = " + findMedian(nums));
        System.out.println("Mode = " + findMode(nums));
    }
}
