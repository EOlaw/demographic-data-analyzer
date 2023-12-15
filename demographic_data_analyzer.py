import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    # I had to make the Bachelor_degree
    Bachelor_degree = df.loc[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(Bachelor_degree) / len(df)) * 100, 1)



    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(higher_education)]
    mask = df['education'].isin(['Bachelors','Masters','Doctorate'])
    lower_education = df[~mask]

    # percentage with salary >50K, I create huge_salary and higher_education_rich
    huge_salary = higher_education[higher_education['salary'] == '>50K']
    higher_education_rich = round((len(huge_salary)/len(higher_education)) * 100, 1)
    lower_education_salary = len(lower_education[lower_education['salary'] == '>50K'])
    lower_education_rich = round((lower_education_salary/len(lower_education)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask = df['hours-per-week'] == 1
    num_min_workers = len(df[mask])
    mask1 = (df['hours-per-week'] == 1) & (df['salary'] == '>50K')
    rich_num = len(df[mask1])
    rich_percentage = (rich_num/num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    country_percent = (df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100))
    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent[highest_earning_country], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    good_earn = df.loc[df['salary'] == '>50K', ['native-country', 'occupation']]
    mask3 = good_earn['native-country'] == 'India'
    india_highest_earners = good_earn[mask3]
    top_IN_occupation = india_highest_earners['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
