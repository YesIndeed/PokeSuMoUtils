from datetime import datetime, timedelta
import sys, getopt


"""
This is a quick script written to calculate when to check fortune teller tents in Festival Plaza
implemented in Python 2. Times are roughly approximate and defaults are set to my own game.
For ease of implementation, some time intervals close to midnight may be missed.

https://www.reddit.com/r/PokeMoonSun/comments/5f9x25/how_to_get_bottle_caps_guaranteed_for_the_price/dajwh72/
^ Referenced for approxiate times for cycles and prize-changing intervals.
"""

# each bottle cap cycles after 50 minutes
cycle_offset = timedelta(minutes=50)
prize_offset = timedelta(minutes=5)

# time defaults
YEAR = 2017
MONTH = 1
DAY = 17
HOURS = 10
MINS = 15

# prize defaults
LAST_RECEIVED = 2
GOAL = 1

def main(argv):
    if (len(argv) > 0 and argv[0] == "--setdate"):
        date_str = raw_input("Please enter the base date (YY MM DD HH MM)")
        year, month, day, hours, mins = map(int, date_str.strip().split(" "))
    else:
        year, month, day, hours, mins = YEAR, MONTH, DAY, HOURS, MINS
    
    base_date = datetime(year, month, day, hours, mins)
    curr_date = base_date
    print "Your base date is %s" % base_date.isoformat()

    while(1):
        date_str = raw_input("Please enter a timestamp (must be after base date) (YYYY MM DD)\n")
        year, month, day = map(int, date_str.strip().split(" "))
        goal_date = datetime(year, month, day)

        last_received = int(raw_input("What prize level did you receive last? (1-10)\n"))
        goal = int(raw_input("What prize level do you want? (1-10)\n"))

        # Move the current date forward until it matches the goal date.
        while(curr_date.date() != goal_date.date()):
            curr_date += cycle_offset

        # Move the current date forward until it matches the goal prize.
        while(last_received % 10 != goal):
            curr_date += prize_offset
            last_received += 1

        # List of candidate times.
        cand_times = []

        while(curr_date.date() == goal_date.date()):
            cand_times.append(curr_date)
            curr_date = curr_date + cycle_offset

        print "You will get prize %d if you visit the lottery tent at:" % goal
        for time in cand_times:
            print time.isoformat()

if __name__ == "__main__":
    main(sys.argv[1:])
