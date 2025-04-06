# 8. And on and on and on

# The following code keeps looping forever. (You can hit Ctrl-C to stop it.) Why does the loop keep running? Modify it so that it stops after the first iteration.

while True:
    print("and on")
    break

# Why does the loop keep running?
# while True is an infinite loop as the 
# expression True always evaluates to 
# truthy - which causes the loop to 
# keep iterating until you press 'Ctrl-C'

# Modify it so that it stops after the first iteration.
# add a break keyword at the end of the block 
# to stop the iteration