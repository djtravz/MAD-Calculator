def fin():
    print "The MAD of the data set is: " + MAD
    done()
def reset():
    q = 0
    qa = 0
    w = 0
    wa = 0
    e = 0
    ea = 0
    r = 0
    ra = 0
    t = 0
    ta = 0
    y = 0
    ya = 0
    u = 0
    ua = 0
    i = 0
    ia = 0
    o = 0
    oa = 0
    p = 0
    pa = 0
    num = 0
    baverage = 0
    average = 0
    aaverage = 0
    MAD = "INTERNAL ERROR 404! INTERNAL SHUTDOWN IMINANT!"
    ans = 0
def nums():
    print "Welcome to djtravz' Mean Absolute Deviation (MAD) calculator! (This does not support decimals!)"
    num = raw_input("How many numbers are in your data set? 2-10 numbers only. No decimals.")
    num = int(num)
    if num == 2:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        two()
    if num == 3:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        e = raw_input("What is the third number in your data set? (Please only enter a number and press enter). ")
        e = int(e)
        three()
    if num == 4:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        e = raw_input("What is the third number in your data set? (Please only enter a number and press enter). ")
        e = int(e)
        r = raw_input("What is the fourth number in your data set? (Please only enter a number and press enter) ")
        r = int(r)
        four()
    if num == 5:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        e = raw_input("What is the third number in your data set? (Please only enter a number and press enter). ")
        e = int(e)
        r = raw_input("What is the fourth number in your data set? (Please only enter a number and press enter) ")
        r = int(r)
        t = raw_input("What is the fifth number in your data set? (Please only enter a number and press enter). ")
        t = int(t)
        five()
    if num == 6:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        e = raw_input("What is the third number in your data set? (Please only enter a number and press enter). ")
        e = int(e)
        r = raw_input("What is the fourth number in your data set? (Please only enter a number and press enter) ")
        r = int(r)
        t = raw_input("What is the fifth number in your data set? (Please only enter a number and press enter). ")
        t = int(t)
        y = raw_input("What is the sixth number in your data set? (Please only enter a number and press enter). ")
        y = int(y)
        six()
    if num == 7:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        e = raw_input("What is the third number in your data set? (Please only enter a number and press enter). ")
        e = int(e)
        r = raw_input("What is the fourth number in your data set? (Please only enter a number and press enter) ")
        r = int(r)
        t = raw_input("What is the fifth number in your data set? (Please only enter a number and press enter). ")
        t = int(t)
        y = raw_input("What is the sixth number in your data set? (Please only enter a number and press enter). ")
        y = int(y)
        u = raw_input("What is the seventh number in your data set? (Please only enter a number and press enter). ")
        u = int(u)
        seven()
    if num == 8:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        e = raw_input("What is the third number in your data set? (Please only enter a number and press enter). ")
        e = int(e)
        r = raw_input("What is the fourth number in your data set? (Please only enter a number and press enter) ")
        r = int(r)
        t = raw_input("What is the fifth number in your data set? (Please only enter a number and press enter). ")
        t = int(t)
        y = raw_input("What is the sixth number in your data set? (Please only enter a number and press enter). ")
        y = int(y)
        u = raw_input("What is the seventh number in your data set? (Please only enter a number and press enter). ")
        u = int(u)
        i = raw_input("What is the eighth number in your data set? (Please only enter a number and press enter). ")
        i = int(i)
        eight()
    if num == 9:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        e = raw_input("What is the third number in your data set? (Please only enter a number and press enter). ")
        e = int(e)
        r = raw_input("What is the fourth number in your data set? (Please only enter a number and press enter) ")
        r = int(r)
        t = raw_input("What is the fifth number in your data set? (Please only enter a number and press enter). ")
        t = int(t)
        y = raw_input("What is the sixth number in your data set? (Please only enter a number and press enter). ")
        y = int(y)
        u = raw_input("What is the seventh number in your data set? (Please only enter a number and press enter). ")
        u = int(u)
        i = raw_input("What is the eighth number in your data set? (Please only enter a number and press enter). ")
        i = int(i)
        o = raw_input("What is the ninth number in your data set? (Please only enter a number and press enter). ")
        o = int(o)
        nine()
    if num == 10:
        q = raw_input("What is the first number in your data set? (Please only enter a number and press enter) ")
        q = int(q)
        w = raw_input("What is the second number in your data set? (Please only enter a number and press enter) ")
        w = int(w)
        e = raw_input("What is the third number in your data set? (Please only enter a number and press enter). ")
        e = int(e)
        r = raw_input("What is the fourth number in your data set? (Please only enter a number and press enter) ")
        r = int(r)
        t = raw_input("What is the fifth number in your data set? (Please only enter a number and press enter). ")
        t = int(t)
        y = raw_input("What is the sixth number in your data set? (Please only enter a number and press enter). ")
        y = int(y)
        u = raw_input("What is the seventh number in your data set? (Please only enter a number and press enter). ")
        u = int(u)
        i = raw_input("What is the eighth number in your data set? (Please only enter a number and press enter). ")
        i = int(i)
        o = raw_input("What is the ninth number in your data set? (Please only enter a number and press enter). ")
        o = int(o)
        p = raw_input("What is the tenth number in your data set? (Please only enter a number and press enter). ")
        p = int(p)
        ten()
