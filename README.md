# Django Weather and Currency Tracker

## Overview

**Django Weather and Currency Tracker** is a sophisticated web application designed to deliver real-time weather updates and currency conversion services. Leveraging Django, a high-level Python web framework, this project integrates with various APIs to provide accurate and timely information on weather conditions and currency exchange rates.

## Features

- **Real-Time Weather Information**: Access up-to-date weather details for any global location.
- **Currency Conversion**: Convert amounts between different currencies with the latest exchange rates.
- **User-Friendly Interface**: Designed for simplicity and ease of use, with an intuitive layout.
- **Responsive Design**: Ensures a seamless experience across both desktop and mobile devices.

## Technologies Used

- **Django**: The core framework powering the backend, facilitating rapid development and robust design.
- **Python**: The programming language employed for backend logic.
- **External APIs**: Integrated services for real-time data retrieval:
  - **Weather API**: Provides current weather information.
  - **Currency Conversion API**: Delivers live exchange rates for currency conversion.
- **HTML/CSS**: Technologies used for frontend structuring and styling.
- **JavaScript**: Enhances interactivity and dynamic content on the user interface.

## Installation

To set up and run this project locally, follow these steps:

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

## API Keys

To utilize the weather and currency APIs, you need to acquire API keys. Refer to the project's configuration settings to input your API keys.

## Usage

- **Weather Functionality**: Enter a city name or geographical coordinates to receive current weather updates.
- **Currency Conversion**: Select the source and target currencies and input the amount for conversion.


## Contact

For questions or further information, please reach out to me at [your-email@example.com](mailto:syedsherali263@gmail.com).
