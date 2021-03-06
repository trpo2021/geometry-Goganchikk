#include "infoOutput.h"
#include <cmath>
#include <iostream>

using std::cout;
using std::endl;

const double PI = 3.141592653589793238463;

void triangleInfo(
        double x1, double y1, double x2, double y2, double x3, double y3)
{
    cout << "x1 = " << x1 << endl;
    cout << "y1 = " << y1 << endl;
    cout << "x2 = " << x2 << endl;
    cout << "y2 = " << y2 << endl;
    cout << "x3 = " << x3 << endl;
    cout << "y3 = " << y3 << endl;

    double a = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
    double b = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
    double c = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2));
    double p = (a + b + c) / 2.0;

    cout << "P = " << a + b + c << endl;
    cout << "S = " << sqrt(p * (p - a) * (p - b) * (p - c)) << endl;
}
void circleInfo(double x, double y, double radius)
{
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;

    cout << "radius = " << radius << endl;
    cout << "P = " << 2 * PI * radius << endl;
    cout << "S = " << PI * radius * radius << endl;
}
