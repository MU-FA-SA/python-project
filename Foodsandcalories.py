def li():
    foods = []
    for items in range(int(input("ENTER THE NUMBER OF ELEMENT\n"))):
        w = input("Enter the elements\n")
        foods.append(w)
        print(foods)
    foods.sort()
    print(f'THE ELEMENTS ARE SORTED {foods}')

    foods.reverse()
    print(f'THE ELEMENTS ARE REVERSE {foods}')

    foods[::1]
    print(f'THE ELEMENTS ARE SLICED {foods}')

    foods[0],foods[-1]=foods[-1],foods[0]
    print(f'THE FIRST ELEMENTS ARE INTERCHANGED {foods}')
    foods[1],foods[-2] = foods[-2],foods[1]
    print(f'THE SECOND ELEMENTS ARE INTERCHANGED {foods}')



if __name__ == '__main__':
    li()