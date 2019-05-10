class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int>::iterator it = nums.begin();
        if(it == nums.end()){
            return 0;
        }
        it ++;
        vector<int>::iterator it_index = nums.begin();
        int CountReturnNum = 0;
        int CurrentNumCount = 1;
        int CurrentNum = *(nums.begin());
        for(it = it; it != nums.end(); it++){
            if((*it) == (*(it - 1))){
                if(CurrentNumCount < 2){
                    CurrentNumCount ++;
                }
            }
            else{
                for(int AddNewNumber = 0; AddNewNumber < CurrentNumCount; AddNewNumber ++){
                    *it_index = CurrentNum;
                    it_index ++;
                    CountReturnNum ++;
                }
                CurrentNumCount = 1;
                CurrentNum = *it;
            }
        }
        
        for(int AddNewNumber = 0; AddNewNumber < CurrentNumCount; AddNewNumber ++){
            *it_index = CurrentNum;
            it_index ++;
            CountReturnNum ++;
        }
        
        return CountReturnNum;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

string integerVectorToString(vector<int> list, int length = -1) {
    if (length == -1) {
        length = list.size();
    }

    if (length == 0) {
        return "[]";
    }

    string result;
    for(int index = 0; index < length; index++) {
        int number = list[index];
        result += to_string(number) + ", ";
    }
    return "[" + result.substr(0, result.length() - 2) + "]";
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> nums = stringToIntegerVector(line);
        
        int ret = Solution().removeDuplicates(nums);

        string out = integerVectorToString(nums, ret);
        cout << out << endl;
    }
    return 0;
}