// Program Name:        Lab4a.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Lab 4
// Due Date:            06/18/2017

/* This program is a for loop that prints the Celsius temperatures for Fahrenheit temperatures 25 to 125.  C = 5/9(F – 32).  Output its given in a table format  */

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
                                                                                // Variables decalaration
    cout << setprecision(3) <<endl;
    double c = 0.0,f = 25.0;
    cout << "\t" << "Farenheit" << "\t\t" << "Celsius" <<endl;
                                                                                // Units conversion
    for(int i = 1;f <= 125; i++)
    {
        c = (5.0/9.0)*(f - 32);
        
        cout << "\t\t" << f <<"\t\t\t" << c <<endl;
        f++;
    }

    cout << "\nThis program was coded by Eric L Saldana" << endl;                 // e-signature
    cin.get();
    return 0;
}
