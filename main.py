import math

def boxbox(m1, m2, u1, u2):
    rel_v=u1-u2
    init_m=m1**2*u1+m2**2*u2
    v1=(init_m-m2*rel_v)/(m1**2+m2**2)
    v2=v1+rel_v
    return(v1, v2)

def boxwall(u2):
    v2=-u2
    return v2

def display(t, v1, v2, x1, x2, next_box, c_count):
    print(f"{t:>5.2f} {v1:>7.2f} {v2:>7.2f} {x1:>5.2f} {x2:>5.2f} {'boxbox ' if next_box else 'boxwall'} {c_count}")

def move_boxbox(t, v1, v2, x1, x2):
    rel_v=v1-v2
    disp=x2-x1
    delta_t=disp/rel_v
    t+=delta_t
    x1+=delta_t*v1
    x2+=delta_t*v2
    return(t,v1,v2,x1,x2)

def move_boxwall(t, v1, v2, x1, x2):
    delta_t=-x2/v2
    t+=delta_t
    x1+=delta_t*v1
    x2+=delta_t*v2
    return(t,v1,v2,x1,x2)

def move(t, v1, v2, x1, x2, next_box):
    if next_box:
        return move_boxbox(t, v1, v2, x1, x2)
    else:
        return move_boxwall(t, v1, v2, x1, x2)

def collide(next_box, m1, m2, v1, v2):
    if next_box:
        assert (v1 and m1 and m2)
        return boxbox(m1, m2, v1, v2)
    else:
        return (v1, boxwall(v2))

try:
    m1 = int(input())
    assert 1<=m1<=10**10
except:
    m1 = 100

m2 = 1
t = 0.0
v1 = 1.0
v2 = 0.0
x1 = -1.0
x2 = -1.0
next_box = True
c_count = 0

sparse_printing = m1>=100
predicted_c_count = int(math.pi * m1)

print("-" * (42+len(str(c_count))))
print("  t       v1      v2    x1    x2   coll   c")

while not (v1<=v2<=0):
    c_count+=1
    t,v1,v2,x1,x2=move(t,v1,v2,x1,x2,next_box)
    v1,v2=collide(next_box,m1,m2,v1,v2)

    if not sparse_printing:
        display(t,v1,v2,x1,x2,next_box,c_count)
    elif predicted_c_count-c_count <= 20 or c_count <= 20:
        display(t,v1,v2,x1,x2,next_box,c_count)

    next_box = not next_box
    
print("-" * (42+len(str(c_count))))
print(f"Prediction: {predicted_c_count} | True: {c_count}")
print(f"pi * {m1}: {(math.pi * m1):.7f}")