x1 = " "
x2 = " "
x3 = " "
x4 = " "
x5 = " "
x6 = " "
x7 = " "
x8 = " "
x9 = " "
cof = 0
point = ''
X_score = 0
o_score = 0

def output():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9
    print("---------------")
    print("  / A / B / C /")
    print("---------------")
    print("1 / "+x1+" / "+x2+" / "+x3+" /")
    print("2 / "+x4+" / "+x5+" / "+x6+" /")
    print("3 / "+x7+" / "+x8+" / "+x9+" /")
    print("---------------")

def ask():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9
    ask_cof = 0
    while ask_cof == 0:
        location = input("enter location: ")
        if str(location) == "A1" and x1 == " ":
            x1 = str(point)
            ask_cof = 1
        elif str(location) == "B1" and x2 == " ":
            x2 = str(point)
            ask_cof = 1
        elif str(location) == "C1" and x3 == " ":
            x3 = str(point)
            ask_cof = 1
        elif str(location) == "A2" and x4 == " ":
            x4 = str(point)
            ask_cof = 1
        elif str(location) == "B2" and x5 == " ":
            x5 = str(point)
            ask_cof = 1
        elif str(location) == "C2" and x6 == " ":
            x6 = str(point)
            ask_cof = 1
        elif str(location) == "A3" and x7 == " ":
            x7 = str(point)
            ask_cof = 1
        elif str(location) == "B3" and x8 == " ":
            x8 = str(point)
            ask_cof = 1
        elif str(location) == "C3" and x9 == " ":
            x9 = str(point)
            ask_cof = 1
        else:
            print("please enter location (for example A2, B3, C1, etc.) OR restart game")

