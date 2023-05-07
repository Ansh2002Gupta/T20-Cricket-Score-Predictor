# T20-Cricket-Score-Predictor
A **ML powered web facilitated application** that can predict the score of a **T20 match after the end of 20th over** for the batting team. You just need to provide certain inputs and the magic happens!
<hr>

### If you quickly wanna try my model, do this:
* Search for `app.py` in the repository.
* See on the right corner and find `raw` button, open the raw version of app.py.
* Copy the `url` from the address bar.
* Open an IDE, prefer `VSCode`.
* Install `streamlit` using `pip` or `conda`.
* Open the terminal of VSCode and type `streamlit run <url you had copied>`.
* Wait for some time, till a new browser window opens.
* Test the application and Enjoy!!

### Features
* `Interface`: The predictor is web deployed **streamlit** powered ML application, with a simple user interface. 
* `Accuracy`: The model has an accuracy of **93%**. More the overs passed better are the predictions.
* `User Friendliness`: The model takes just the necessary number of inputs that are required for making predictions. It has drop down features that make the work of the user handy. The required necessary features have been mentioned below:-
  > Batting Team <br>
  > Bowling Team <br>
  > Current Score <br>
  > Overs done <br>
  > Wickets left <br>
  > Runs scored in last 5 overs <br>
* `Time Complexity`: Outputs are given with a lightning speed.
* `Advanced ML Libraries`: The training and testing of the model is done through advanced ML libraries (you might need to install them using **pip** or **conda**), these are:
  > XGBOOST <br>
  > SKLEARN <br>
  > STREAMLIT <br>
  > NUMPY <br>
  > PANDAS <br>
  > PICKLE <br>

### Background Details
* The dataset that is used for model training and testing purposes can be downloaded from kaggle, named [Cricsheet Dataset]([www.google.com](https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket))
* Since, our dataset contains a lot of noise, null values, unnecessary data and features, they need to be filtered out. This is elaboratorily shown in `DataExtraction.ipynb` file.
* Moreover, we need to get those features over which our predictions would depend, this is done by feature extraction, that is elaboratorily shown in `FeatureExtraction.ipynb` file.
* After these two steps, we get the `final dataframe` that is used for training the ML model.
* The most important file is `pipe.pkl` that contains our trained model. Without this file, you will not be able to run the program.

### Things to keep in mind
* The feature `Overs done` takes values greater than 5. This means that atleast 5 overs should have been played before the predictions are made.
* `DataExtraction.ipynb` and `FeatureExtraction.ipynb` files are just provided for reference. They need not be to downloaded.

### User Guide
* First, download all the necessary files. This include the-
  > * `app.py`
  > * `pipe.pkl`
* Save these files in one common directory.
* Open `app.py` in a IDE, I used *VScode* :).
* You might need to install some of the python packages like, streamlit, pandas, numpy etc. This can simply be done through terminal using `pip` command.
* Finally open the terminal -> Navigate to the current directory -> type `streamlit run app.py` -> wait a little -> a browser window opens up like this.<br>
![2023-05-07-20-11-15](https://user-images.githubusercontent.com/84438495/236684514-ffa5eb5e-4c75-48f5-a64d-7a5e704961e4.png)

---
Made By: <br>
Ansh Gupta. <br>
B.Tech, <br>
Computer Science and Engineering. <br>
Thank You.
