#include<iostream>
#include<vector>
#include<string>
#include<cstdlib>
#include<fstream>
using namespace std;

vector<int> readfile(string fname){
  vector<int> all_value=vector<int>();
  ifstream datafile(fname.c_str());
  if (datafile.is_open()){
    string line;
    while(getline(datafile,line)){
      cout<<line<<endl;
      cout<<std::atoi(line.c_str())<<endl;
    }
    datafile.close();
  }
  return all_value;
}
int main(){
  vector<int> d;
  d=readfile("PA6-1test1.txt");
  return 0;
}
