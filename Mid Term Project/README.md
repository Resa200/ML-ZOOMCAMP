# Diabetes Prediction using Machine Learning

## **About Data**

 The data used was gotten from [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_5050split_health_indicators_BRFSS2015.csv). The csv file used is a clean dataset of 70,692 survey responses to the CDC's BRFSS2015. It has an equal 50-50 split of respondents with no diabetes and with either prediabetes or diabetes. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is balanced.

 ### **Features Description**
 * Diabetes_binary - 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes.
 * HighBP - 0 = no high BP ,1 = high BP
 * HighChol - 0 = no high cholesterol ,1 = high cholesterol
 * CholCheck -0 = no cholesterol check in 5 years ,1 = yes cholesterol check in 5 years
 * BMI - Body Mass Index
 * Smoker - Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] 0 = no ,1 = yes
 * Stroke - (Ever told) you had a stroke. 0 = no ,1 = yes
 * HeartDiseaseorAttack - coronary heart disease (CHD) or myocardial infarction (MI) 0 = no ,1 = yes
* PhysActivity - physical activity in past 30 days - not including job 0 = no ,1 = yes
* Fruits - Consume Fruit 1 or more times per day 0 = no 1 = yes
* Veggies - Consume Vegetables 1 or more times per day 0 = no ,1 = yes
* HvyAlcoholConsumption - (adult men >=14 drinks per week and adult women>=7 drinks per week) 0 = no ,1 = yes
* AnyHealthcare - Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. 0 = no ,1 = yes
* NoDocbcCost - Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? 0 = no ,1 = yes
* GenHlth - Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor
* MentHlth - days of poor mental health scale 1-30 days
* PhysHlth - physical illness or injury days in past 30 days scale 1-30
* DiffWalk - Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes
* Sex - 0 = female 1 = male
* Age - 13-level age category (_AGEG5YR see codebook) 1 = 18-24 9 = 60-64 13 = 80 or older
* Education - Education level (EDUCA see codebook) scale 1-6 1 = Never attended school or only kindergarten 2 = elementary etc.
* Income - Income scale (INCOME2 see codebook) scale 1-8 1 = less than $10,000 5 = less than $35,000 8 = $75,000 or more


## Methodology 

* Data Wrangling
* EDA
* Features Selection
* Model Selection
* Model Deployment

The first four steps were carried out in [Analysis](Analysis.ipynb)