def create_phone_number(n):
    for i in range(0, len(n)):
        n[i] = str(n[i])
    return f'({"".join(n[:3])}) {"".join(n[3:6])}-{"".join(n[6:])}'

def main():
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

if __name__ == "__main__":
    main()
