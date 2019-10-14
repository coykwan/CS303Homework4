// Brittney MacLennan, Coy Kwan, Ami Khalsa
// CS 303
// Homework #4, Question 2


#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <cctype>
#include <vector>

using namespace std;

int sumNum = 0;
int i = 0;

void to_number(string sum)
{


		if (i >= sum.length())

		{

			cout << sumNum << endl;

			i = 0;
			sumNum = 0;

			return;

		}

		if (isdigit(sum[i]))
		{
	
			sumNum += sum[i] - '0';
			i++;
			
		}

		else
		{
			sumNum += 0;
			i++;
		}

		to_number(sum);
}


int main()
{
	to_number("12c3a45");
	to_number("12");
	to_number("ccc123");
	
	cout << endl;

	system("pause");
    return 0;
}

