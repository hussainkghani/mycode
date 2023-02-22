 #!/usr/bin/env python3
def main():

    wordbank= ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    print(tlgstudents)

    wordbank.append(4)
    print(wordbank)
    num = int(input("Enter a number between 0 and 20"))

    student_name= tlgstudents[num]

    print(f"{student_name}")

if __name__ == "__main__":
    main()
