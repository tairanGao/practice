//
// Created by thoma on 2021-05-11.
//
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>


namespace lintcode_1357 {
    using namespace std;
    class Solution {

    private:
        string codebase = "lintcode";
        int questionNum = 1357;

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
        long long kDistinctCharacters(string &s, int k) {
            // Write your code here
            long long l = s.size();
            long long output = 0;
            long long dict_size = 0;
            if (k <= 1){
                return (1+l)*l/2;
            }
            auto dict = set<char>();
            for (int i=0;i<l;i++){
                dict_size = 0;
                dict.clear();
                dict.emplace(s[i]);
                dict_size += 1;
                for (int j=i+1;j<l;j++){
                    if (dict.count(s[j]) == 0){
                        dict.emplace(s[j]);
                        dict_size += 1;
                    }
                    if (dict_size == k){
                        output += l - j;
                        break;
                    }
                }
            }
            return output;
        }
    };
}
