#include <iostream>
#include <list>
#include <vector>
using namespace std;

int linear_search(vector<int>& items, int& target, size_t pos_last){
    if (pos_last == items.size()){
        return -1;
    }
    if (target == items[pos_last]){
        return pos_last;
    }
    else{
        return linear_search(items, target, pos_last - 1);
    }
}
