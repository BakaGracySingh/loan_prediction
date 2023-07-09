# Loan eligible prediction

This project use to predict is Loan get approved or not based on applicant condition

## Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [imblearn](https://imbalanced-learn.org/stable/)
- [streamlit](https://streamlit.io/)


## Usage

first, you can clone this git repository

```
git clone https://github.com/HillalXD/Loan-eligible-prediction.git
```

then navigate your command to this directory

```
cd Loan-eligible-prediction
```

after that run `streamlit-loan.py` to use streamlit app

```
streamlit run streamlit-loan.py
```


## Code 
- Template code is provided in the `loan.ipynb` notebook file.
- `loan-dataset.csv` is provide data source for training model
- `streamlit-loan.py` is streamlit web application to user input features for model predicting loan approval

## Dataset features

for doing prediction you need to input this features:

| features  | explanation  | 
| :-------- | :------- | 
| gender | user applicant gender |
| married  | is applicant has married or not |
| dependents  | is applicant has dependent or not |
| education | is applicant has graduate or not |
| Applicant income | total applicant income |
| loan amount | total applying amount |
| property_area | apllicant property type (rural, semiurban, urban) |
| credit_history  | 1 if good and 0 if bad history |





