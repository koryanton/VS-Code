// Program Name:        Lab1.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Lab 1
// Due Date:            06/07/2017

/* This program takes two integers values which are passed to h and b which represent de base &
 heigth respectively of a triangle to output the area 'a' */

#include <iostream>
using namespace std;


int main(){
    float h,b,a;                                                                    // Declare variables of type float
    
    cout<< "Please enter the base 'b' and the height 'h' of your triangle: "<<endl; // Request user for height & base values
    cin >> b >> h;                                                                  // Pass input values to h & b
    
    cout<< "Base = "<<b<< ", Height = "<<h<< endl;                                  // Confirm values to the user
    
    a = (h*b)/2;                                                                    // Calculate using the area formula of a triangle
    
    cout<< "The area of your triangle is:  " << a << " square units " << endl;      // Output result to user
    cout<<""<<endl;
    
    cout << "This program was coded by Eric L Saldana" << endl;                     // e-signature
    cin.get();                                                                      // Pause
    return 0;
    
}
