### Description
This is the midterm project for the DataTalks Club ML Zoomcamp 2024.

In this project we will build a web service that predicts house prices.

When we want to sell a house we visit a real estate site and provide all the house information we want to be available to a possible buyer. The problem arises when we want to find a suitable house price. What we usually do is we try to find other listed houses with similar characteristics and their prices. Most of the times this is a very time consuming procedure.

So to help a house seller find a house price more easily we are going to build a web service. When the user fills in all the house characteristics, those characteristics will be send to the web service which will actually be a model that will predict the house price and return it to the user.

This procedure will make the sellers experience easier and of course quicker.

### Dataset

We will use **Jiffs house price prediction** dataset from Kaggle. The dataset can be found in the URL below:

https://www.kaggle.com/datasets/elakiricoder/jiffs-house-price-prediction-dataset

but you don't need to download it. It can be found in the **data** folder as **data.csv**

### Tecnologies used

#### Streamlit
![image info](./images/streamlit.png)  
Streamlit is used to create the user interface (UI). The user types a question, hits the Enter button and after a while an answer is produced by the assistant. The user
question and the generated answered are stored in the Postgres database. There are also Thumbs Up and Thumbs Down buttons so that the user can provide a feedback. 
Thumbs Up for a relevant answer and Thumbs Down for a non relevant answer. Feedback is also stored in the Postgres database.

#### Docker
![image info](./images/docker.png)  
Every application component mentioned above is actually a docker container. When we start the application all the containers start one by one in a specific order until the user interface is presented to the user and we can start typing questions.
