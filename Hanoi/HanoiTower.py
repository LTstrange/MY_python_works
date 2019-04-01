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
    window.geometry('1200x800')

    canvas = tk.Canvas(window, bg="white", height=400, width=800)

    x0, y0, x1, y1 = 0, 0, 80, 80
    oval = canvas.create_oval(x0, y0, x1, y1, anchor='center', fill='green')
    rect = canvas.create_rectangle(0, 0, 50, 50, fill='blue')
    canvas.pack()

    def moveit():


    b = tk.Button(window, text='move', command=moveit).pack()

    window.mainloop()
    # HanoiTowerMove(3, 'A', 'B', 'C')
