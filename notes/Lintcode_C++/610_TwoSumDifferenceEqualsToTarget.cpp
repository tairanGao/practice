//
// Created by thoma on 2021-05-11.
//
#include <string>
#include <unordered_map>

namespace lintcode_610 {
    using namespace std;
    class Solution {

    private:
        string codebase = "lintcode";
        int questionNum = 610;

    public:

        string outputInfo(){
            return "Solving " + this->codebase + to_string(this->questionNum);
        }

        /**
         * @param nums: an array of Integer
         * @param target: an integer
         * @return: [num1, num2] (num1 < num2)
         */
        vector<int> twoSum7(vector<int> &nums, int target) {
            // write your code here
            int l = nums.size();
            if (l < 2) {
                return {};
            }
            int left = 0, right = 1, diff;
            while (right < l) {
                diff = nums[right] - nums[left];
                if (diff == target) {
                    return {min(nums[left], nums[right]), max(nums[left], nums[right])};
                }
                if (diff < target) {
                    right += 1;
                    if (right == left){
                        right += 1;
                    }
                    continue;
                } else {
                    left += 1;
                    if (left == right){
                        left += 1;
                    }
                    continue;
                }
            }
            return {};
        }
    };
}
