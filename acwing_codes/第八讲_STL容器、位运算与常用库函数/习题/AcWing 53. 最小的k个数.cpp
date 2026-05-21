class Solution {
public:
    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
        //只保持前K个数
        priority_queue<int> heap;
        for (auto x: input) {
            heap.push(x);
            if (heap.size() > k) heap.pop();
        }
        //把堆的元素压入vector
        vector<int> res;
        while(heap.size()) res.push_back(heap.top()), heap.pop();
        //堆是大根堆，需要逆序
        reverse(res.begin(), res.end());
        return res;
    }
};