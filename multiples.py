
def multiples(x):
    sum = 0
    for i in range(x):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    print(sum)

if __name__ == "__main__":
    multiples(1000)