def computer():
    global point, x1, x2, x3, x4, x5, x6, x7, x8, x9
    point_lst = ["X","0"]
    point_lst.remove(str(point))
    comp_point = point_lst[0]
        
    if str(comp_point) == "0" and str(x5)==str(x9)==str(point) and str(x1)== str(comp_point) and str(x7) == " ":
        point_lst.remove(str(comp_point))
        x7 = str(comp_point)

    elif str(comp_point) == "X" and str(x1) == " " and str(x2) == " "  and str(x3) == " "  and str(x4) == " "  and str(x5) == " " and str(x6) == " " and str(x7) == " " and str(x8) == " " and str(x9) == " ":
        point_lst.remove(str(comp_point))
        x5 = str(comp_point)        

    elif str(comp_point) == "0" and str(x3)==str(point) and str(x8)==str(point) and str(x2) == " " and str(x4) == " "  and str(x5) == " " and str(x6) == " " and str(x7) == " " and str(x9) == " ":
        point_lst.remove(str(comp_point))
        x7 = str(comp_point)
        
    elif str(comp_point) == "0" and str(x1)==str(point) and str(x2) == " "  and str(x3) == " "  and str(x4) == " "  and str(x5) == " " and str(x6) == " " and str(x7) == " " and str(x8) == " " and str(x9) == " ":
        point_lst.remove(str(comp_point))
        x9 = str(comp_point)

    elif str(comp_point) == "0" and str(x3)==str(point) and str(x2) == " "  and str(x1) == " "  and str(x4) == " "  and str(x5) == " " and str(x6) == " " and str(x7) == " " and str(x8) == " " and str(x9) == " ":
        point_lst.remove(str(comp_point))
        x7 = str(comp_point)

    elif str(comp_point) == "0" and str(x7)==str(point) and str(x2) == " "  and str(x1) == " "  and str(x4) == " "  and str(x5) == " " and str(x6) == " " and str(x3) == " " and str(x8) == " " and str(x9) == " ":
        point_lst.remove(str(comp_point))
        x3 = str(comp_point)
        
    elif str(comp_point) == "0" and str(x9)==str(point) and str(x2) == " "  and str(x3) == " "  and str(x4) == " "  and str(x5) == " " and str(x6) == " " and str(x7) == " " and str(x8) == " " and str(x1) == " ":
        point_lst.remove(str(comp_point))
        x1 = str(comp_point)

    elif str(comp_point) == "0" and str(x7)==str(x2)==str(point) and str(x3)==str(comp_point) and str(x1)==" " and str(x4) == " " and str(x5)==" " and str(x6)==" " and str(x8)==" " and str(x9)==" ":
        point_lst.remove(str(comp_point))
        x9 = str(comp_point)

    elif str(comp_point) =="0" and str(x7)==str(x2)==str(x6)==str(point) and str(x3)==str(x9)==str(comp_point) and str(x1)==str(x4)==str(x5)==str(x8)==" ":
        point_lst.remove(str(comp_point))
        x5 = str(comp_point)
    else:

        if str(x1)==str(x2)==str(comp_point) and x3 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x3 = str(comp_point)

        elif str(x4)==str(x5)==str(comp_point) and x6 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x6 = str(comp_point)

        elif str(x7)==str(x8)==str(comp_point) and x9 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x9 = str(comp_point)

        elif str(x1)==str(x3)==str(comp_point) and x2 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x2 = str(comp_point)

        elif str(x4)==str(x6)==str(comp_point) and x5 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x5 = str(comp_point)

        elif str(x7)==str(x9)==str(comp_point) and x8 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x8 = str(comp_point)

        elif str(x2)==str(x3)==str(comp_point) and x1 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x1 = str(comp_point)

        elif str(x5)==str(x6)==str(comp_point) and x4 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x4 = str(comp_point)

        elif str(x8)==str(x9)==str(comp_point) and x7 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x7 = str(comp_point)

        elif str(x1)==str(x4)==str(comp_point) and x7 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x7 = str(comp_point)

        elif str(x2)==str(x5)==str(comp_point) and x8 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x8 = str(comp_point)

        elif str(x3)==str(x6)==str(comp_point) and x9 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x9 = str(comp_point)

        elif str(x1)==str(x7)==str(comp_point) and x4 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x4 = str(comp_point)

        elif str(x2)==str(x8)==str(comp_point) and x5 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x5 = str(comp_point)

        elif str(x3)==str(x9)==str(comp_point) and x6 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x6 = str(comp_point)

        elif str(x4)==str(x7)==str(comp_point) and x1 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x1 = str(comp_point)

        elif str(x5)==str(x8)==str(comp_point) and x2 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x2 = str(comp_point)

        elif str(x6)==str(x9)==str(comp_point) and x3 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x3 = str(comp_point)

        elif str(x1)==str(x5)==str(comp_point) and x9 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x9 = str(comp_point)

        elif str(x1)==str(x9)==str(comp_point) and x5 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x5 = str(comp_point)

        elif str(x5)==str(x9)==str(comp_point) and x1 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x1 = str(comp_point)

        elif str(x3)==str(x5)==str(comp_point) and x7 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x7 = str(comp_point)

        elif str(x3)==str(x7)==str(comp_point) and x5 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x5 = str(comp_point)

        elif str(x5)==str(x7)==str(comp_point) and x3 == " ":
            comp_point = point_lst[0]
            point_lst.remove(str(comp_point))
            x3 = str(comp_point)

        else:

            if str(x1)==str(x2)==str(point) and x3 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x3 = str(comp_point)

            elif str(x4)==str(x5)==str(point) and x6 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x6 = str(comp_point)

            elif str(x7)==str(x8)==str(point) and x9 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x9 = str(comp_point)

            elif str(x1)==str(x3)==str(point) and x2 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x2 = str(comp_point)

            elif str(x4)==str(x6)==str(point) and x5 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x5 = str(comp_point)

            elif str(x7)==str(x9)==str(point) and x8 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x8 = str(comp_point)

            elif str(x2)==str(x3)==str(point) and x1 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x1 = str(comp_point)

            elif str(x5)==str(x6)==str(point) and x4 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x4 = str(comp_point)

            elif str(x8)==str(x9)==str(point) and x7 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x7 = str(comp_point)

            elif str(x1)==str(x4)==str(point) and x7 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x7 = str(comp_point)

            elif str(x2)==str(x5)==str(point) and x8 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x8 = str(comp_point)

            elif str(x3)==str(x6)==str(point) and x9 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x9 = str(comp_point)

            elif str(x1)==str(x7)==str(point) and x4 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x4 = str(comp_point)

            elif str(x2)==str(x8)==str(point) and x5 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x5 = str(comp_point)

            elif str(x3)==str(x9)==str(point) and x6 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x6 = str(comp_point)

            elif str(x4)==str(x7)==str(point) and x1 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x1 = str(comp_point)

            elif str(x5)==str(x8)==str(point) and x2 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x2 = str(comp_point)

            elif str(x6)==str(x9)==str(point) and x3 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x3 = str(comp_point)

            elif str(x1)==str(x5)==str(point) and x9 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x9 = str(comp_point)

            elif str(x1)==str(x9)==str(point) and x5 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x5 = str(comp_point)

            elif str(x5)==str(x9)==str(point) and x1 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x1 = str(comp_point)

            elif str(x3)==str(x5)==str(point) and x7 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x7 = str(comp_point)

            elif str(x3)==str(x7)==str(point) and x5 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x5 = str(comp_point)

            elif str(x5)==str(x7)==str(point) and x3 == " ":
                comp_point = point_lst[0]
                point_lst.remove(str(comp_point))
                x3 = str(comp_point)

            else:
                if x1 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x1 = str(comp_point)
                elif x2 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x2 = str(comp_point)
                elif x3 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x3 = str(comp_point)
                elif x4 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x4 = str(comp_point)
                elif x5 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x5 = str(comp_point)
                elif x6 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x6 = str(comp_point)
                elif x7 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x7 = str(comp_point)
                elif x8 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x8 = str(comp_point)
                elif x9 == " ":
                    comp_point = point_lst[0]
                    point_lst.remove(str(comp_point))
                    x9 = str(comp_point)
                
        
        

