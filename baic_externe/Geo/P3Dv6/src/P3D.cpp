#include "P3D.h"

P3D::P3D(int X,int Y,int C)
{
    x=X;
    y=Y;
    c=C;
    //ctor
}
bool operator==(P3D &a, const P3D &b)
{
    if(a.x==b.x)
    {
        if(a.y==b.y)
        {
            return true;
        }
    }
    return false;

}

P3D::~P3D()
{
    //dtor
}
