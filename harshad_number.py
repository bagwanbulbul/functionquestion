def harshad_number(n):
    a = n/10
    b = n%10
    sub = a+b
    if n%sub == 0:
        print "harshad number hai"
    else:
        print "haeshad number nhi hai"
harshad_number(45)