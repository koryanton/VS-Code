#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
using namespace std;


int main()
{
  for (int i=2; i<200; i++)
  {
    bool prime=true;
    for (int j=2; j*j<=i; j++)
    {
      if (i % j == 0)
      {
        prime=false;
        break;
      }
    }
    if(prime) cout << i << " ";
  }
  return 0;
}
