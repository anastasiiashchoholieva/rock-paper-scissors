# Classification Web App: rock-paper-scissors

***

The Rock, Paper, Scissors Image Classifier is an AI-powered web application that can classify images of hands as one of three categories:
rock, paper, or scissors.
Users can upload images, and the application will provide a classification label along with the probability of the prediction.


## Technologies Used

***

- TensorFlow for deep learning model creation.
- Flask for building the web application.
- HTML/CSS for the user interface.


## Deep learning model

***

- Dataset: https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors
- Google Collab: https://colab.research.google.com/drive/1zu6ASHV_XU-qUHQk1EjL9X7Dg4YfraF-?usp=sharing

## Usage

***

- Clone the repository: `git clone https://github.com/anastasiiashchoholieva/rock-paper-scissors.git`
- Run with docker:
```
docker build -t <app_name> .
docker run -p 5000:5000 <app_name>
```
## How it looks

***

![Screenshot 2023-08-23 at 19.00.34.png](static%2Fimages%2FScreenshot%202023-08-23%20at%2019.00.34.png)
![Screenshot 2023-08-23 at 19.01.06.png](static%2Fimages%2FScreenshot%202023-08-23%20at%2019.01.06.png)
![Screenshot 2023-08-23 at 19.01.16.png](static%2Fimages%2FScreenshot%202023-08-23%20at%2019.01.16.png)