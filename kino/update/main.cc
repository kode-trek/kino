#include "proc_update.hh"

int main(int argc, char* argv[1]) {
 string v1 = argv[1]; // stored
 string v2 = argv[2]; // 2watch
 vector<string> v3 = {};
 //
 v1 = cat(v1).txt;
 v3 = split(cat(v2).txt, "\n");
 enlist(_update(v1, unique(v3)), 0);
}
