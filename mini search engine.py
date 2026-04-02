while True:
    print("\n--- Mini Search Engine ---")
    print("1. Add Data")
    print("2. Search")
    print("3. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        sentence = input("Enter text: ").strip()

        if sentence == "":
            print("Empty input not allowed ")
            continue

        with open("data.txt", "a") as file:
            file.write(sentence + "\n")

        print("Data added successfully ")

    elif choice == "2":
        try:
            with open("data.txt", "r") as file:
                data = file.readlines()

            keyword = input("Search here: ").strip().lower()

            if keyword == "":
                print("Keyword cannot be empty ")
                continue

            found = False
            count = 0

            print("\n--- Results ---")

            for  line in data:
                if keyword in line.lower():
                    print(line.strip())
                    found = True
                    count += 1

            if not found:
                print("No results found ")
            else:
                print(f"\nTotal results: {count}")

        except FileNotFoundError:
            print("No data found. Add data first ")

    elif choice == "3":
        print("Goodbye ")
        break

    else:
        print("Invalid choice ")
