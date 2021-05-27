//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//
//        You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
//        You can return the answer in any order.



// Brute force algorithm:
// TIME BOUND O(n^2)

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


//There is a solution that time bound is O(n), which is using HashMap<K,V>

//Basic knowledge of HashMap:
// O(1) - get(), put(), remove()
//HashMap is not Synchronized, if multiple threads want to access and modified it, it need to be synchronized at first

//Basic idea of O(n) algorithm:

//Because it only needs two number to get the final answer and they have to be unique. Therefore,
//it will always have one element before and one element after.

//We store the current value, store it as a key and its value is the index of that value.

//We need to iterate the list and check if the hashmap has a value which is excatly equal to the difference between the target
//and current value. If it has, we store the current index as a **second** value in the return array and store the difference's
//index as the first value in the return array. The reason we did that is that we can only check the difference in the previous number.

//Otherwise, if we iterate the array from back to begin, we can store the current index as the first value in the return array.

//Here is my updated solution:(I iterate from back to begin):

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diff = new HashMap();
        int answer[] = new int[2];
        for(int i=nums.length-1; i >= 0; i--){
            if(diff.containsKey(target-nums[i])){

                answer[0] = i;
                answer[1] = diff.get(target-nums[i]);
                return answer;
            }
            diff.put(nums[i],i);
        }
        return answer;
    }
}


// the interesting thing is if we iterate form bagin to end, the run time will less than now. But I do not think
// the order of iterating matters, it's probably because of the test case.


