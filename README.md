Diabetes Predictor ML Model
===========================

### Introduction

-   The global disease burden of diabetes increased greatly from 1990 to 2017 .Diabetes mellitus is a leading cause of mortality and reduced life expectancy.The global prevalence of diabetes increased from 211.2 million (196.0--228.5) in 1990 to 476.0 million (436.6--522.8) in 2017, with a 129.7% increase. Global deaths due to diabetes increased from 0.61 million (0.59--0.62) in 1990 to 1.37 million (1.34--1.40) in 2017, with a 125.5% increase.
-   This is a project made for exploration and predicting whether a person can have diabetes or not.This is an Machine Learning Predictive Model for which i have used RandomForestRegressor method. A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The reason for choosing RFR method and its advantages is further explained in testing and training.

### Dataset

-   There was a research conducted on the Pima Indians community near Pheonix, Arizona. The population was under continues study since 1965 by the [National Institute of Diabetes and Digestive and Kidney Diseases](https://www.niddk.nih.gov/) because of the high instance of diabetes only in that particular community. Eight parameters were selected for the research which included

### Parameters

-   Pregnancies
-   Glucose Level
-   Blood Pressure
-   Skin Thickness
-   Insulin Level
-   Bmi
-   Diabetes Pedigree Function
-   Age
-   While interpreting the Ml model by analysing the weights of the parameters, the following conclusions were found
    1.  Parameters like Glucose Level, BMI, Pregnancies, Diabetes Pedigree Function and Age were found directly proportional to the chances of having diabetes.
    2.  Whereas parameters like Skin Thickness, Insulin Level, and Blood Pressure were found inversely proportional to chances of having diabetes.

### The Region Parameter

-   The diabetes condition is not constant throughout the world. Different locations, Different epitite and Different enviornments may alter the chances of getting diabeties.
-   For Example , Asia and America have highest prevelence number, thus we can say people belonging to those regions may have higher chances of getting diabetes. Whereas regions like Greenland have the lowest prevelence number and thus people belonging to those regions have the lowest chances of getting diabetes.
-   To know more about this [Click Here](https://www.nature.com/articles/s41598-020-71908-9#).)
-   Here is a photo depicting the prevelence number of diabetes throughout the world.
-   ![](https://yourdiabetespredictor.herokuapp.com/static/website/world_prevelance.30f9894abeed.png)
original copyright belongs to [nature.com](https://www.nature.com/)

###### Thus for every country belonging to these regions , i have made a small addition in the final percentage based on the region.

### Conclusion and Result

-   This is only a predictive model and works though a machine learning model designed by me. There is no guarantee that the prediction may be 100 percent correct. But these predictions may give you a rough estimate on your chances of getting diabetes.

### Model Working

-   The model is firstly sorted on the basis of gender cause the survey has a high proportion of women.
    -   For males, the model is constructed without the pregnancy as a parameter and due to less parameters, the model is less predictable.
    -   For females, the model is constructed with the pregnancy as a parameter and thus predictions for females are more predictable.
-   Predictions above 85 percent are considered to be as high, between 75 and 85 are termed to be as average and below 75 are termed to be low.
-   The model uses the random regressor model and make predictions based on the inputs and giving a special weightage to the region parameter and adding it to the end.

### References

-   <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2245318/?page=1>
-   <https://www.nature.com/articles/s41598-020-71908-9#>
-   <https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database>
-   <https://www.who.int/news-room/fact-sheets/detail/diabetes>
-   [National Institute of Diabetes and Digestive and Kidney Diseases](https://www.niddk.nih.gov/)

### Disclaimer

-   Due to the limitation of the hosting service the website crashes many times. Thus to run this on your local follow the following steps

    ### How to Run This on Local Website

    To deploy this project run

    ```bash

      $ pip install -r requirements.txt

    ```

    ```bash

      $ python manage.py runserver

    ```

    Woohoo!! Now the website is running on your local
