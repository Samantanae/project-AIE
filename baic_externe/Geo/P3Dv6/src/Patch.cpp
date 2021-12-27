#include "Patch.h"
bool in(const int& a,const std::vector<int>&b){for(int e:b){if(a==e){return true;}}return false;}
int &VIndex(const int& a,const std::vector<int>&b){int id=0;int index=-1;for(int item:b){if(item==a){index = id;id=0;/*réinitialisationDeId*/int &Ind=index;return Ind;}id += 1;}id=0;/*réinitialisationDeId*/int &Ind=index;return Ind;}
void Vremove(const int& a, std::vector<int>&b){b.erase(b.begin()+VIndex(a,b));}


Patch::Patch(const P3D& Ci,const P3D& Cf,const std::vector<P3D>&Data, std::vector<int>&Floor, std::vector<int>&not_Floor)
{
    v1=-1;
    if(in(v1,Floor)){Vremove(v1,Floor);}
    if(!in(v1,not_Floor)){not_Floor.push_back(v1);}
    ci=Ci;
    cf=Cf;
    v1 = 0;
}
void Patch::findPatch()
{
    if(ci==cf)
    {
        /*retun[[ci]]*/
    }
    else
    {

        if(in(v1,floor))
        {

        }
        else
        {

        }
}
Patch::Patch(const P3D& Ci,const P3D& Cf,const std::vector<P3D>&Data, std::vector<int>&not_Floor)
{

}



Patch::~Patch()
{
    //dtor
}
