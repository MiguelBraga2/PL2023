from reader import Model
from distribution import Distribution


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

    print("//////////////// Distribution by sex ////////////////")
    print(by_sex)

    print("//////////////// Distribution by age ////////////////")
    print(by_age)

    print("//////////////// Distribution by cholesterol ////////////////")
    print(by_cholesterol)


if __name__ == "__main__":
    main()
