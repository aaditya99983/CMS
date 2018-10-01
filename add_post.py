def add_post():
    post=input("Enter Post: ")
    counter=open("count.cms","r")
    count=int(counter.read())
    file=open(str(count)+".html","w+")
    counter.close()
    counter=open("count.cms","w+")
    counter.write(str(count+1))
    counter.close()
    file.write("<HTML>\n")
    file.write("<Title>"+post+"</Title>")
    file.write("<Body>")
    file.write("<p>"+post+"</p>")
    file.close()
    print("Post Added Successfully")

if __name__=="__main__":
    add_post()