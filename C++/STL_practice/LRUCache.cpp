//
// Created by Tairan Gao on 2021-03-15.
//

#include "LRUCache.h"


template<class K, class V>
V LRUCacheTemplate<K, V>::get(const K &key) {
    int value;
    auto map_it = _map.find(key);
    if (map_it != _map.end()){ // key exist
        value = map_it->second.first;
        auto list_it = map_it->second.second;
        _list.splice( _list.end(), _list, list_it);
        return value;
    }else{
        return -1;
    }
}

template<class K, class V>
void LRUCacheTemplate<K, V>::set(int key, int value){

    auto map_it = _map.find(key);
    if (map_it != _map.end()){ // key exist
        map_it->second.first = value;
        _list.splice( _list.end(), _list, map_it->second.second );
        return;
    }
    //key does not exist

    if (current_cap == capacity){//cap full, need to remove one
        auto delete_key = _list.front();
        _map.erase(delete_key);
        _list.pop_front();
        current_cap -= 1;
    }

    // insert new key and value
    _list.push_back(key);
    auto list_it = std::prev(_list.end());
    std::pair<V, typename std::list<K>::iterator> _pair = std::make_pair(value, list_it);

    auto result = _map.emplace(key, _pair);
    if (!result.second){
        std::cerr << "key exist" << std::endl;
        return; // shouldn't be here
    }
    current_cap += 1;
}

// Explicit template instantiation
template class LRUCacheTemplate<int,int>;