// Program Name:        Lab3.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Lab 3
// Due Date:            06/14/2017

/* This program can play “Rock, Paper, Scissors”.User inputs his/her choice – ‘R’, ‘S’, or ‘P’, then the computer generates its choice 
 randomly as an integer the numeric choice for the computer, converts (using a switch statement) it into a letter (‘R’, ‘S’, or ‘P’.)  
 and determines the winner of the game explaining: Rock crushes Scissors, Paper covers Rock, and Scissors cuts Paper
 
 */
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <time.h>
using namespace std;

int main()
{
    srand((unsigned)time(0));
    int num = (rand() % 3) + 1;
    
    string RPS[] = {"R","P","S"},comp;                              // Declare variables & arrays and to use in the program
    string computerGuess = RPS[num-1],userGuess;
    string legend[] = { "Paper covers Rock","Rock crushes Scissors","Scissors cuts Paper"};
    
    cout <<"Type in Paper(P), Rock(R) or Scissors(S) " << endl;     //Request user input
    cin >> userGuess;
    
    comp = computerGuess+userGuess;                                 //Create string array for use in program logic
    cout<< "Computer(" << comp[0] << ")  VS " << " You(" << comp[1]<<") \n"<<endl;
    
    switch(comp[0]+comp[1])                                         //Creates & compares an int number for unique (R,P,S) combination
    {
        case 162:
            cout << legend[0]<< endl;
            break;
        case 163:
            cout << legend[2]<< endl;
            break;
        case 165:
            cout << legend[1]<< endl;
            break;
    }
    
    if (userGuess == computerGuess)                                 //Condition for a draw event
    {
        cout <<"It's draw try again \n"<< endl;
    }
    else if (comp == "RP" || comp == "RS" || comp == "SP")
    {
        cout << "You win \n"<< endl;
    }
    else
    {
        cout << "Haha computer wins \n" << endl;
    }
    cout << "This program was coded by Eric L Saldana" << endl;	// e-signature
    cin.get();                                                  // stops the program to view the output until you type any character
    return 0;
}
