
#include <iostream>
#include <typeinfo>
#include <string>

using namespace std;


template <class T>

/* list of mode:




*/

class arg{
    public:
        /** Default constructor */
        arg(arg&a)
        {

        }

        arg(T _value_,bool av_=false,bool active_=true,int mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T&_value_,bool&av_      ,bool&active_=true,int&mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T _value_,bool&av_      ,bool&active_=true,int&mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T&_value_,bool av_=false,bool&active_=true,int&mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T&_value_,bool&av_      ,bool active_=true,int&mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T&_value_,bool&av_      ,bool&active_=true,int mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T _value_,bool av_=false,bool&active_=true,int&mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T _value_,bool&av_      ,bool active_=true,int&mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T _value_,bool&av_=false,bool&active_=true,int mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T&_value_,bool av_=false,bool active_=true,int&mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T&_value_,bool av_=false,bool&active_=true,int mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
        arg(T&_value_,bool&av_      ,bool active_=true,int mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
//        arg(T _value_,bool&av_      ,bool&active_     ,int&mode_    ){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
//        arg(T&_value_,bool av_=false,bool&active_     ,int&mode_    ){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
//        arg(T&_value_,bool&av_      ,bool active_=true,int&mode_    ){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}
//        arg(T&_value_,bool&av_      ,bool&active_     ,int mode_ = 0){value=_value_;try{_type_= typeid(_value_).name();}catch (...){if(_value_.hasOwnProperty('name')==true){_type_=_value_.name();}else{throw 1000;}}}

        arg(T&_value_);
        std::string& getType()const;
        friend operator+(arg&a,const arg&b){}
        friend operator+(arg&a,const auto&b);
        /** Default destructor */
        virtual ~arg();

    protected:
        T& value;
        std::string&_type_;
    private:
};

