//
// Created by thoma on 2021-05-11.
//
#include <string>

namespace lintcode_1343 {
    using namespace std;
    class Solution {

    private:
        string codebase = "lintcode";
        int questionNum = 1343;

    public:

        string outputInfo(){
            return "Solving " + this->codebase + to_string(this->questionNum);
        }

        /**
         * @param A: a string
         * @param B: a string
         * @return: return the sum of two strings
         */

        string SumofTwoStrings(string &A, string &B) {
            // write your code here
            int num_A, num_B, result;
            int lenA = A.size(), lenB = B.size();
            string output;
            output = "";
            int i_A = lenA - 1, i_B = lenB - 1;

            while (i_A>=0 && i_B>=0){
                num_A = int(A[i_A]) - int('0');
                num_B = int(B[i_B]) - int('0');
                result = num_A + num_B;
                output = to_string(result) + output;

                i_A -= 1;
                i_B -= 1;
            }
            if(i_A >= 0) output = A.substr(0, i_A + 1) + output ;
            if(i_B >= 0) output = B.substr(0, i_B + 1) + output;
            return output;
        }
    };
}
