import sys
import getopt

def main():
    f1 = None
    f2 = None
    argv = sys.argv[1:]
    
    try:   
        opts, args = getopt.getopt (argv, "", [ "first_file=" , "second_file="])   
    except:   
        print("Error in Arg denotation, use --first_file and --second_file")

    print(opts)

    for opt , arg in opts:   
        if opt in ['--first_file'] :   
            f1 = arg   
        elif opt in ['--second_file'] :   
            f2 = arg
   
    print(compareFiles(f1, f2))


def compareFiles(f1, f2):
    File1 = open(f1, mode="rb")
    File2 = open(f2, mode="rb")
    
    KiB1 = File1.read(1024)
    KiB2 = File2.read(1024)
    
    while(KiB1 or KiB2):
        if(KiB1 == KiB2):
            KiB1 = File1.read(1024)
            KiB2 = File2.read(1024)
        else:
            print("Diferença encontrada nos ficheiros")
            exit()
    
    return("Nenhuma diferença encontrada.")


if __name__ == "__main__":
    main()