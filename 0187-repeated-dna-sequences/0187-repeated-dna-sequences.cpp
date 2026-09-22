class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_set<string> seen;
        unordered_set<string> repeated;
        vector<string> ans;
        if (s.size() < 10)
            return ans;
        for (int i = 0; i <= s.size() - 10; i++) {
            string sub = s.substr(i, 10);
            if (seen.count(sub)) {
                repeated.insert(sub);
            } else {
                seen.insert(sub);
            }
        }
        for (auto &x : repeated) {
            ans.push_back(x);
        }
        return ans;
    }
};