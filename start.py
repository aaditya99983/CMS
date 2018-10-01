def start():
    name=input("Enter Name of the Blog: ")
    file=open("index.html","w+")
    file.write("<HTML>\n")
    file.write("<Title>"+name+"</Title>")
    file.write("<Body>")
    file.write("<H1>Welcome To "+name+"</H1>")
    file.close()
    print("Blog Initialized Successfully")

if __name__=="__main__":
    start()