class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        int i = 0; //indexes
        for (auto x: nums) {
            if (mp.find(target-x) != mp.end()) return {i,mp.at(target-x)};
            mp.insert({x,i});
            i++;
        }
        return {-1,-1};
    }
};