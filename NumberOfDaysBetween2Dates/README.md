# Calculate the number of days between 2 dates!

This program follows a simple procedure by dividing the whole problem into 3 sub problems with the help of conditional **If-Else** statements based on the 3 differences between days, months & years as follows:-

 1. #### When both dates are in same month & year (`daydiff != 0`, `monthdiff = 0` and `yeardiff = 0`)
 2. #### When both dates are in same year but different months (`daydiff != 0`, `monthdiff != 0` and `yeardiff = 0`)
 3. #### When both dates are in different years altogether (`daydiff != 0`, `monthdiff != 0` and `yeardiff != 0`)
 
 We further categorize the 2nd & 3rd parts into the ones for **Leap Years** & **Regular Years** by checking if the year is a leap year or not by simple `leap()` function.

> **Note** : The number of days in every month of a year is saved in two lists (one for **Regular Years** and another for **Leap Years**)
> `daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]` and 
> `daysInMonthLeapYear = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`

>You can see that an **extra element 0** is added in the beginning of list so that we can access number of days in list as per numerical value of the month like `daysInMonth[1]` would give `31` as  result that is the number of days in January
