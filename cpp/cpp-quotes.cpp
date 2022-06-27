#include <iostream>
int main() {
    int arr1[10];
    const int n = 10;
    int arr2[n];
    return 0;
}
// source
// geeksforgeeks - Arrays
// code
int main() { int arr[6] = {10, 20, 30, 40}; }
// source
// geeksforgeeks - Arrays
// code
#include <stdio.h>
int main() {
    int arr[5];
    arr[0] = 5;
    arr[2] = -10;
    arr[3 / 2] = 2;
    arr[3] = arr[0];
    printf("%d %d %d %d", arr[0], arr[1], arr[2], arr[3]);
    return 0;
}
// source
// geeksforgeeks - Arrays
// code
#include <iostream>
using namespace std;
int main() {
    int x[3][2] = {{0, 1}, {2, 3}, {4, 5}};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            cout << "Element at x[" << i << "][" << j << "]: ";
            cout << x[i][j] << endl;
        }
    }
    return 0;
}
// source
// geeksforgeeks - Multidimensional Arrays
// code
#include <cstring>
#include <iostream>
using namespace std;
int main() {
    char str[] = "This is a string";
    char *ch = strrchr(str, 'a');
    cout << ch - str + 1;
    return 0;
}
// source
// geeksforgeeks - strrchr() function in C/C++
// code
#include <iostream>
int max(int x, int y) {
    if (x > y)
        return x;
    else
        return y;
}
// source
// geeksforgeeks - Functions in C/C++
// code
#include <iostream>
using namespace std;
int main() {
    int a = 10, b = 20;
    int m = max(a, b);
    cout << "m is " << m;
    return 0;
}
// source
// geeksforgeeks - Functions in C/C++
// code
void fun(int x) { x = 30; }
// source
// geeksforgeeks - Functions in C/C++
// code
void fun(int *ptr) { *ptr = 30; }
// source
// geeksforgeeks - Functions in C/C++
// code
class CImage {
public:
    CImage();
    ~CImage();
    struct SImageInfo *pImageInfo;
    void Rotate(double angle);
    void Scale(double scaleFactorX, double scaleFactorY);
    void Move(int toX, int toY);
private:
    void InitImageInfo();
};
// source
// geeksforgeeks - Opaque Pointer
// code
#include <iostream>
using namespace std;
void swap(int &first, int &second) {
    int temp = first;
    first = second;
    second = temp;
}
// source
// geeksforgeeks - References
// code
struct Student {
    string name;
    string address;
    int rollNo;
};
// source
// geeksforgeeks - References
// code
void print(const Student &s) {
    cout << s.name << "  " << s.address << "  " << s.rollNo << '\n';
}
// source
// geeksforgeeks - References
// code
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> vect{10, 20, 30, 40};
    for (int &x : vect) {
        x = x + 5;
    }
    for (int x : vect) {
        cout << x << " ";
    }
    cout << '\n';
    return 0;
}
// source
// geeksforgeeks - References
// code
int &fun() {
    static int x = 10;
    return x;
}
// source
// geeksforgeeks - References
// code
int fun(int &x) { return x; }
// source
// geeksforgeeks - References
// code
class Test {
private:
    int x;
public:
    void setX(int x) { this->x = x; }
    void print() { cout << "x = " << x << endl; }
};
// source
// geeksforgeeks - 'this' pointer in C++
// code
Test &Test::func() {
    // Some processing
    return *this;
}
// source
// geeksforgeeks - 'this' pointer in C++
// code
class Test {
private:
    int x;
public:
    Test(int x = 0) { this->x = x; }
    void change(Test *t) { this = t; }
    void print() { cout << "x = " << x << endl; }
};
// source
// geeksforgeeks - 'this' pointer in C++
// code
class person {
    char name[20];
    int id;
public:
    void getdetails() {}
};
// source
// geeksforgeeks - Object Oriented Programming in C++
// code
class Geeks {
public:
    string geekname;
    void printname() { cout << "Geekname is: " << geekname; }
};
// source
// geeksforgeeks - C++ Classes and Objects
// code
class Geeks {
public:
    int id;
    ~Geeks() { cout << "Destructor called for id: " << id << endl; }
};
// source
// geeksforgeeks - C++ Classes and Objects
// code
int main() {
    Geeks obj1;
    obj1.id = 7;
    int i = 0;
    while (i < 5) {
        Geeks obj2;
        obj2.id = i;
        i++;
    }
    return 0;
}
// source
// geeksforgeeks - C++ Classes and Objects
// code
class Person {
    int id;
    char name[100];
public:
    void set_p();
    void display_p();
};
void Person::set_p() {
    cout << "Enter the Id:";
    cin >> id;
    fflush(stdin);
    cout << "Enter the Name:";
    cin.get(name, 100);
}
// source
// geeksforgeeks - Inheritance in C++
// code
void Person::display_p() { cout << endl << id << "\t" << name; }
// source
// geeksforgeeks - Inheritance in C++
// code
class Student : private Person {
    char course[50];
    int fee;
public:
    void set_s();
    void display_s();
};
// source
// geeksforgeeks - Inheritance in C++
// code
void Student::set_s() {
    set_p();
    cout << "Enter the Course Name:";
    fflush(stdin);
    cin.getline(course, 50);
    cout << "Enter the Course Fee:";
    cin >> fee;
}
// source
// geeksforgeeks - Inheritance in C++
// code
void Student::display_s() {
    display_p();
    cout << "t" << course << "\t" << fee;
}
// source
// geeksforgeeks - Inheritance in C++
// code
int main() {
    Student s;
    s.set_s();
    s.display_s();
    return 0;
}
// source
// geeksforgeeks - Inheritance in C++
// code
void Person::set_p(int id, char n[]) {
    this->id = id;
    strcpy(this->name, n);       
}
// source
// geeksforgeeks - Inheritance in C++
