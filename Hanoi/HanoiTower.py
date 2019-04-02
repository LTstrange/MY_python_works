import turtle

TURTLE_SPEED = 5

def draw_poles(n):
    t = turtle.Turtle()
    t.ht()
    t.pu()
    t.speed(0)
    t.pensize(5)
    for i in range(3):
        t.goto(-200+i*200, 10*n)
        t.pd()
        t.goto(-200+i*200, -100)
        t.goto(-250+i*200, -100)
        t.goto(-150+i*200, -100)
        t.pu()
    p_sq = dict(enumerate([[] for _ in range(3)]))
    return p_sq


def set_blocks(n):
    sq = []
    for i in range(n):
        t = turtle.Turtle()
        t.speed(TURTLE_SPEED)
        t.pu()
        t.shape("square")
        t.shapesize(1, i+1)
        t.goto(-200, -110+20*(n-i))
        sq.append(t)
    return sq


def move_blocks(blocks, poles, x, y):
    i = poles[x/200+1][-1]
    blocks[i].sety(150)
    blocks[i].setx(y)
    blocks[i].sety(-90+20*len(poles[y/200+1]))
    poles[y/200+1].append(poles[x/200+1].pop())
    print(poles)


def hanoi_tower(b_sq, p_sq, n, a, b, c):
    if n == 1:
        move_blocks(b_sq, p_sq, a, c)
    else:
        hanoi_tower(b_sq, p_sq, n-1, a, c, b)
        hanoi_tower(b_sq, p_sq, 1, a, b, c)
        hanoi_tower(b_sq, p_sq, n-1, b, a, c)


if __name__ == "__main__":
    n = int(input("请输入汉诺塔层数并回车:"))
    screen = turtle.Screen()
    screen.screensize(canvwidth=600, canvheight=250)
    screen.screensize(bg='gray')
    p_sq = draw_poles(n)
    l = [i for i in range(n)]
    l.reverse()
    p_sq[0].extend(l)
    print(p_sq)
    b_sq = set_blocks(n)  # sq按从小到大的顺序存放blocks
    hanoi_tower(b_sq, p_sq, n, -200, 0, 200)
    screen.exitonclick()

