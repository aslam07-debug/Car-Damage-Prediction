# Vehicle Damage Detection App

This ML powered app lets you upload an image of a car and it tells you what kind of damage it has.
The model is trained on third quarter front and rare view hence the picture should capture the third quarter front or rare view of a car. 

![app](App_Screenshot%202026-11-11%20212935.png)


### Model Details

1. I used ResNet50 for transfer learning
2. The model was trained on around 1,700 images with 6 classes below
   1.Front Normal
   2.Front Crushed
   3.Front Breakage
   4.Rear Normal
   5.Rear Crushed
   6.Rear Breakage

The accuracy of the model on the validation set was around 80%.

### Set Up
1.To get started, first install the dependences using
```commandline
pip install -r requirements.txt

```
2. Run the streamlit app
   ```command line
   streamlit run app.py
   ```