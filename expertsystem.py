while True:
    print("\n--- Course/Stream Selector ---")

    stream = input("Enter your stream (PCM / PCB / PCMB / COMMERCE / ARTS): ").upper()
    interest = input("Enter your interest (coding / biology / maths / business / design / teaching): ").lower()
    percent = float(input("Enter your percentage: "))

    print("\n--- Suggested Career Options ---")

    if stream == "PCM":
        if percent >= 75:
            if interest == "coding":
                print("-> B.Tech / Engineering (Computer Science, IT)")
            elif interest == "maths":
                print("-> B.Sc Mathematics / Data Science / Statistics")
            else:
                print("-> Engineering or NDA / Defense")
        else:
            print("-> Diploma Engineering / BCA / Basic Science Courses")

    elif stream == "PCB":
        if percent >= 80:
            if interest == "biology":
                print("-> MBBS / BDS / Medical Field")
            else:
                print("-> Pharmacy / Nursing / Biotechnology")
        else:
            print("-> B.Sc Biology / Allied Health Sciences")

    elif stream == "PCMB":
        if percent >= 85:
            if interest == "coding":
                print("-> Engineering (CS/IT)")
            elif interest == "biology":
                print("-> Medical (MBBS)")
            else:
                print("-> Choose between Engineering or Medical")
        else:
            print("-> B.Sc (General) / Mixed Fields")

    elif stream == "COMMERCE":
        if percent >= 70:
            if interest == "business":
                print("-> BBA / B.Com / CA / CS")
            else:
                print("-> Economics / Banking / Finance")
        else:
            print("-> B.Com (General) / Diploma Courses")

    elif stream == "ARTS":
        if percent >= 65:
            if interest == "teaching":
                print("-> BA + B.Ed / Lecturer")
            elif interest == "design":
                print("-> Fashion Design / Graphic Design / Fine Arts")
            else:
                print("-> Civil Services / Psychology / Sociology")
        else:
            print("-> BA (General) / Skill-based Courses")

    else:
        print("Invalid stream entered!")

    choice = input("\nDo you want to try again? (yes/no): ").lower()
    if choice != "yes":
        print("Thank you for using Course Selector!")
        break
