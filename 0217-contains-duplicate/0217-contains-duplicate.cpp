class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
            std::unordered_multimap<int, int> y;
            for (int i = 0; i < nums.size(); i++) {
                y.insert({nums[i],nums[i]});
                if (y.count(nums[i]) > 1) {return true;}
            }
            return false;
        /*
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (j == i) {
                    if ((j+1) == nums.size()) {
                        return false;
                    }
                    else {
                        j++;
                    }
                }
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
         }
         return false;
         */
    }
};