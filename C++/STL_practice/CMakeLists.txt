cmake_minimum_required(VERSION 3.17)
project(STL_practice)

set(CMAKE_CXX_STANDARD 17)

add_executable(STL_practice main.cpp LRUCache.cpp LRUCache.h tests.cpp tests.h)