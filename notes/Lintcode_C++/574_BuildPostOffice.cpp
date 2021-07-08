//
// Created by thoma on 2021-05-11.
//
#include <string>
#include <vector>
#include <set>
#include <utility>
#include <unordered_map>


namespace lintcode_574 {
    using namespace std;
    typedef pair<int, int> pairs;

    class Solution {

    private:
        string codebase = "lintcode";
        int questionNum = 574;

    public:

        string outputInfo(){
            return "Solving " + this->codebase + to_string(this->questionNum);
        }

        /**
         * @param grid: a 2D grid
         * @return: An integer
         */
        int shortestDistance(vector<vector<int>> &grid) {
            // write your code here
            int row = grid.size();
            if (row <= 0) return -1;
            int col = grid[0].size();
            if (col <= 0) return -1;

            set<pairs> empty_loc;
            unordered_map<int, int> x, y;
            for (int i=0; i<row;i++){
                for (int j=0;j<col;j++){
                    if (grid[i][j]) {
                        if (x.count(i) == 0)
                            x[i] = 1;
                        else
                            y[i] += 1;

                        if (y.count(j) == 0)
                            y[i] = 1;
                        else
                            y[i] += 1;
                    }
                    else
                        empty_loc.emplace(make_pair(i,j));
                }
            }
            int result = -1, temp_result = 0;
            for (auto potential:empty_loc){
                for (auto house:houses){
                    temp_result += abs(house.first - potential.first);
                    temp_result += abs(house.second - potential.second);
                }
                if (temp_result <= 0) continue;
                if (result < 0) result = temp_result;
                else result = min(result, temp_result);
                temp_result = 0;
            }

            return result;

        }

    };
}
