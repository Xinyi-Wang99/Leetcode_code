class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(n == 0 )
            return;
        else if(m==0){
            for(int i=0; i<n; i++)
                nums1[i] = nums2[i];
            return;
        }
        else if(nums1[m-1] < nums2[0]){// the biggest number in nums1 is less than the smallest number in nums2
            for(int i=0; i<n; i++){
                nums1[m+i] = nums2[i];
            }
            return;
        }
        else if(nums2[n-1] < nums1[0]){// the biggest number in nums2 is less than the smallest number in nums1
            int[] sorted = new int[m];
            for(int i=0; i<m; i++){
                sorted[i] = nums1[i];
            }
            for(int num =0; num< n; num ++){
                nums1[num] = nums2[num];
            }
            for(int i=n; i<m+n; i++){
                nums1[i] = sorted[i-n];
            }
            return;
        }
        else{
            int i=0;// index for num1
            int j=0;// indedx for num2
            int s=0;// sorted array index
            int[] sorted = new int[n+m];
            while(i<m && j<n){
                if(nums1[i] < nums2[j]){
                    sorted[s] = nums1[i];
                    s++;
                    i++;
                }
                else if(nums1[i] > nums2[j]){
                    sorted[s] = nums2[j];
                    j++;
                    s++;
                }
                else{// if they are equal
                    sorted[s] = nums1[i];
                    sorted[s+1] = nums2[j];
                    s += 2;
                    i++;
                    j++;
                }
            }
            while(i<m){
                sorted[s] = nums1[i];
                s++;
                i++;
            }
            while(j<n){
                sorted[s] = nums2[j];
                s++;
                j++;
            }
            for(int num =0; num< n+m; num ++){
                nums1[num] = sorted[num];
            }
            return;
        }
    }
}


//Explain the problem:
//The reason why it has so many trailing 0s is that it allocates the space for nums2.
//The better solution for this question is storing everything from the largest number to
//smallest number.
//It won't cover the original number is because we put everything to the back and there are
//n free entries. If you want to replace the number in original nums1, you have to have at
//least n+1 elements there.


//Better Solution

class Solution{
    public void merge(int[] nums1, int m, int[] nums2, int n){
        int index = n+m-1;
        int in1 = m-1;  //index for nums1
        int in2 = n-1;  //index for nums2
        while(in1 >= 0  && in2 >= 0){   //Here also needs an equal sign, it is also legal when index eauqls to 0
            nums1[index--] = nums1[in1] > nums2[in2] ? nums1[in1--] : nums2[in2--]; // here is a colon!
            // this is so smart!!
            // after you get the value, decrease the index
        }
        //there are 2 different way to finish this while loop:
        //1. in1 = 0; which means it goes through all numbers from nums1, still
        //some number exists in nums2 don't add to nums1. Since it already sorted
        //just add a while loop to add all of them into nums1
        while(in2 >= 0 ){
            nums1[index--] = nums2[in2--];
        }

        //2. in2=0; which means it goes through all numbers from nums2, and all of them are
        // bigger than what nums1 currently pointing to. However nums1 is a sorted array
        // all numbers dont go through also sorted already, no need to worry about them.
    }
}