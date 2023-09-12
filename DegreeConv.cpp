#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){

    cout << setprecision(3) <<endl;
    double c = 0.0,f = 25.0;
    cout << "\t" << "Farenheit" << "\t\t" << "Celsius" <<endl;

    for(int i = 1;f <= 125; i++)
    {
        c = (5.0/9.0)*(f - 32);

        cout << "\t\t" << f <<"\t\t\t" << c <<endl;
        f++;
    }
    cout <<"\n"<<"Program coded by Eric L Saldana"<<"\n"<<endl;
    return 0;
}
