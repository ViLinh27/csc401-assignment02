#hw2.py, Vi-Linh Nguyen, collaborators: Vi-Anh Nguyen, Bryce Jensen

#3.23, f)
for x in range(1,6):
    y = 4*x+1
    print(y)
#slope intercept form (used to figure out equation)
#source: https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-linear-equations-functions/8th-slope/a/slope-formula

#3.28--requests int n, from user-prints on screen the squares of
#all numbers from 0 up to but not including n
def makeSquares():
    uNum=eval(input('Enter in a number'))
    for i in range(uNum):
        print(i**2)

    
#3.34
def pay(wg,hr):
    if hr>40:
        ot =hr-40
        sl = (wg*hr)+(.5*wg)*ot
        return sl
    else:
        sl= wg * hr
        return sl
#3.38
def abbreviation(d): 
    abD = d[0:2:1]
    return abD  

#3.39---------check if return is better
def collision(x1,y1,r1,x2,y2,r2):
    d = ((x2-x1)+(y2-y1))**0.5
    rsum = r1+r2
    if rsum >d:
        print("They have collided!")
    else:
        print("They have not collided.")

#chilimath.com is where I get distance formula d
    
#3.40
def partition():
    for n in names:
        if n[0]()<'N':
            print(n)
    
#3.41
def lastF():
    FirstName = input('Enter first name: ')
    LastName = input('Enter last name: ')
    print (LastName+', '+ FirstName[0])




2
4
3


