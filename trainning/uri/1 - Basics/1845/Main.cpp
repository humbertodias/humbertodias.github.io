#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

/*
 * 
 */

//p -> f
//s -> f
//j -> f
//v -> f;
//x -> f;
//b -> f;
//
int main(int argc, char** argv) {
    string str;
    while(getline(cin,str)){
        replace(str.begin(),str.end(),'p','f');
        replace(str.begin(),str.end(),'s','f');
        replace(str.begin(),str.end(),'v','f');
        replace(str.begin(),str.end(),'x','f');
        replace(str.begin(),str.end(),'b','f');
        replace(str.begin(),str.end(),'j','f');
        replace(str.begin(),str.end(),'z','f');
        replace(str.begin(),str.end(),'P','F');
        replace(str.begin(),str.end(),'S','F');
        replace(str.begin(),str.end(),'V','F');
        replace(str.begin(),str.end(),'X','F');
        replace(str.begin(),str.end(),'B','F');
        replace(str.begin(),str.end(),'J','F');
        replace(str.begin(),str.end(),'Z','F');
        string str2;
        for(unsigned int i=0;i<str.size();){
            char f = str[i];
            while(i<str.size() && tolower(str[i])=='f' && tolower(str[i+1])=='f'){
                i++;
            }
            str2.push_back(f);
            i++;
        }
        cout << str2 << "\n";
    }
    return 0;
}