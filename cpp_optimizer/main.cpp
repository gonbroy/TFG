#include <iostream>
#include <vector>
#include <string>

int main(int argc, char* argv[]) {

    if (argc < 2) {
        std::cerr << R"({"error":"Usage: optimizer ORIGIN DEST1 DEST2 ..."})";
        return 1;
    }

    auto strip_quotes = [](std::string s){
        while (!s.empty() && (s.front() == '"' || s.front() == '\'')) {
            s.erase(s.begin());
        }
        while (!s.empty() && (s.back() == '"' || s.back() == '\'')) {
            s.pop_back();
        }
        return s;
    };

    std::string origin = strip_quotes(argv[1]);

    std::vector<std::string> dests;
    for (int i = 2; i < argc; ++i) {
        dests.push_back(strip_quotes(argv[i]));
    }

    std::cout << R"({"route":[)";
    std::cout << "\"" << origin << "\"";

    for (const auto& d : dests) {
        std::cout << ",\"" << d << "\"";
    }

    std::cout << R"(],"estimated_cost":123,"note":"C++ optimizer MVP"})";

    return 0;
}
