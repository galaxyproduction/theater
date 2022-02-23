# theater

Code for "The Problem with the Problem" talk, given by
David Beazley (@dabeaz) at PyCon Sri Lanka, February 22, 2022.

# The Problem with the Problem Problem

David Beazley showed this problem in his talk, ["The Problem with the Problem"](https://www.youtube.com/watch?v=t-IUY6QrJyU), and he demonstrate how professional developers can over engineer solutions to seemingly simple problems. This can lead the developers down rabit holes of abstractions that can lose sight of what the original problem they were trying to solve was.

# My Solution to the problem
``` python
def compute_best_ticket_price(
        base_ticket_price=5.0,
        base_attendence=120,
        attendence_per_dollar=150,
        attendee_cost=0.04):
    return (base_ticket_price * attendence_per_dollar + base_attendence + attendence_per_dollar  * attendee_cost) / (2 * attendence_per_dollar)
```

## What is good about this solution

David Beazley showed several attempts at solving the problem through his talk, and he ended up simplifing the problem by using a while loop and forgoing the previous abstractions that developers might think of using. 


In my solution, I derived a formula to calcuate the optimal cost by using calculus. I think this solution adheres more closly to the 'true' solution to the problem as my solution doesn't abstract the logic away from the problem by using arrays, classes, or other libraries.


My solution also solves the problem of 'magic' hard coded numbers by using default parameters. We get the benfit of calling simple method signitures when we just want to calcuate the most optimal ticket price, while still allowing for variance in the problem space.

## What is bad about this solution

My solution is not without its own problems, many of which David Beazley highlighted in his talk. 
- Floating point errors
- No abstractions to deal with changes in the business logic
- Magic formula that gives no insight to its correctness or what problem it actually solves

## What is the purpose

There is no right or wrong way to structure your code for this problem. This was my attempt at furthering the discussion of how developers should use abstractions in their problem solving, and when they should simplify their thinking and solve the problem at hand.

# Author
[Hunter Wilkins](https://hunterwilkins.dev)
