# perceptron-flask-docker-hw
This repository is created as a part of homework for Real Time Analytics course.<br />
This enables deploying a sklearn model (perceptron model with Iris dataset) using Flask and a Docker container.

### Tips for querying the prediction API with new input data
Our perceptron prediction model is based on using only 2 columns (sepal length, petal length) of Iris dataset.<br />
Accordingly, please input like below *(this is just an example, you can input any float number as an input)*:<br />

- sepal length = 4.6
- petal length = 1.7

### In Your Browser
Paste this URL into your browser bar:<br />
`http://localhost:3333/api/v1.0/predict?sl=4.6&pl=1.7`

Then, you should expect to see the result as below in your browser.
```
{"features":[4.6,1.7],"predicted_class":-1}
```
<img width="722" alt="Screen Shot 2022-05-16 at 6 20 00 PM" src="https://user-images.githubusercontent.com/53321802/168643189-5b3ef26f-6e33-4574-b51d-d59aa8809ade.png">

In here, "predicted_class":-1 means that the predicted class is "Iris setosa".<br /> 
If predicted_class returns 1 as a result, it means it's classified as "Else" (In real dataset, it would be either "Iris Versicolor" or "Iris Virginica").<br />

### When you are opening the browser from DOCKER container
Just like above, you can click open in browser and don't forget to add `/api/v1.0/predict?sl=4.6&pl=1.7` at the end of the address showing up in your browser address bar. In here, the sl(sepal length) and pl(petal length) can be changed into whatever float input as you wish to check the predicted result.

![Screen Shot 2022-05-16 at 6 53 15 PM](https://user-images.githubusercontent.com/53321802/168644107-88fefea1-a302-4c9f-bb1b-5d0fa368350e.png)

