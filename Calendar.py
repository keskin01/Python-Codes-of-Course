year = 2019
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
first_day = 1
final_day = 31


def plan_of_month(month):
    for i in range(first_day, (final_day + 1)):

        if month == "January":
            x = 0

        elif month == "February":
            x = 3
            if year % 4 == 0:
                if i == 30:  # if Feb is 29
                    break
            else:
                if i == 29:  # if Feb is 28
                    break

        elif month == "March":
            x = 3

        elif month == "April":
            x = -1
            if i == 31:
                break

        elif month == "May":
            x = 1

        elif month == "June":
            x = 4
            if i == 31:
                break
        elif month == "July":
            x = -1

        elif month == "August":
            x = 2

        elif month == "September":
            x = 5
            if i == 31:
                break
        elif month == "October":
            x = 0

        elif month == "November":
            x = 3
            if i == 31:
                break
        elif month == "December":
            x = 5

        else:
            print("Please enter month correctly")
        print(i, month, year, days[(i + x) % 7])
    print("----------------------")


plan_of_month("January")
plan_of_month("February")
plan_of_month("March")
plan_of_month("April")
plan_of_month("May")
plan_of_month("June")
plan_of_month("July")
plan_of_month("August")
plan_of_month("September")
plan_of_month("October")
plan_of_month("November")
plan_of_month("December")
