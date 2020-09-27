def get_ages(df, sex):
    """Returns the ages of men or women, whom Embarked from section C.
    
       Parameters:
       df(pyspark.sql.DataFrame): based on the titanic.csv module
       sex(str): for our dataset, it is a binary classification of 'male' or 'female'
       
       Returns: List[float]
    
    """
    # get ages of those whom Embarked from 'C', and sex
    people_embarked_C_ages = df.filter((df.Embarked == 'C') & (df.Sex == sex)).rdd.map(lambda person: person.Age).collect()
    return people_embarked_C_ages
