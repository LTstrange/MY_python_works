import tkinter as tk


def HanoiTowerMove(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        HanoiTowerMove(n-1, a, c, b)
        HanoiTowerMove(1, a, b, c)
        HanoiTowerMove(n-1, b, a, c)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("hanoi tower")
    window.geometry('200x100')

    var = tk.StringVar()

    l = tk.Label(window, textvariable=var, bg='white', font=('Arial', 12), width=15, height=2)

    l.pack()
    on_hit = False

    def hit_me():
        global on_hit
        if not on_hit:
            on_hit = True
            var.set('you hit me')
        else:
            on_hit = False
            var.set('')

    b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
    b.pack()

    window.mainloop()
    HanoiTowerMove(3, 'A', 'B', 'C')
