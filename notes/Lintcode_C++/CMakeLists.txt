cmake_minimum_required(VERSION 3.13)  # CMake version check
project(simple_example)               # Create project "simple_example"
set(CMAKE_CXX_STANDARD 17)            # Enable c++14 standard

# Add main.cpp file of project root directory as source file
set(SOURCE_FILES main.cpp)

# Add executable target with source files listed in SOURCE_FILES variable
add_executable(lintcode_practice
        main.cpp
        1343_SumofTwoStrings.cpp
        64_MergeSortedArray.cpp
        56_TwoSum.cpp
        1870_NumberofSubstringswithAllZeroes.cpp
        59_3SumClosest.cpp
        1375_SubstringWithAtLeastKDistinctCharacters.cpp
        610_TwoSumDifferenceEqualsToTarget.cpp
        all.h
        )