// This program computes the factors of an integer using Sieve method

#include <iostream>

using namespace std;

// Definition of the Sieve function
void sieve(int);

int main()
{
	int num;
	cout<<"Enter an integer: ";
	cin>>num;
	//int array[num];
	
	cout<<"The primes factors of "<<num<<" are: ";
	sieve(num);
}

void sieve(int a)
{
	int myArray[a];
	for (int i=1; i<=a; i++)
		myArray[i] = -1;
		
	for (int i=2; i<=a; i++)
	{
		if (myArray[i] == -1)
		{
			for (int j=i; j<=a; j+=i)
			{
				if (myArray[j] == -1)
					myArray[j] = i;
			}
		}
		
		
	}
	
	
	int k = a;
	while (k>1)
	{
		cout<<myArray[k]<<"  ";
		k/=myArray[k];
	}
		
}
