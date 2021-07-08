//
// Created by thoma on 2021-05-11.
//
#include <iostream>
#include <memory>

#include "all.h"


int main()
{
    std::cout << "Starting ---------------" <<std::endl;
//    auto sol_1343 = std::make_shared<lintcode_1343::Solution>();
//    std::cout << sol_1343->outputInfo() <<std::endl;
//    std::string A = "555552";
//    std::string B = "321";
//    std::cout << sol_1343->SumofTwoStrings(A, B) <<std::endl;

//    auto sol_64 = std::make_shared<lintcode_64::Solution>();
//    std::cout << sol_64->outputInfo() <<std::endl;

//    auto sol_56 = std::make_shared<lintcode_56::Solution>();
//    std::cout << sol_56->outputInfo() <<std::endl;
//    std::vector<int> numbers = {2,7,11,15};
//    int target = 17;
//    auto result =sol_56->twoSum(numbers, target);
//    for (auto i: result)
//        std::cout << i << ' ';
//    std::cout << std::endl;
//
//
//    auto sol_1870= std::make_shared<lintcode_1870::Solution>();
//    std::cout << sol_1870->outputInfo() <<std::endl;
//    std::string input = "00000000000000";
//    std::cout << sol_1870->stringCount(input) <<std::endl;



//    auto sol_59= std::make_shared<lintcode_59::Solution>();
//    std::cout << sol_59->outputInfo() <<std::endl;
//    std::vector<int> input = {};
//    std::cout << sol_59->threeSumClosest(input, -5) <<std::endl;

//    auto sol_1357= std::make_shared<lintcode_1357::Solution>();
//    std::cout << sol_1357->outputInfo() <<std::endl;
//    std::string input = "abcabcabcabc";
//    std::cout <<sol_1357->kDistinctCharacters(input, 3) <<std::endl;


//    auto sol_610= std::make_shared<lintcode_610::Solution>();
//    std::cout << sol_610->outputInfo() <<std::endl;
//    std::vector<int> input = {0,5,7,7};
//
//    auto result =sol_610->twoSum7(input, -2);
//    for (auto i: result)
//        std::cout << i << ' ';
//    std::cout << std::endl;




    auto sol_574= std::make_shared<lintcode_574::Solution>();
    std::cout << sol_574->outputInfo() <<std::endl;
    std::vector<std::vector<int>> grid = {{0,1,0,0}, {1,0,1,1},{0,1,0,0}};
    std::cout <<sol_574->shortestDistance(grid) <<std::endl;








}
