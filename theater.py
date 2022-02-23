# https://github.com/dabeaz/theater
#
# The owner of a monopolistic movie theater in a small town has
# complete freedom in setting ticket prices.  The more he charges, the
# fewer people can afford tickets.  The less he charges, the more it
# costs to run a show because attendance goes up.  In a recent
# experiment the owner determined a relationship between the price of
# a ticket and average attendance.
#
# At a price of $5.00/ticket, 120 people attend a performance.  For
# each 10-cent change in the ticket price, the average attendance
# changes by 15 people.  That is, if the owner charges $5.10, some 105
# people attend on the average; if the price goes down to $4.90,
# average attendance increases to 135.
#
# Unfortunately, the increased attendance also comes at an increased
# cost.  Every performance comes at a fixed cost of $180 to the owner
# plus a variable cost of $0.04 per attendee.
#
# The owner would like to know the exact relationship between profit
# and ticket price in order to maximize the profit.
#
# Write a program to figure out the best ticket price (to the nearest
# 10 cents) that maximizes profit.
#
# Credit: This problem comes from "How to Design Programs", 2nd Ed.
# by Felleisen, Findler, Flatt, and Krishnamurthi.  pg. 60.

# Hunter Wilkins' Solution to the problem
# I used calculus to maximize the formula
#
# Using the values givin in the problem
# profit(price) = price * (870 - 150 * price) - (180 + 0.04 * (870 - 150 * price))
# profit'(price) = -300 * price + 876
#
# Setting profit'(price) == 0
# -876 = -300 * price
# -876 / -300 = price
# 876 / 300 = price
# price = $2.92

def compute_best_ticket_price(
        base_ticket_price=5.0,
        base_attendence=120,
        attendence_per_dollar=150,
        attendee_cost=0.04):
    return (base_ticket_price * attendence_per_dollar + base_attendence + attendence_per_dollar * attendee_cost) / (2 * attendence_per_dollar)

print(compute_best_ticket_price())