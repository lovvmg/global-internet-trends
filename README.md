# 🌍 Global Internet Trends (1990-2023)

A Python-based data analysis tool that fetches, cleans, and visualizes the percentage of internet users by country over time using World Bank data. 

This project transforms a raw, messy dataset into a clean format and generates an interactive line chart. It is designed to be easily customizable so anyone can compare the internet adoption rates of their preferred countries.

---

## ✨ Features
* **Automated Data Cleaning:** Uses `pyjanitor` to standardize column names and handle string formatting.
* **Smart Missing Value Handling:** Implements Forward Fill (`ffill()`) to logically estimate missing data points in recent years without breaking historical trends.
* **Interactive Visualization:** Uses `plotly.express` to generate dynamic, hoverable charts.
* **Reusable Pipeline:** Encapsulated in clean Python functions for easy modification.

---

## 📂 Project Structure

* `internet_usage.py`: The main, refactored Python script containing the clean data pipeline and visualization functions.
* `exploration.ipynb`: The original Jupyter Notebook showing the step-by-step data exploration and "behind-the-scenes" thought process.
* `requirements.txt`: List of dependencies required to run the script.

---

## 🛠️ Installation & Setup

1. Clone this repository to your local machine:
```bash
   git clone [https://github.com/lovvmg/global-internet-trends.git](https://github.com/lovvmg//global-internet-trends.git)
Navigate to the project folder:

Bash
cd global-internet-trends
Install the required Python libraries:

Bash
pip install -r requirements.txt

🚀 How to Use
Run the Python script directly from your terminal:

Bash
python internet_usage.py
This will process the data and automatically open an interactive chart in your default web browser.

🔧 Customizing the Countries
You can easily change which countries are compared by modifying the countries list at the bottom of the internet_usage.py script:

# Change the list of countries below to fit your preferences!
countries = ["United States", "China", "India", "Brazil", "Germany", "Indonesia"] 
(Note: Ensure the country names match the official World Bank formatting).

📊 Data Source
The dataset used in this project is sourced from the World Bank (Series Code: IT.NET.USER.ZS).
