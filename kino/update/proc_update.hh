vector<string> _update(string arg1, vector<string> arg2) {
 string v1 = arg1; // stored
 vector<string> v2 = arg2; // 2watch
 vector<string> v3 = {}; // updated-2watch
 // op(s)
 for (int i = 0; i < v2.size(); i++) {
  if (has(v1, v2[i])) continue;
  v3.push_back(v2[i]);
 }
 return v3;
}
