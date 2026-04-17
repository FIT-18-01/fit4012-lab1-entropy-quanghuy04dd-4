#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <cmath>

using namespace std;

double calculate_entropy(const string &text) {
    if (text.empty()) {
        return 0.0;
    }

    map<int, int> freq;
    for (char c : text) {
        freq[static_cast<unsigned char>(c)]++;
    }

    double entropy = 0.0;
    for (const auto &pair : freq) {
        double p = static_cast<double>(pair.second) / text.size();
        entropy -= p * (log(p) / log(2.0));
    }
    return entropy;
}

double calculate_redundancy(const string &text, int alphabet_size = 256) {
    if (text.empty() || alphabet_size <= 1) {
        return 0.0;
    }

    double entropy = calculate_entropy(text);
    double max_entropy = log(static_cast<double>(alphabet_size)) / log(2.0);
    double redundancy = max_entropy - entropy;
    return redundancy >= 0.0 ? redundancy : 0.0;
}

int main() {
    string input;
    cout << "Enter a string of characters: ";
    getline(cin, input);

    double entropy = calculate_entropy(input);
    double redundancy = calculate_redundancy(input, 256);

    cout << fixed << setprecision(4);
    cout << "Entropy: " << entropy << '\n';
    cout << "Redundancy: " << redundancy << '\n';
    return 0;
}
