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

    l = tk.Label(window, text="hanoi tower", bg='green', font=('Arial', 12), width=15, height=2)

    l.pack()

    window.mainloop()
    HanoiTowerMove(3, 'A', 'B', 'C')
