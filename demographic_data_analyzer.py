import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    

    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[["sex", "age"]].groupby("sex").mean().iat[1,0],1)

    # What is the percentage of people who have a Bachelor's degree?
    education_all = df['education'].value_counts(normalize=True) * 100
    percentage_bachelors = round(education_all.loc['Bachelors'],1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    education_salary = df[["education", "salary"]]
    EducationHigher_50K = education_salary[((education_salary['salary']=='>50K') & (education_salary['education']== 'Masters')) |  ((education_salary['salary']=='>50K') & (education_salary['education']== 'Bachelors')) | ((education_salary['salary']=='>50K') & (education_salary['education']== 'Doctorate'))].value_counts()
    SumOfEducationHigher_50K = EducationHigher_50K.sum()

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    
    EducationHigher = education_salary[( (education_salary['education']== 'Masters')) |  ( (education_salary['education']== 'Bachelors')) | ((education_salary['education']== 'Doctorate'))].value_counts()

    # percentage with salary >50K
    higher_education_rich = round(SumOfEducationHigher_50K/EducationHigher.sum()*100,1)
    
    EducationLower = education_salary[( (education_salary['education']!= 'Masters')) &  ( (education_salary['education']!= 'Bachelors')) & ((education_salary['education']!= 'Doctorate'))].value_counts()
    EducationLower_50K = education_salary[((education_salary['salary']=='>50K') & (education_salary['education']!= 'Masters')) &  ((education_salary['salary']=='>50K') & (education_salary['education']!= 'Bachelors')) & ((education_salary['salary']=='>50K') & (education_salary['education'] != 'Doctorate'))].value_counts()
    lower_education_rich = round(EducationLower_50K.sum()/EducationLower.sum() *100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    hoursPerWeek = df[["salary","hours-per-week"]]
    min_work_hours = hoursPerWeek['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = hoursPerWeek[hoursPerWeek['hours-per-week'] == min_work_hours ].value_counts(normalize=True)*100

    rich_percentage = num_min_workers[1]

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    CountryOcupationSalary = df[["occupation","salary","native-country"]]
    topOccupation = CountryOcupationSalary[(CountryOcupationSalary['salary']=='<=50K') & (CountryOcupationSalary['native-country']=='India')].value_counts().idxmax()
    top_IN_occupation = topOccupation[0]

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
