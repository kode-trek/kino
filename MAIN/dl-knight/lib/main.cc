void f1(string &str, const string& from, const string& to) {
 size_t start_pos = 0;
 while((start_pos = str.find(from, start_pos)) != std::string::npos) {
  str.replace(start_pos, from.length(), to);
  // Handles case where 'to' is a substring of 'from'
  start_pos += to.length();
 }
}

int main(int argc, char* argv[]) {
 /* variable(s)
 [v1] web-page-URL
 [v2] list-text
 [v3] list-zip
 [cmd] color-command
 [out] color-output
 [cmd] color-error/warning
 */
 string inp = color("blue", "[inp] ");
 string cmd = color("blue", "[] ");
 string out1 = color("blue", "[out] ");
 string out2 = color("green", "DONE.");
 string err1 = color("yellow", "[WARNING] ");
 string err2 = color("red", "HALTED.""\n""[FAILED] ");
 //
 if (argc < 2) {
  cout << err1 + "needs 1 argument. 0 provided." << endl;
  exit(1);
 }
 //
 string v1 = argv[1];
 abbr(v1);
 if (dir(v1)) {
  cout << err1 + "needs URL. Directory provided." << endl;
  exit(1);
 }
 if (v1.find("http") == string::npos) {
  cout <<
  inp + v1 + "\n" +
  err1 + "URL starts with \"http\"."
  << endl;
 } else cout << inp + v1 << endl;
 if (exist(v1)) {
  sys("sudo cp " + quote(v1) + " /var/www/html/dl-knight");
  v1 = "http://127.0.0.1/dl-knight/" + uri(v1)[1];
 }
 f1(v1, "/", "\\/");
 string v2 = "list.txt";
 string v3 = "list_" + ts() + ".zip";
 // message(s)
 string msg1 =
 out1 + v3 + "\n" +
 cmd + "collecting all link(s) in page...";
 // command(s)
 int e = 0;
 string cmd1 =
 "sed 's/http:\\/\\/127.0.0.1\\//" + v1 + "/g' spider-1.py > spider-2.py";
 string cmd2 = "scrapy runspider spider-2.py -o list.jl";
 string cmd3 = "scrapy runspider spider-2.py -o list.json";
 string cmd4 = "python3 enlist.py " + v2;
 string cmd5 = "zip -y -q -r " + v3 + " list.json " + v2;
 // op(s)
 sys("sudo '' 2>/dev/null");// traps sudo-password
 disp(msg1);
 e = sys(cmd1 + " 2>/dev/null");
 if (e) {
  cout << err2 + cmd1 << endl;
  exit(1);
 }
 e = sys(cmd2 + " 2>/dev/null");
 if (e) {
  cout << err2 + cmd2 << endl;
  exit(1);
 }
 e = sys(cmd3 + " 2>/dev/null");
 if (e) {
  cout << err2 + cmd3 << endl;
  exit(1);
 }
 e = sys(cmd4 + " 2>/dev/null");
 if (e) {
  cout << err2 + cmd4 << endl;
  exit(1);
 }
 e = sys(cmd5 + " 2>/dev/null");
 if (e) {
  cout << err2 + cmd5 << endl;
  exit(1);
 }
 rm("__pycache__");
 rm("list.jl");
 rm("list.json");
 rm("spider-2.py");
 sys("sudo rm -rf " + v1);
 rm(v2);
 cout << out2 << endl;
}
