// Program Name:        Lab4c.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Lab 4
// Due Date:            06/18/2017

#include <iostream>
#include <cmath>
#include <stdin.h>
using namespace std;

/* This program makes change for a customer. When the user inputs the amount of money put into a vending machine and the amount of the
 purchase and converts it inito cents. Subtracts the two values & determines the customer’s change in number of
quarters,dimes,nickels, and pennies, using integer arithmetic*/


int main(){
    char answer;
                                                                                // Do statement
    do
    {                                                                           // Variables decalrations
        double  cashIn,item = 0.0;
        int  change,i = 0, denom[i],coins[] = {25,10,5,1};
                                                                                // User input
        cout << "Please enter amount in cash" << endl;
        cin >> cashIn;
        cashIn *= 100;

        cout << "Please type in item price: "<<endl;
        cin >> item;
        item *= 100;
                                                                                // Transaction calculation
        change = cashIn-item;

        cout << "\nYour change is: "<<change << " cents \n" << endl;
                                                                                // Coins denomination logic & break apart
        while(change > 0)
        {
            denom[i] = change/coins[i];
            int rem = change % coins[i];
            change = rem;
            if (rem < coins[i])
            {
                i++;
            }
        }
                                                                                // Printed result
        cout<<denom[0]<<" Quarters  \n"<<denom[1]<<" Dimes \n"<<denom[2]<<" Nickels \n"<<denom[3]<<" Pennies \n"<<endl;
        cout << "Would you like to make another purchase? \nYES [y], NO [n]" <<endl;
        cin >> answer;
    }
    while (answer == 'y');

    cout << "This program was coded by Eric L Saldana" << endl;                 // e-signature
    cin.get();

    return 0;
}
