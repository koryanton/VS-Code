// Program Name:        Lab2.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Lab 2
// Due Date:            06/07/2017


#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
    const double PI= 3.1415927;
    double radius, volume, surface;
    
    cout << "Please type the radius 'r'" <<endl;
    cin >> radius;
    
    volume = 4.0/3.0*PI*pow(radius,3);
    surface = 4*PI*pow(radius,2);
    
    cout<< "Radius = "<< radius <<endl;
    cout<< "Voulume = "<< volume <<endl;
    cout<< "Surface area = "<< surface <<endl;
    
    cout<< fixed <<endl;
    cout<< "Radius = "<< radius <<endl;
    cout<< "Voulume = "<< volume <<endl;
    cout<< "Surface area = "<< surface <<endl;
    
    cout<< setprecision(3) <<endl;
    cout<< "Radius = "<< radius <<endl;
    cout<< "Voulume = "<< volume <<endl;
    cout<< "Surface area = "<< surface <<endl;
    
    
    cout<< scientific << setprecision(4) <<endl;
    cout<< "Radius = "<< radius <<endl;
    cout<< "Voulume = "<< volume <<endl;
    cout<< "Surface area = "<< surface <<endl;
    
    cout << "This program was coded by Eric L Saldana" << endl;	// e-signature
    cin.get();
    return 0;
}
