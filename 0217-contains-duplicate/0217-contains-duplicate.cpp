class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
            unordered_set<int> y;
            for (int i = 0; i < nums.size(); i++) {
                if (y.find(nums[i]) != y.end()) return true;
                y.insert(nums[i]);
            }
            return false;

    }
};