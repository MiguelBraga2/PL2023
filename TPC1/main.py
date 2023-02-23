import plotting
from reader import Model
from distribution import Distribution
from plotting import draw_histogram


def sex_distribution(model):
    sex_dist = Distribution()
    for elem in model.model:
        sex_dist.add_element(elem.sex)

    return sex_dist


def age_distribution(model):
    age_dist = Distribution()
    for elem in model.model:
        age_dist.add_element((elem.age//5)*5)

    return age_dist

def cholesterol_distribution(model):
    cholesterol_distribution = Distribution()
    for elem in model.model:
        cholesterol_distribution.add_element(model.min_cholesterol + ((elem.cholesterol-model.min_cholesterol)//10)*10)

    return cholesterol_distribution

def main():
    model = Model()
    model.read_file('myheart.csv')
    by_sex = sex_distribution(model)
    by_age = age_distribution(model)
    by_cholesterol = cholesterol_distribution(model)

    a = 4
    while a != 0:
        a = int(input("""What distribution to see?
1 - by sex
2 - age
3 - by cholesterol
0 - leave
"""))

        if a == 1:
            print("//////////////// Distribution by sex ////////////////")
            by_sex.print_sex_distribution()
            men_count = by_sex.dist['M']
            women_count = by_sex.dist['F']
            total_count = men_count + women_count
            plotting.draw_pie_plot([men_count / total_count, women_count / total_count])
        elif a == 2:
            print("//////////////// Distribution by age ////////////////")
            by_age.print_age_distribution()
            plotting.draw_histogram(model.get_ages(), 20, 100, 5)
        elif a == 3:
            print("//////////////// Distribution by cholesterol ////////////////")
            by_cholesterol.print_cholesterol_distribution()
            plotting.draw_histogram(model.get_cholesterol(), 0, 600, 10)


if __name__ == "__main__":
    main()
