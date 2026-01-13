class Author:
    def __init__(self,name,book_name,pages):
        self.n=name;
        self.bn=book_name;
        self.p=pages
        
    def __str__(self):
        return f"{self.bn} is written by {self.n}";

    def __len__(self):
        return self.p;

    def __call__(self,*args,**kwargs):
        print("Hello calling from here")

    def __del__(self):
        print("1st object has been deleted.")


A1=Author("Ram","Math",1000) # init dunder method
print(A1)# #str dunder method
print(len(A1))# len dunder method
A1()# call __call__ dunder method
print(A1)
del A1;# del dunder method


# Extra
print(dir(int))
ans=1
print(id(ans)) # Address showing of ans variable 