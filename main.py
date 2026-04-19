import math

def zeroes(a,b,c) -> tuple[int, int]:
    """Assumes discriminant is a perfect square. Doesn't care if it's a double root lol."""
    discr = b**2-(4*a*c)
    denominator=(2*a)
    return (
        (-b-math.sqrt(discr))/denominator,
        (-b+math.sqrt(discr))/denominator
    )

if __name__ == "__main__":

    box_x_box=True
    t=0.0
    dist_boxes=0.0
    dist_box_wall=1.0

    m1=1
    m2=10

    v1=0.0
    v2=1.0

    for i in range(6):
        assert dist_boxes>=0
        assert dist_box_wall>=0
        
        print("-"*20)
        print(f"Post Collision {i+1}")
        print(f"Time: {t:.2f}")
        print(f"Distances: {dist_boxes:.2f} | {dist_box_wall:.2f}")
        print(f"Velocities: {v1:.2f} | {v2:.2f}")
        print(f"Current collision is box and box?: {not box_x_box}")
        if box_x_box:
            rel_v = v2-v1
            delta_t = dist_boxes/rel_v
            t += delta_t
            dist_boxes=0
            dist_box_wall-=(delta_t*v1)


            # v1-v2=u2-u1
            # rel_v=u2-u1
            # v1=v2+rel_v
            # 5=1/2(v1)^2+5(v2)^2
            # 1/2(v2+(rel_v))^2+5(v2)^2-5=0
            # 1/2(v2^2+2*rel_v*v2+rel_v^2)+5(v2^2)-5=0
            # 11/2(v2^2)+rel_v*v2+rel_v^2-5=0
            # a=11/2, b=rel_v, c=rel_v^2-5
            alpha, beta = zeroes(11/2, rel_v, rel_v**2/2-5)

            # for a root to be the correct root, the value f or v_2 must support(i forgot the verb im really tired)
            # m1*u1+m2*u2=m1*v1+m2*v2
            # since v1=v2+rel_v
            # m1*u1+m2*u2=v2*(m2+m1)+rel_v*m1
            if m1*v1+m2*v2 == alpha*(m2+m1)+rel_v*m1:
                v2=alpha
            elif m1*v1+m2*v2 == beta*(m2+m1)+rel_v*m1:
                v2=beta
            else:
                print("you should probably meditate")
                print(beta*(m2+m1)+rel_v*m1)
                print(alpha*(m2+m1)+rel_v*m1)
                print(m1*v1+m2*v2)
                print(alpha, beta)
                print(rel_v)
                print(v1, v2)
                print(11/2, rel_v, rel_v**2-10)
                raise ValueError()
            #print(11/2, rel_v, rel_v**2-10)
            v1 = v2+rel_v
        else:
            assert v1>=v2 # If this is false, physics has failed you
            delta_t = dist_box_wall/v1
            t+=delta_t
            dist_box_wall=0
            rel_v=v2-v1
            dist_boxes+=(rel_v*delta_t)
            v2*=-1

        box_x_box=not box_x_box

    print("-"*20)
    print("Final")
    print(f"Time: {t:.2f}")
    print(f"Distances: {dist_boxes:.2f} | {dist_box_wall:.2f}")
    print(f"Velocities: {v1:.2f} | {v2:.2f}")