#include "P3D.h"

P3D::P3D(int X,int Y,int C)
{
    x=X;
    y=Y;
    c=C;
    actif=true;
    //ctor
}
void P3D::nullifier()
{
    actif=false;
}
bool&P3D::null()
{
    return actif;

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


class P2V2:
{
    int x;
    int y;
    int c;
    bool active;
    public:
    P2V2(int X=0,int Y=0,int C=0)
    {
        x=X;
        y=Y;
        c=C;
        active=true;
    }
    int &getItem(const int&item)
    {
        int&i;
        if(item==0)
        {
            i=x;
            return i;
        }
        else if(item==1)
        {
            i=y;
            return i;
        }
        else if(item==2)
        {
            i=c;
            return i;
        }
    }
    void setItem(const int&key,const int&value)
    {
        if(key==0)
        {
            x=value;
        }
        else if(key==1)
        {
            y=value;
        }
        else if(key==2)
        {
            c=value;
        }
    }


};

