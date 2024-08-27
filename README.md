# Django Weather and Currency Tracker

## Overview

**Django Weather and Currency Tracker** is a sophisticated web application that provides real-time weather updates and currency conversion services. Built with Django, this application integrates with external APIs to offer accurate and current data on weather conditions and currency exchange rates.

## Features

- **Real-Time Weather Information**: Get up-to-date weather details for any location globally.
- **Currency Conversion**: Convert amounts between different currencies using the latest exchange rates.
- **User-Friendly Interface**: Simple and intuitive layout for ease of use.
- **Responsive Design**: Ensures optimal experience across desktop and mobile devices.

## Technologies Used

- **Django**: The main framework powering the backend, facilitating rapid development and scalability.
- **Python**: Used for backend logic and API interactions.
- **External APIs**:
  - **Weather API**: Provides real-time weather data.
  - **Currency Conversion API**: Supplies live exchange rates for currency conversion.
- **HTML/CSS**: For frontend structure and styling.
- **JavaScript**: Enhances interactivity and dynamic content.

## Django Integration with APIs

- **Weather API Integration**: Django uses the [WeatherStack API](https://weatherstack.com/documentation) to fetch current weather data. Requests are made to the API to retrieve and display weather information on the application's frontend.

- **Currency Conversion API Integration**: The [ExchangeRate-API](https://www.exchangerate-api.com/documentation) is integrated for currency conversion. Django handles requests to the API to get exchange rates and perform currency conversions based on user inputs.

## Installation

To set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sherali143/DjangoWeatherCurrencyTracker.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd DjangoWeatherCurrencyTracker
   ```

3. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv newenv
   source newenv/bin/activate  # On Windows: newenv\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/` to interact with the application.

## API Keys and URLs

To use the external APIs, you will need to obtain your own API keys and update the project configuration:

- **Currency Conversion API**:
  - **API Key**: Obtain from [ExchangeRate-API](https://www.exchangerate-api.com/).
  - **API URL**: Example format:
    ```python
    EXCHANGE_RATE_API_URL = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest/USD'
    ```

- **Weather API**:
  - **API Key**: Obtain from [WeatherStack](https://weatherstack.com/).
  - **API URL**: Example format:
    ```python
    WEATHER_API_URL = f'https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}'
    ```

Replace `'your_api_key_here'` with your actual API keys in the project’s configuration files.

## Usage

- **Weather Functionality**: Enter a city name or coordinates to view current weather updates.
- **Currency Conversion**: Select source and target currencies and input the amount for conversion.

## Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/28ee902c-b70a-4e0a-bc3d-bb0b00bc6988)

### Weather Check Page
![Weather Check Page](https://github.com/user-attachments/assets/0785183c-9571-459b-b468-6df26c49ae74)

### Currency Converter Page
![Currency Converter Page](https://github.com/user-attachments/assets/ad02e860-14a9-4c52-8a1e-ebb13943c81e)

## Contact

For questions or further information, please reach out to me at [syedsherali263@gmail.com](mailto:syedsherali263@gmail.com).
