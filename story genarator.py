import random
who = ['a cat',' a dog','a mouse','a tiger' ]
when = ['A few years ago,','Yesterday,','Last night,','A long time ago,','On the 8th of July,']
residence = ['Barcelona','Rome','England','Egypt','Korea','Japan','America','Canada']
went = ['cinema','school','kitchen in their home',' park']
happened = ['found a missing key','solved a mystery']
print(f"{random.choice(when)} {random.choice(who)} that lived in {random.choice(residence)} went to the {random.choice(went)} and {random.choice(happened)}.")