def two():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    aaverage = qa * wa
    MAD = aaverage / num
    fin()
def three():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w * e
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    ea = abs(average - e)
    aaverage = qa * wa
    MAD = aaverage / num
    fin()
def four():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w * e * r
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    ea = abs(average - e)
    ra = abs(average - r)
    aaverage = qa * wa * ea * ra
    MAD = aaverage / num
    fin()
def five():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w * e * r * t
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    ea = abs(average - e)
    ra = abs(average - r)
    ta = abs(average - t)
    aaverage = qa * wa * ea * ra * ta
    MAD = aaverage / num
    fin()
def six():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w * e * r * t * y
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    ea = abs(average - e)
    ra = abs(average - r)
    ta = abs(average - t)
    ya = abs(average - y)
    aaverage = qa * wa * ea * ra * ta * ya
    MAD = aaverage / num
    fin()
def seven():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w * e * r * t * y * u
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    ea = abs(average - e)
    ra = abs(average - r)
    ta = abs(average - t)
    ya = abs(average - y)
    ua = abs(average - u)
    aaverage = qa * wa * ea * ra * ta * ya * ua
    MAD = aaverage / num
    fin()
def eight():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w * e * r * t * y * u * i
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    ea = abs(average - e)
    ra = abs(average - r)
    ta = abs(average - t)
    ya = abs(average - y)
    ua = abs(average - u)
    ia = abs(average - i)
    aaverage = qa * wa * ea * ra * ta * ya * ua * ia
    MAD = aaverage / num
    fin()
def nine():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w * e * r * t * y * u * i * o
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    ea = abs(average - e)
    ra = abs(average - r)
    ta = abs(average - t)
    ya = abs(average - y)
    ua = abs(average - u)
    ia = abs(average - i)
    oa = abs(average - o)
    aaverage = qa * wa * ea * ra * ta * ya * ua * ia * oa
    MAD = aaverage / num
    fin()
def ten():
    print "Thanks! Now I will start calculating. I will give you the average and the MAD when I get them."
    baverage = q * w * e * r * t * y * u * i * o * p
    average = baverage / num
    print "The average of your numbers is: " + average
    qa = abs(average - q)
    wa = abs(average - w)
    ea = abs(average - e)
    ra = abs(average - r)
    ta = abs(average - t)
    ya = abs(average - y)
    ua = abs(average - u)
    ia = abs(average - i)
    oa = abs(average - o)
    pa = abs(average - p)
    aaverage = qa * wa * ea * ra * ta * ya * ua * ia * oa * pa
    MAD = aaverage / num
    fin()
def s():
   reset()
   nums()
def done():
   ans = raw_input("Would you like to do another data set? (y or n)")
   if ans == "y":
      print "Ok! Here we gooooo!!!"
      s()
   elif ans == "n":
      print "OK. Thank you for using my MAD (Mean Absolute Deviation) calculator! :)"
   else:
      print "You didn't tell me an answer I support!"
      done()
s()