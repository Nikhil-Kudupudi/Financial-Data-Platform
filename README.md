# 💰 Financial Analysis and Investment Platform

## Project Overview

This is a comprehensive financial analysis and investment platform that empowers users with data-driven insights and a risk-free environment to learn about the US stock market. The project is a full-stack web application that integrates with various financial APIs to provide real-time data, historical performance, and advanced analytics.

## Key Features

### Stock & ETF Tracker
Search for any US-listed stock or ETF to view its real-time price, historical performance, and key metrics.

### Simulated Portfolio
A dashboard where users can manage a virtual portfolio, track their simulated gains and losses, and understand the impact of their investment decisions without financial risk.

### Fund Analysis
A section dedicated to comparing different investment funds, including mutual funds and ETFs. It displays key metrics like expense ratios and historical returns. For hedge funds, it provides a researched historical overview due to data limitations.

### Financial Modeling & Forecasting
An automated tool that generates a company's financial statements (Income Statement, Balance Sheet, Cash Flow Statement) from a single ticker symbol. It also includes a basic machine learning model for price forecasting.

### AI-Powered News & Sentiment
An integrated NLP system that fetches the latest financial news for a stock, summarizes the articles, and provides a sentiment score (positive, neutral, or negative) to help users gauge market mood.

## Technical Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript (with Chart.js for data visualization)
- **Database:** SQLite
- **APIs:**
  - **Financial Data:** Alpha Vantage, Finnhub
  - **Financial Statements:** Financial Modeling Prep (FMP)
  - **Government Filings:** SEC EDGAR database API (for advanced features)

## Getting Started

Follow these steps to get a local copy of the project up and running.

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API keys:**
   - Create a `.env` file in the root directory
   - Add your API keys from Finnhub, Alpha Vantage, etc., like this:
   ```env
   FINNHUB_API_KEY=your_key_here
   ALPHA_VANTAGE_API_KEY=your_key_here
   ```

5. **Run the application:**
   ```bash
   flask run
   ```

Your application will now be running at `http://127.0.0.1:5000/`.

## Data Resources & Limitations

### Stock & ETF Data
All data is sourced from reliable financial APIs with free access tiers.

### Mutual Funds
Data is sourced from public financial websites and is limited to publicly available information.

### Hedge Funds
Due to data being proprietary, this section is a static analysis of historical performance based on publicly available filings and research. It does not provide real-time data.

### F&O (Futures & Options)
Due to the high cost of real-time options data, this section is a conceptual demonstration.

## Contributing

This is a portfolio project, but feel free to fork the repository, explore the code, and submit any bug reports.

## License

This project is licensed under the MIT License.