def toh(n, start, aux, end):
    if n == 0:
        return
    toh(n-1, start, end, aux)
    print(f"Move disk {n} from {start} to {end}")
    toh(n-1, aux, start, end)


n = 4

toh(n, "A", "B", "C")

