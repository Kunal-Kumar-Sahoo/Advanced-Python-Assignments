def display_quiz(file_path):
    with open(file_path, 'r') as file:
        contents = file.readlines()
        for line in contents:
            print(line, end='')
    print()


if __name__ == '__main__':
    display_quiz('./31-07-2023/quiz.txt')