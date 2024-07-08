import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'C:/Users/Alex/Desktop/Project/datasets1.csv'
df = pd.read_csv(file_path)


# Rename columns to fit Prophet's requirements
df.rename(columns={'Date': 'ds', 'Amount': 'y'}, inplace=True)

# Ensure the date column is in datetime format
df['ds'] = pd.to_datetime(df['ds'])

# Initialize the Prophet model
model = Prophet()

# Fit the model on the dataset
model.fit(df)

# Create a dataframe with future dates for forecasting
<<<<<<< Updated upstream
future = model.make_future_dataframe(periods=60)  # Forecasting for the next 30 days
=======
<<<<<<< HEAD
future = model.make_future_dataframe(periods=65)  # Forecasting for the next 30 days
=======
future = model.make_future_dataframe(periods=60)  # Forecasting for the next 30 days
>>>>>>> 46632a13658b8d3d451bd999aa5e307c95faf5e3
>>>>>>> Stashed changes

# Make the forecast
forecast = model.predict(future)

# Display the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())

# Plot the forecast
fig = model.plot(forecast)
fig2 = model.plot_components(forecast)
plt.show()

fig3 = model.predict_seasonal_components(forecast)
#this is a new comment

