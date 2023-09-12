// Program Name:        Lab5.cpp
// Course:              CSE1311/Section 900
// Student Name:        Eric L Saldana
// Assignment Number:   Lab 5
// Due Date:            06/21/2017

/* This program reads data from a file, 3 values at a time, until it reaches sentinel the
data line.  Arranges the three values that have been read in order from lowest to highest,
and then writes the set of three numbers to an output file. When all lines of data have
been processed, it closes both files.  Then reopens the output file (file2) as input. reads
the data back in and prints it to the screen. */

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    double hold;                                          // Declare variables
    int first, second, last, m, n = 3,exe = 0;
        while (exe < 1 )
        {                                                 // .txt document read protocol
            ifstream fin("file1.txt");
            ofstream fout("file2.txt");
            fin >> first >> second >> last;               // Asigns values from file to variables
            cout << "Ordering numbers in file1: \n "<<endl;

                while (first != -1)                       // Ascending order sorting algorithm
                {
                    int x[] = {first,second, last};
                    for (int k = 0; k <= n - 2; k++)
                    {
                        m = k;
                        for (int j = k + 1; j <= n - 1; j++)
                        {
                            if (x[j] < x[m])
                                m = j;
                        }
                                hold = x[m];
                                x[m] = x[k];
                                x[k] = hold;
                    }

                    cout << x[0] <<"\t"<< x[1] <<"\t"<< x[2] <<endl;
                    fout << x[0] <<"\t"<< x[1] <<"\t"<< x[2] <<endl;
                    fin >> first >> second >> last;
                }
            fin.close();                                // Closes input open files
            fout.close();                               // Closes output open files
            cout << "End of task 1 \n"<<endl;
            exe++;                                      // Ends sorting algorithm
        }


    ifstream fin("file2.txt");                          // Opens recenlty created 'file2'
    fin >> first >> second >> last;                     // Asigns values from file to variables

    cout << "Printing file2:  \n "<<endl;               // Confirms that file2 is being read

        while (!fin.eof())                              // Prints file2 data to user's screen
        {
            fin >> first >> second >> last;
            cout << first <<"\t"<< second <<"\t"<< last <<"\t"<<endl;
        }
        fin.close();
    cout << "End of task 2 \n\n"<<endl;
    cout <<"Program coded by Eric L Saldana" <<endl;    // e-signature
    cin.get();
return 0;
}
