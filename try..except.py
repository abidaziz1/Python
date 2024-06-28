try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong with the file")
    finally:
        f.close()

except:
    print("Something went wrong with the file while opening")   # TODO  check   this            