def check():
    global cof, X_score, o_score
    if str(x1)==str(x2)==str(x3)=="X":
        print("X WINS!")
        X_score = int(X_score) + 1
        cof = 1
    elif str(x4)==str(x5)==str(x6)=="X":
        print("X WINS!")
        X_score = int(X_score) + 1
        cof = 1
    elif str(x7)==str(x8)==str(x9)=="X":
        print("X WINS!")
        X_score = int(X_score) + 1
        cof = 1
    elif str(x1)==str(x4)==str(x7)=="X":
        print("X WINS!")
        X_score = int(X_score) + 1
        cof = 1
    elif str(x2)==str(x5)==str(x8)=="X":
        print("X WINS!")
        X_score = int(X_score) + 1
        cof = 1
    elif str(x3)==str(x6)==str(x9)=="X":
        print("X WINS!")
        X_score = int(X_score) + 1
        cof = 1
    elif str(x1)==str(x5)==str(x9)=="X":
        print("X WINS!")
        X_score = int(X_score) + 1
        cof = 1
    elif str(x7)==str(x5)==str(x3)=="X":
        print("X WINS!")
        X_score = int(X_score) + 1
        cof = 1
    elif str(x1)==str(x2)==str(x3)=="0":
        print("0 WINS!")
        o_score = int(o_score) + 1
        cof = 1
    elif str(x4)==str(x5)==str(x6)=="0":
        print("0 WINS!")
        o_score = int(o_score) + 1
        cof = 1
    elif str(x7)==str(x8)==str(x9)=="0":
        print("0 WINS!")
        o_score = int(o_score) + 1
        cof = 1
    elif str(x1)==str(x4)==str(x7)=="0":
        print("0 WINS!")
        o_score = int(o_score) + 1
        cof = 1
    elif str(x2)==str(x5)==str(x8)=="0":
        print("0 WINS!")
        o_score = int(o_score) + 1
        cof = 1
    elif str(x3)==str(x6)==str(x9)=="0":
        print("0 WINS!")
        o_score = int(o_score) + 1
        cof = 1
    elif str(x1)==str(x5)==str(x9)=="0":
        print("0 WINS!")
        o_score = int(o_score) + 1
        cof = 1
    elif str(x7)==str(x5)==str(x3)=="0":
        print("0 WINS!")
        o_score = int(o_score) + 1
        cof = 1
    else:
        if x1 != " " and x2 != " " and x3 != " " and x4 != " " and x5 != " " and x6 != " " and x7 != " " and x8 != " " and x9 != " ":  
            print("Draw!")
            cof = 1
        
while str(point) != "X" and str(point) != "0":
    point = input("choose (X/0): ")
output()    
while True:
    if str(point) == "X":
        ask()
        computer()
        output()
        check()
        if int(cof) == 1:
            x1 = " "
            x2 = " "
            x3 = " "
            x4 = " "
            x5 = " "
            x6 = " "
            x7 = " "
            x8 = " "
            x9 = " "
            cof = 0
            print("X - "+str(X_score))
            print("0 - "+str(o_score))
            
    elif str(point) == "0":
        computer()
        check()
        if int(cof) == 1:
            x1 = " "
            x2 = " "
            x3 = " "
            x4 = " "
            x5 = " "
            x6 = " "
            x7 = " "
            x8 = " "
            x9 = " "
            print("X - "+str(X_score))
            print("0 - "+str(o_score))
        output()
        if cof == 0:  
            ask()
        cof = 0





    
