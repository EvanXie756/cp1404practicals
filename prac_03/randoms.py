# line 1 picks a random number between 5 and 20
# The smallest number I could have seen is 4 and the largest number I could have seen is 19


# line 2 gives a random number between 3 and 10, starts from 3 and increase by every 2
# The smallest number I could have seen is 3 and largets number I seen is 9, line 2 could not produce 4 as the
# code starts at 3 iterates in 2

# line 3 gives an random number between 2.5 and 5.5 with a floating integer
# the smallest number I saw I was 2.6 and the biggest number I saw was 5.3

import random
random_number = random.randint(1, 100)
print(f"{random_number}")
