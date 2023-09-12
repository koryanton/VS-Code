// Program Name:        DayOfWeek.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Project 1
// Due Date:            06/14/2017

/* This program computes the day of the week for any date entered by the user.  The user will be prompted to enter a month, day, and 
 year.  The program will then display the day of the week for that date as a number between 0 and 6, where 0 represents Saturday and 6 
 represents Friday*/


#include <iostream>
#include <cmath>


using namespace std;

int main()
{                                                                               // Variables and strings declaration
    int q = 0,j = 0,k = 0,h = 0,m = 0;
    string week[] = {"Saturday","Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday"};
                                                                                // Request input from user
    cout<< "Please type month, day, century & year in that order"<< endl;
    cin >> m >> q >> j >> k ;
                                                                                // Fix for Jan, Feb & 2000 year
    if(k == 0)
    {
        j =19,k = 100;
        
    }
    if(m == 1)
    {
        m = 13 , k = k-1;
        
    }
    else if(m == 2)
    {
        m = 14 , k = k-1;
    }
                                                                                // Zeller's formula day calculation
    h = (q + 26*(m + 1)/10 + k + k/4 + j/4 + 5*j)%7;
    
    cout << "The day of the week is: "<< h << " / " << week[h]<<"\n"<< endl;
    
    cout << "This program was coded by Eric L Saldana" << endl;	// e-signature
    cin.get();                                                  // stops the program to view the output until you type any character
    return 0 ;
}

