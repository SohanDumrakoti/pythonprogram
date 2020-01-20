def div(a,b):
    return (a/b)
success=False
while success==False:
    try:
        a = float(input('Enter a value for a:: '))
        b = float(input('Enter a value for b:: '))
        print(div(a,b))
        success=True
    except:
        print('Value can not be string or b can not be 0. Please enter again')