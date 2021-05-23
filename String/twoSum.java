//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//
//        You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
//        You can return the answer in any order.

// Brute force algorithm:

class twoSum {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i< nums.length -1; i++){
            for(int j = i+1; j<nums.length; j++){
                if(nums[i] + nums[j] == target){
                    int answer[] = new int[2];
                    answer[0] = i;
                    answer[1] = j;
                    return answer;
                }
            }
        }
        int finalarray[] = new int[2];
        return finalarray;
    }
}