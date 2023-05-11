def menu():
  print ("Do you have the angles (A), the sum of interior angles (SIA), size of interior angles (IA) or size of external angles (EA)")
  while True:
    selection = input().upper()
    if selection == "A":
      angles()
    elif selection == "SIA":
      siangles()
    elif selection == "IA":
      iangles()
    elif selection == "EA":
      eangles()
def angles():
  print ("Input number of angles")
  angles = int(input())
  interiorangles = int((angles - 2) * 180)
  sizeinterior = round(interiorangles/angles,2)
  sizeexterior = round(360/angles,2)
  print ("Sum of interior angles",interiorangles)
  print ("Size of interior angle",sizeinterior)
  print ("Size of exterior angle",sizeexterior)
  while True:
    print ("Would you like to restart (Y/N)")
    restart = input().upper()
    if restart == "Y":
      menu()
    elif restart == "N":
      exit()
    else:
      print ("Incorrect input")
def siangles():
  print ("Enter the interior angle")
  interiorangles = int(input())
  angles = int(interiorangles / 180 + 2)
  sizeinterior = round(interiorangles/angles,2)
  sizeexterior = round(360/angles,2)
  print ("Amount of angles in polygon",angles)
  print ("Size of interior angle",sizeinterior)
  print ("Size of exterior angle",sizeexterior)
  while True:
    print ("Would you like to restart (Y/N)")
    restart = input().upper()
    if restart == "Y":
      menu()
    elif restart == "N":
      exit()
    else:
      print ("Incorrect input")
def iangles():
  print("Input the size of interior angle")
  sizeinterior = int(input())
  sizeexterior = round(180-sizeinterior,2)
  angles = int(360/sizeexterior)  
  interiorangles = round((angles - 2) * 180,2)
  print ("Amount of angles in polygon",angles)
  print ("Sum of interior angle",interiorangles)
  print ("Size of exterior angle",sizeexterior)
  while True:
    print ("Would you like to restart (Y/N)")
    restart = input().upper()
    if restart == "Y":
      menu()
    elif restart == "N":
      exit()
    else:
      print ("Incorrect input")
def eangles():
  print ("Input the size of exterior angle")
  sizeexterior = int(input())
  angles = int(360/sizeexterior)
  interiorangles = int((angles - 2) * 180)
  sizeinterior = round(interiorangles/angles,2)
  print ("Amount of angles in polygon",angles)
  print ("Sum of interior angle",interiorangles)
  print ("Size of interior angle",sizeinterior)
  while True:
    print ("Would you like to restart (Y/N)")
    restart = input().upper()
    if restart == "Y":
      menu()
    elif restart == "N":
      exit()
    else:
      print ("Incorrect input")
menu()
