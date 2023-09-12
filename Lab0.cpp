// Program Name:        Lab0.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Lab 0
// Due Date:            06/04/2017

/* This program takes two integers values which are passed to x and y and adds them together, then stores the result in the variable
 'z' and prints the result as well as 'x' and 'y' current stored values */

#include <iostream>
using namespace std;


int main()
{
    int x = 5, y = 6;                                           // Variable declarations
    int z;
    z = x + y;                                                  // Calculation
    cout << "x = " << x << "  & " << " y = "<< y << endl;       // Prints passed values to x & y
    cout << "The sum of x plus y = " << z << endl;              // Prints answer
    cout << " " << endl;
    cout << "This program was coded by Eric L Saldana" << endl;	// e-signature
    cin.get();                                                  // stops the program to view the output until you type any character
    return 0;
}
