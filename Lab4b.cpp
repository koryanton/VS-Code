// Program Name:        Lab4b.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Lab 4
// Due Date:            06/18/2017


/*  This code reads in and total any number of positive integers terminated with a -1 as a sentinel.  Prints the average of the values after the loop is finished. And it does noy include negative values in the total or average.*/


#include <iostream>
#include <iomanip>
#include <stdio.h>

using namespace std;

int main()
{                                                                               // Set significant figures
    cout<<setprecision(5)<<endl;
                                                                                // Variables decalaration
    double num, tot = 0, c = 0;
                                                                                // User input request
    cout << "Type in the first quiz grade " << endl; ;
    cin >> num;
                                                                                // Degrees conversion calcualation
    while (num != -1 )
    {
        if (num >= 0)
        {
            tot += num;
            cout << "\nTotal \t"<<tot << endl;
            c++;
            cout << "Quizes \t"<< c <<"\n"<< endl;
            cout << "Type in the next quiz grade " << endl;;
            cin >> num;
        }
        else if (num < -2)
        {
            c--;
            num = 0;
        }

    }                                                                           // Print result

    cout << "\nThe average of all the quiz grades is: \n" << tot/c <<"\n"<< endl;


    cout << "This program was coded by Eric L Saldana" << endl;                 // e-signature
    cin.get();

    return 0;
}
