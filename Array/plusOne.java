class Solution {
    public int[] plusOne(int[] digits) {
        int i = 0;
        for(i=digits.length-1; i >=0 ; i--){    // only thing that need to remember is
            if(digits[i] == 9){                 // the inedx of first digits in an array
                digits[i] = 0;                  // is 0 and the last is length -1
            }
            else{
                digits[i] += 1;
                break;
            }
        }
        if(i == -1){
            int[] answer = new int[digits.length + 1];      //the size of array is determined at
            for(int j =answer.length-1 ; j>0; j--){         //runtime rather than compile time
                answer[j] =0;                               //it can use variable to define
            }
            answer[0] = 1;
            return answer;
        }
        return digits;
    }
}