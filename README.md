# 3b1b pi

i wrote this without google or internet at 1am across 2 nights.

## inspiration

Completely inspired by 3b1b's video on [why colliding blocks compute pi](https://www.youtube.com/watch?v=6dTyOl1fmDo). And physics textbook lol.

From [a text adaptation by Josh Pullen](https://www.3blue1brown.com/lessons/colliding-blocks-v2/)

> The setup involves two sliding blocks, a big one coming in from the right, a smaller one that starts of stationary to its left, and a wall to the left of both of them that the small one can bounce off of. The two blocks bounce back and forth until the big block's momentum is fully redirected, and it outpaces the small one away from the wall.  
> 
> If that first block has a mass which is some power of 100 times the mass of the second, for example 1,000,000 times as much, a ridiculously surprising fact pops out: The total number of collisions has the same starting digits as pi! In this example, that's 3,141 collisions.  

[![video of block collisions]()](https://storage.googleapis.com/3blue1brown-website-bucket/lessons/2025/colliding-blocks-v2/frictionless-elastic-collisions.mp4)

<video controls src="https://storage.googleapis.com/3blue1brown-website-bucket/lessons/2025/colliding-blocks-v2/frictionless-elastic-collisions.mp4" title="the video wont embed :("></video>

I watched the video a long time ago and recently wanted to try and do it lol :>

## explanation

total momentum in the system technically isn't constant since we treat the wall as a unmovable object.  

there are two types of collisions:
- box and box
- box and wall

in box and box collisions, momentum is conserved.  
relative velocity = u1 - u2  
intial momentum = m1 * u1 + m2 * u2  
since the collision is elastic, v2 + u2 = v1 + u1  
v2 = v1 + u1 - u2  
v2 = v1 + relative velocity  

initial momentum = final momentum    
initial momentum = m1 * v1 + m2 * v2  
initial momentum = m1 * v1 + m2 * (v1 + relative velocity)  
initial momentum = v1 * (m1 + m2) + m2 * relative velocity  
v1 = (initial momentum - m2 * relative velocity) / initial momentum  
v2 = v1 + relative velocity  

python code:
```py
rel_v=u1-u2
init_m=m1*u1+m2*u2
v1=(init_m-m2*rel_v)/(m1+m2)
v2=v1+rel_v
return(v1, v2)
```

in box and wall collisions, the box's velocity is multiplied by -1 lol that's it.  
definitely how collisions work trust me :>

move_boxbox handles movement from post boxwall collision to boxbox collision
move_boxwall handles movement from post boxbox collision to boxwall collision

if you want to know why it computes pi you should watch 3b1b video if you haven't already.  
also for small n it's not right sometimes if you know please tell me owo  

## contents

`old.py` contains really bad code where I tried to calculate the outcome of elastic collisions using a quadratic. Uses KE and doesn't work.

`main.py` has "finished" code you run it and enter a positive integer and it will calculate pi*m1 through physics

`outputs.txt` contains some sample outputs 

## usage

you need python 3 for this
```bash
python3 main.py
```
or
```bash
python main.py
```
then enter a positive integer for m2, if you don't enter an integer between 1 and 10^15 inclusive it will default to 100  
if you dont want to choose just press enter and it'll default to 100  
if you enter a number larger than 100 then it will print the first 20 and the last 20 collisions only  
you should probably enter a number that is 100^n  
it will takes a while for big numbers.

# if you don't have python available you can look at sample outputs in `outputs.txt`