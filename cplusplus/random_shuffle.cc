// Compiled with: g++ -Wall -std=c++14 -pthread

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int a[]={0,1,2,3,4,5,6,7,8,9};

    random_shuffle(std::begin(a), std::end(a));
    for (unsigned int i=0; i<(sizeof(a)/sizeof(a[0])); i++) {cout << a[i] << ",";}
    cout << endl;

    random_shuffle(std::begin(a), std::end(a));
    for (unsigned int i=0; i<(sizeof(a)/sizeof(a[0])); i++) {cout << a[i] << ",";}
    cout << endl;

    random_shuffle(std::begin(a), std::end(a));
    for (unsigned int i=0; i<(sizeof(a)/sizeof(a[0])); i++) {cout << a[i] << ",";}
    cout << endl;

    random_shuffle(std::begin(a), std::end(a));
    for (unsigned int i=0; i<(sizeof(a)/sizeof(a[0])); i++) {cout << a[i] << ",";}
    cout << endl;
}
