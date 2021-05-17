//
// Created by thoma on 2021-05-11.
//
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <numeric>


namespace lintcode_59 {
    using namespace std;
    class Solution {

    private:
        string codebase = "lintcode";
        int questionNum = 59;

    public:

        string outputInfo(){
            return "Solving " + this->codebase + to_string(this->questionNum);
        }

        /**
         * @param A: a string
         * @param B: a string
         * @return: return the sum of two strings
         */

        /**
         * @param numbers: Give an array numbers of n integer
         * @param target: An integer
         * @return: return the sum of the three integers, the sum closest target.
         */
        int threeSumClosest(vector<int> &numbers, int target) {
            // write your code here

            int l = numbers.size();
            if (l < 3){
                return accumulate(numbers.begin(), numbers.end(),0);
            }
            sort(numbers.begin(), numbers.end());
            int temp_sum;
            int closest_sum = numbers[0] + numbers[1] + numbers[2];

            int left, right;
            for (int i = 0; i < l-2;i++){
                left = i+1;
                right = l-1;
                while (left < right){
                    temp_sum = numbers[i] + numbers[left] + numbers[right];
                    if (temp_sum == target){
                        return target;
                    }
                    if (abs(target - temp_sum)<abs(target - closest_sum)){
                        closest_sum = temp_sum;
                    }
                    if (temp_sum < target){
                        left += 1;
                    }
                    else{ //temp_sum > target
                        right -= 1;
                    }
                }
            }
            return closest_sum;
        }
    };
}
