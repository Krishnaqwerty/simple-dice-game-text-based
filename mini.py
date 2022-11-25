import random
import os
b="Y"
i=0
def one_1():
    print("***************************")
    print("*                         *")
    print("*           11            *")
    print("*          111            *")
    print("*         1111            *")
    print("*           11            *")
    print("*           11            *")
    print("*           11            *")
    print("*        111111           *")
    print("*                         *")
    print("***************************")

def two_2():
    print("***************************")
    print("*                         *")
    print("*          222            *")
    print("*        22   22          *")
    print("*        22   22          *")
    print("*            22           *")
    print("*           22            *")
    print("*          22             *")
    print("*         22              *")
    print("*        22222222         *")
    print("*                         *")
    print("***************************")

def three_3():
    print("***************************")
    print("*                         *")
    print("*        3333333          *")
    print("*            33           *")
    print("*           33            *")
    print("*        333              *")
    print("*            33           *")
    print("*              3          *")
    print("*            33           *")
    print("*        333              *")
    print("*                         *")
    print("***************************")

def four_4():
    print("***************************")
    print("*                         *")
    print("*        44  44           *")
    print("*        44  44           *")
    print("*        444444           *")
    print("*            44           *")
    print("*            44           *")
    print("*                         *")
    print("***************************")
    

def five_5():
    print("***************************")
    print("*                         *")
    print("*          555555         *")
    print("*         55              *")
    print("*        5555555          *")
    print("*              55         *")
    print("*              55         *")
    print("*        55555            *")
    print("*                         *")
    print("***************************")

def six_6():
    print("***************************")
    print("*                         *")
    print("*             66          *")
    print("*            66           *")
    print("*          66             *")
    print("*         66666           *")
    print("*        66    66         *")
    print("*         66666           *")
    print("*                         *")
    print("***************************")

def you_won():
    print("  *     *    *    * * * *     *       *             *     *     *   * * * *   *    *        *")
    print("* * *    * *      *     *     *       *              *   * *   *    *     *   * *  *      * * *")
    print(" * *      *       *     *     *       *               * *   * *     *     *   *  * *       * *")
    print("  *       *       * * * *     * * * * *                *     *      * * * *   *    *        *")

def you_loss():
    print("*    *     * * * *     *       *           *           * * * *    * * * *    * * * *")
    print(" * *       *     *     *       *           *           *     *    *          *      ")
    print("  *        *     *     *       *           *           *     *    * * * *    * * * *") 
    print("  *        *     *     *       *           *           *     *          *          *") 
    print("  *        * * * *     * * * * *           * * * *     * * * *    * * * *    * * * *")




while b=="Y" or b=="y":
    def mini(n):
        global i
        a=random.randint(1,6)
        print("\n")
        print("DICE OUTCOME:")
        if a==1:
            one_1()
        elif a==2:
            two_2()
        elif a==3:
            three_3()
        elif a==4:
            four_4()
        elif a==5:
            five_5()
        else:
            six_6()
        
        print("\n")


        print("**"*50)
        print("**"*50)
        if a==n:
            i+=1
            print("\n")
            you_won()
            print("\n")
        else:
            print("\n")
            you_loss()
            print("\n")
    os.system('cls')
    n=int(input("ENTER A DICE FACE NUMBER: "))
    print("\n")
    print("**"*50)
    print("**"*50)
    os.system('cls')

    if 1<=n<=6:
        print("YOUR CHOICE: ","\n")
        if n==1:
            one_1()
        elif n==2:
            two_2()
        elif n==3:
            three_3()
        elif n==4:
            four_4()
        elif n==5:
            five_5()
        else:
            six_6()
        print("\n")
        print("<>"*50)
        print("<>"*50)
        print("<>"*50)
        print("\n")

        mini(n)
    else:
        print("!!"*50)
        print("!!"*50)
        print("!!"*50)
        
        while n not in range(1,7):
            os.system('cls')
            n=int(input("ENTER A VALID FACE NUMBER !! :"))
        os.system('cls')
        print("YOUR CHOICE: ","\n")
        if n==1:
            one_1()
        elif n==2:
            two_2()
        elif n==3:
            three_3()
        elif n==4:
            four_4()
        elif n==5:
            five_5()
        else:
            six_6()
        print("\n")
        print("<>"*50)
        print("<>"*50)
        print("<>"*50)
        print("\n")

        mini(n)
    print("**"*50)
    print("**"*50)
    print("YOUR SCORE:",i)
    print("\n")
    print("**"*50)
    print("**"*50)
    print("\n")
    b=input("ENTER Y/y TO PLAY AGAIN: ")
    print("**"*50)
    print("**"*50)
    print("**"*50)
else:
    print("!! END !!"*11)

    
