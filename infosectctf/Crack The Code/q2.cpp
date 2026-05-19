#include <iostream>
#include <vector>
#include <cassert>
#include <fstream>

using namespace std;

void zq(const vector<vector<double>>& x) {
    for (const auto& y : x) {
        for (double z : y) {
            cout << z << " ";
        }
        cout << endl;
    }
}

void kwd(const vector<vector<double>>& x, const string& p) {
    ofstream vq(p);

    if (!vq) {
        cerr << "Error opening file for writing!" << endl;
        exit(EXIT_FAILURE);
    }

    for (const auto& y : x) {
        for (double z : y) {
            vq << z << " ";
        }
        vq << endl;
    }

    vq.close();
}

vector<vector<double>> eqw(const vector<vector<double>>& x, const vector<vector<double>>& y) {
    int z = x.size();
    vector<vector<double>> qw(z, vector<double>(z, 0.0));

    for (int a = 0; a < z; a++) {
        for (int b = 0; b < z; b++) {
            for (int c = 0; c < z; c++) {
                qw[a][b] += x[a][c] * y[c][b];
            }
        }
    }

    return qw;
}

vector<vector<double>> rxw(const vector<vector<double>>& x) {
    int z = x.size();
    vector<vector<double>> qw(z, vector<double>(z));

    for (int a = 0; a < z; a++) {
        for (int b = 0; b < z; b++) {
            qw[a][b] = x[b][a];
        }
    }

    return qw;
}

vector<vector<double>> axj(const vector<vector<double>>& x) {
    int z = x.size();
    vector<vector<double>> hj(z, vector<double>(2 * z));

    for (int a = 0; a < z; a++) {
        for (int b = 0; b < z; b++) {
            hj[a][b] = x[a][b];
            hj[a][b + z] = (a == b) ? 1.0 : 0.0;
        }
    }

    for (int a = 0; a < z; a++) {
        double ajk = hj[a][a];
        if (ajk == 0) {
            cerr << "Matrix is singular, cannot invert!" << endl;
            exit(EXIT_FAILURE);
        }
        for (int b = 0; b < 2 * z; b++) {
            hj[a][b] /= ajk;
        }

        for (int b = 0; b < z; b++) {
            if (a != b) {
                double vwb = hj[b][a];
                for (int c = 0; c < 2 * z; c++) {
                    hj[b][c] -= hj[a][c] * vwb;
                }
            }
        }
    }

    vector<vector<double>> mwb(z, vector<double>(z));
    for (int a = 0; a < z; a++) {
        for (int b = 0; b < z; b++) {
            mwb[a][b] = hj[a][b + z];
        }
    }

    return mwb;
}

int main() {
    int z = 4;

    vector<vector<double>> q0 = {
        {3, 5, 1, 4},
        {9, 7, 8, 6},
        {6, 2, 7, 5},
        {8, 3, 4, 2}
    };

    vector<vector<double>> q1 = {
        {4, 7, 2, 3},
        {3, 6, 1, 4},
        {1, 2, 5, 7},
        {6, 1, 8, 9}
    };

    vector<vector<double>> q2 = {
        {10, 12, 14, 15},
        {6, 8, 2, 9},
        {4, 7, 3, 10},
        {11, 5, 1, 13}
    };

    vector<vector<double>> q3 = {
        {2, 1, 3, 6},
        {5, 4, 7, 8},
        {6, 7, 2, 3},
        {8, 6, 4, 1}
    };

    

    vector<vector<double>> q5 = {
        {102, 105, 110, 100},
        {116, 104, 105, 115},
        {102, 108, 97, 103},
        {000, 000, 000, 000}
    };

    vector<vector<double>> q6(z, vector<double>(z, 0.0));
    for (int a = 0; a < z; a++) {
        q6[a][a] = 1.0;
    }


    vector<vector<double>> q1l = rxw(q1);
    vector<vector<double>> q1ia = axj(q1l);
    vector<vector<double>> q2i = rxw(q2);
    vector<vector<double>> q2li = axj(q2i);

    vector<vector<double>> q7 = eqw(q5, q1);
    q7 = eqw(q7, q2);
    q7 = eqw(q7, q6);
    vector<vector<double>> q2M = axj(q2);
    q7 = eqw(q7, q2M);
    vector<vector<double>> q1W = axj(q1);
    q7 = eqw(q7, q1W);

    vector<vector<double>> q8 = eqw(q1ia, q2li);
    q8 = eqw(q8, q6);
    q8 = eqw(q8, q2);
    q8 = eqw(q8, q1);
    q8 = eqw(q8, q5);

    for (int a = 0; a < z; a++) {
        for (int b = 0; b < z; b++) {
            q7[a][b] += q8[a][b];
        }
    }

    kwd(q7, "q2_enc.txt");

    return 0;
}
