#ifndef P2_H
#define P2_H
#include <vector>

class P2
{
    public:
        /** Default constructor */
        P2(const P2&);
        P2(int x_,int y_,int c_=0,bool active_=true);
        //P2(int&[1]xy);
        //P2(int&[2] &xyc);
        std::vector<int>& coordonner()const;
        bool& actif() const;
        /** Default destructor */
        virtual ~P2();
        int getx()const{return x;}
        int gety()const{return y;}
        int getc()const{return c;}
        bool getactive()const{return active;};
        int&getCx(){int&cx=x;return cx;}
        int&getCy(){int&cy=y;return cy;}
        int&getCc(){int&cc=c;return cc;}
        bool&getactive(){bool&cactive=active;return cactive;}

    protected:
        int x; //!< Member variable "x"
        int y; //!< Member variable "y"
        int c; //!< Member variable "c"
        bool active; //!< Member variable "active"

    private:
};

#endif // P2_H
