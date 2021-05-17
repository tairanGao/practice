//
// Created by thoma on 2021-05-11.
//
#include <string>
#include <unordered_map>

namespace lintcode_1870 {
    using namespace std;
    class Solution {

    private:
        string codebase = "lintcode";
        int questionNum = 1870;

    public:

        string outputInfo(){
            return "Solving " + this->codebase + to_string(this->questionNum);
        }

        /**
         * @param A: a string
         * @param B: a string
         * @return: return the sum of two strings
         */

        static int stringCount(string &str) {
            // Write your code here.
            int l = str.size();
            int num_zeros = 0, result = 0;
            for (int i=0;i<l;i++){
                if (str[i] == '0'){
                    num_zeros += 1;
                }else{
                    result += (0+num_zeros)*(num_zeros+1)/2;
                    num_zeros = 0;
                }
            }
            result += (0+num_zeros)*(num_zeros+1)/2;
            return result;
        }

    };
}
