def view_post():
    file=open("data.csv","r+")
    for i in file.readlines():
        print(i)



if __name__=="__main__":
    view_post()