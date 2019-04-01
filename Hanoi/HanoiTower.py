import tkinter as tk


def HanoiTowerMove(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        HanoiTowerMove(n-1, a, c, b)
        HanoiTowerMove(1, a, b, c)
        HanoiTowerMove(n-1, b, a, c)


if __name__ == "__main__":
    HanoiTowerMove(3, 'A', 'B', 'C')