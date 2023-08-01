from csv import reader

def read_csv(file_path):
    with open(file_path, 'r') as file:
        csv_content = reader(file, delimiter=',')
        return list(csv_content)

def list2dict(reader):
    dictionary = dict()
    for line in reader:
        dictionary[line[0]] = list(map(int, line[1:]))
    return dictionary

def mean(list):
    return sum(list) / len(list)

def display_average(dictionary):
    print('Student\t\t\t Average grade')
    for key in dictionary:
        print(f'{key}\t\t\t {mean(dictionary[key])}')


if __name__ == '__main__':
    file_path = './31-07-2023/grades.csv'
    display_average(
        dictionary=list2dict(
            reader=read_csv(
                file_path=file_path
            )
        )
    )