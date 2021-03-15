//
// Created by Tairan Gao on 2021-03-15.
//

#ifndef STL_PRACTICE_LRUCACHE_H
#define STL_PRACTICE_LRUCACHE_H

#include <list>
#include <unordered_map>
#include <iostream>


template <class K, class V>
class LRUCacheTemplate {
public:
    /*
    * @param capacity: An integer
    */
    explicit LRUCacheTemplate(int capacity) : capacity(capacity), current_cap(0){
        _map.reserve(capacity);
    };


    /*
     * @param key: An integer
     * @return: An integer
     */
    V get(const K& key);

    /*
     * @param key: An integer
     * @param value: An integer
     * @return: nothing
     */
    void set(int key, int value);

private:
    int capacity;
    int current_cap;
    std::unordered_map<K, std::pair<V, typename std::list<K>::iterator>> _map;
    std::list<K> _list;

};


class LRUCache {
public:
    explicit LRUCache(int capacity) : lru(capacity) {}

    int get(int key) {
        return lru.get(key);
    }

    void set(int key, int value) {
        lru.set(key, value);
    }

private:
    LRUCacheTemplate<int, int> lru;
};


#endif //STL_PRACTICE_LRUCACHE_H
