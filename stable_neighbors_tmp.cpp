#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

// #define DEBUG

#ifdef DEBUG
#define fin cin
#define fout cout
#else
ifstream fin("stable_neighbors.input.txt");
ofstream fout("stable_neighbors.output.txt");
#endif

string create_pairs(string color, int count) {
    string result = "";
    string pair = "";
    if (color == "R") { pair = "GR"; }
    else if (color == "Y") { pair = "VY"; }
    else { pair = "OB"; }
    for (int i = 0; i < count; ++i) {
        result += pair;
    }
    return result;
}

void replace_color(string& result, string color, int count) {
    if (count <= 0) { return; }
    string pairs = create_pairs(color, count);
    if (!result.empty()) {
        int idx = result.find(color);
        result.replace(idx, 1, color + pairs);
    }
    else {
        result = pairs;
    }
    //return result;
}

string solve(int N, int R, int O, int Y, int G, int B, int V) {
    /* 
        Note: O should be surrounded by B, G should be surrounded by R, 
        V should be surrounded by Y. Therefore, this can be converted to
        problem with just 3 main colors R, Y , B. E.g RGR, YVY, BOB. 
    */
    // Check if it's possible
    if (
            O > B || G > R || V > Y ||
            (O == B && B > 0 && (Y > 0 || R > 0)) || 
            (G == R && R > 0 && (Y > 0 || B > 0)) || 
            (V == Y && Y > 0 && (R > 0 || B > 0))) {
        return "IMPOSSIBLE";
    }
    // if (G > 0 && G == R) {
    //     string result = "";
    //     for (int i = 0; i < G; ++i) {
    //         result += "RG";
    //     }
    //     return result;
    // }
    // if (V > 0 && V == Y) {
    //     string result = "";
    //     for (int i = 0; i < V; ++i) {
    //         result += "YV";
    //     }
    //     return result;
    // }
    // if (O > 0 && O == B) {
    //     string result = "";
    //     for (int i = 0; i < O; ++i) {
    //         result += "BO";
    //     }
    //     return result;
    // }
    // Merge R&G, Y&V, B&O and update R, Y, B because RGRG...R is equivalent to R
    R -= G; Y -= V; B -= O;
    // Make vector of unicorns
    vector<pair<int, string>> unicorns = {
        make_pair(R, "R"), make_pair(Y, "Y"), make_pair(B, "B")};
    // Sort unicorns by descending order
    sort(unicorns.rbegin(), unicorns.rend());
    // Check if its possible for circular stable
    if (unicorns[0].first > unicorns[1].first + unicorns[2].first) {
        return "IMPOSSIBLE";
    }
    vector<string> stable(unicorns[0].first, unicorns[0].second);
    for (int i = 0; i < unicorns[1].first + unicorns[2].first; ++i) {
        if (i < unicorns[1].first) {
            stable[i % unicorns[0].first] += unicorns[1].second;
        }
        else {
            stable[i % unicorns[0].first] += unicorns[2].second;
        }
    }
    // Combine stable vector into a single string
    string result = "";
    for (int i = 0; i < stable.size(); ++i) {
        result += stable[i];
    }

    replace_color(result, "R", G);
    replace_color(result, "Y", V);
    replace_color(result, "B", O);

    // // Replace R with group RG..R if exists
    // int R_idx = result.find("R");
    // if (R_idx != string::npos) {
    //     string RG_group = "R";
    //     for (int i = 0; i < G; ++i) {
    //         RG_group += "GR";
    //     }
    //     result.replace(R_idx, 1, RG_group);
    // }
    // // Replace Y with group YV..Y if exists
    // int Y_idx = result.find("Y");
    // if (Y_idx != string::npos) {
    //     string YV_group = "Y";
    //     for (int i = 0; i < V; ++i) {
    //         YV_group += "VY";
    //     }
    //     result.replace(Y_idx, 1, YV_group);
    // }
    // // Replace B with group BO..B if exists
    // int B_idx = result.find("B");
    // if (B_idx != string::npos) {
    //     string BO_group = "B";
    //     for (int i = 0; i < O; ++i) {
    //         BO_group += "OB";
    //     }
    //     result.replace(B_idx, 1, BO_group);
    // }
    return result;
}

bool verify(int N, string result) {
    /* Check to see if the result is corrrect */
    if (result == "IMPOSSIBLE") {
        return true;
    }
    if (N != result.size()) {
        cout << "Result length is wrong!" << endl;
        return false;
    }
    // Check for the case with R, Y, B only
    for (int i = 1 ; i < N; ++i) {
        if (result[i] == result[i-1] or result[i] == result[(i+1) % N]) {
            return false;
        }
    }
    return true;
}

int main() {
    int T; fin >> T;
    for (int c =1; c <= T; c++) {
        int N, R, O, Y, G, B, V;
        fin >> N >> R >> O >> Y >> G >> B >> V;
        string result = solve(N, R, O, Y, G, B, V);
        fout << "Case #" << c << ": " << result << endl;
    }
    return 0;
}
