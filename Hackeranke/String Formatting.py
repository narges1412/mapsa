def print_formatted(number):
    # your code goes here
    spac=len(bin(number))
    for i in range(1,n+1):
        dec=str(i).rjust(spac)
        octnum=oct(i).rjust(spac)
        hexnum=hex(i).upper().rjust(spac)
        binnum=bin(i).rjust(spac)
        print(dec+' ',octnum[2:]+' ',hexnum[2:]+' ',binnum[2:]+' ')
        

    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)