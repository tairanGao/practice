//
// Created by thoma on 2021-05-12.
//
#include <string>
#include <vector>
#include <unordered_map>


namespace lintcode_56 {
    using namespace std;
    class Solution {

        private:
            string codebase = "lintcode";
            int questionNum = 56;
        public:

            string outputInfo() {
                return "Solving " + this->codebase + to_string(this->questionNum);
            }

            /**
             * @param numbers: An array of Integer
             * @param target: target = numbers[index1] + numbers[index2]
             * @return: [index1 + 1, index2 + 1] (index1 < index2)
             */
            vector<int> twoSum(vector<int> &numbers, int target) {
                // write your code here
                int len = numbers.size();
                unordered_map<int, int> map;
                for (int i=0; i<len;i++){
                    if (map.count(target - numbers[i]) > 0){
                        return {map[target - numbers[i]], i};
                    }
                    else{
                        map[numbers[i]] = i;
                    }
                }

                return {};
            }
        };

}
