def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though! 
    daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysInMonthLeapYear = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yeardiff, monthdiff, daydiff = (year1 - year2), (month1 - month2), (day1 - day2)
    if yeardiff == 0:
        if monthdiff == 0:
            if daydiff == 0:
                return 0
            else:
                return (day2 - day1)
        else:
            if leap(year1) == True:
                m1RestDays = daysInMonthLeapYear[month1]-day1
                otherMonthsDays = 0
                for i in range(month1+1, month2):
                    otherMonthsDays += daysInMonthLeapYear[i]
                total = m1RestDays + otherMonthsDays + day2
                return total
            else:
                m1RestDays = daysInMonth[month1]-day1
                otherMonthsDays = 0
                for i in range(month1+1, month2):
                    otherMonthsDays += daysInMonth[i]
                total = m1RestDays + otherMonthsDays + day2
                return total
    else:
        y1RestDays=0
        if leap(year1) == True:
            otherMonthsDays = 0
            m1RestDays = daysInMonthLeapYear[month1]-day1
            for i in range(month1+1, 13):
                otherMonthsDays += daysInMonthLeapYear[i]
            total = m1RestDays + otherMonthsDays
            y1RestDays = total
        else:
            otherMonthsDays = 0
            m1RestDays = daysInMonth[month1]-day1
            for i in range(month1+1, 13):
                otherMonthsDays += daysInMonth[i]
            total2 = m1RestDays + otherMonthsDays
            y1RestDays = total2
        
        y2RestDays=0
        if leap(year2) == True:
            otherMonthsDays = 0
            m1RestDays = day2
            for i in range(1, month2):
                otherMonthsDays += daysInMonthLeapYear[i]
            total3 = m1RestDays + otherMonthsDays
            y2RestDays = total3
        else:
            otherMonthsDays = 0
            m1RestDays = day2
            for i in range(1, month2):
                otherMonthsDays += daysInMonth[i]
            total4 = m1RestDays + otherMonthsDays
            y2RestDays = total4
        
        restDays=0
        for i in range(year1+1, year2):
            if i%4 == 0:
                restDays += 366
            else:
                restDays += 365
        tot = y1RestDays + y2RestDays + restDays
        return tot
        
    
    return 0

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()
