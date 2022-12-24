int main(int argc, char* argv[]) {
 string v1 = argv[1];
 string v2 = argv[2];
 string v3 = "";
 vector<string> v4 = {};
 FILE *v5 = NULL;
 if (v1 == "--add") {
  v3 = cat("wish").txt;
  v3 += v2;
  v4 = split(v3, "\n");
  v4 = unique(v4);
  v5 = fopen("wish2", "a");
  for (int i = 0; i < v4.size(); i++) fprintf(v5, "%s\n", v4[i].c_str());
  fclose(v5);
  rm("wish");
  mv("wish2", "wish");
//  drop("wish", v2 + "\n");
  cout << mark("blue", "[OK] ") + "item added to wish-list." << endl;
 }
}
