# PokeSuMoUtils
Quick scripts for Pokemon Sun/Moon gameplay
## Lottery Tent Calculator  
The bottle cap calculator uses information about what ranked prize (#1-10) you got in Festival Plaza's
Lottery Tents to predict what times you can get a prize of your choice if you visit the same Tent
on a given day.

According to [this reddit discussion](https://www.reddit.com/r/PokeMoonSun/comments/5f9x25/how_to_get_bottle_caps_guaranteed_for_the_price/dajwh72/),
the prizes in a Lottery Tent shift predictably in 5 minute intervals. This calculator calculates the correct offset
and keeps adding 50 minutes intervals to obtain times on a given date when a desired prize is available.

Run with Python like so: `python lottery_tent_calc.py --setdate`. The `--setdate` flag is optional, and
allows you to set the base date (the last time you visited the lottery tent). Without the flag, the program
uses default-specified dates (by default, my times are inputted). Keep in mind that the date and time
you use varies by tent.
