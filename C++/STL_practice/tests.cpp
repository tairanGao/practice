//
// Created by Tairan Gao on 2021-03-15.
//

#include "tests.h"
#include "LRUCache.h"

void test_LRUCache() {
    auto cache = LRUCache(2);
    cache.set(2, 1);
    cache.set(1, 1);
    std::cout << cache.get(2) << std::endl;
    cache.set(4, 1);
    std::cout << cache.get(1)<< std::endl;
    std::cout << cache.get(2)<< std::endl;
}

