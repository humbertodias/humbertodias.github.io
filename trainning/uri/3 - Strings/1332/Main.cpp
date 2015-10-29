#include <iostream>
#include <string>
using namespace std;

int main( ){

    int N; cin >> N;

    while(N--){

        string line;
        cin >> line;
        if(line.length() > 3)
            cout << 3 << endl;
        else
            if(line[0]=='o'||line[1]=='n'||line[2]=='e')
                cout << 1 << endl;
            else
                cout << 2 << endl;

    }

    return 0;

}