#include <vector>
#include <iostream>
#include <string>
using namespace std;

/***
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
    ***/

class Solution {
public:
    

    vector<int> twoSum(vector<int> nums, int target) {
        for (int i = 0; i < nums.size(); i+=1) {
            for (int k = 0; k < nums.size(); k+=1) {
                if (k != i && nums[k] + nums[i] == target) {
                    vector<int> sum = { i,k };
                    return sum;
                }
                
            }
        }
        return nums;
    }

};

int main() {
    int target = 6;
    vector<int> nums = { 3,2,4 };
    vector<int> sum;

    Solution bap;
    sum = bap.twoSum(nums,target);
    for (int i = 0; i < sum.size(); i++) {
        cout << "finale" << sum[i];
    }

    return 0;
}
