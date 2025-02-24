## **🛫 Flight Price Tracker**  

Track flight prices automatically and get notified via SMS when there's a good deal! 📉💰  

---

## **📌 Features**  
✅ Fetches flight prices using **Amadeus API** ✈️  
✅ Stores and organizes data using **Google Sheets (Sheety API)** 📊  
✅ Compares collected prices with existing ones in Google Sheets 🔍  
✅ Sends an **SMS alert via Twilio API** when a cheaper flight is found! 📩  

---

## **🛠 Tech Stack**  
🔹 **Python** 🐍  
🔹 **Requests module** (for API calls) 🔗  
🔹 **Os module** (for storing environment variables) 🔐  
🔹 **Amadeus API** (Flight data) 🛫  
🔹 **Sheety API** (Google Sheets integration) 📄  
🔹 **Twilio API** (SMS notifications) 📲  

---

## **🚀 How It Works**  

1️⃣ **Collect Flight Data**  
- Fetches flights, prices, and departure dates from the **Amadeus API**.  

2️⃣ **Store & Organize**  
- Saves the flight data into a **Google Sheet** via **Sheety API**.  

3️⃣ **Compare Prices**  
- Reads the Google Sheet and **checks if a lower price** is found.  

4️⃣ **Send SMS Alerts**  
- If a cheaper flight is available, it sends an **SMS notification** with the flight details and price using **Twilio API**.  

---

## **📂 Project Structure**  

```
📦 flight-deals-start
│── src/
│   ├── api/
│   │   ├── data_manager.py    # Handles Google Sheets API (Sheety)
│   │   ├── flight_search.py   # Fetches flight data from Amadeus API
│   ├── services/
│   │   ├── flight_data.py     # Processes flight data and compares prices
│   ├── flight_data.py         # Handles the logic to find the best price
│   ├── main.py                # Runs the program
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
```

---

## **🔧 Setup & Installation**  

1️⃣ **Clone this repository**  
```bash
git clone https://github.com/Nickkcj/Flight-Price-Tracker.git
cd flight-deals-start
```

2️⃣ **Create a virtual environment** (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate 
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Set up environment variables**  
- Create a `.env` file and add your API keys:  
```
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret
SHEETY_ENDPOINT=your_sheety_api_endpoint
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE=your_twilio_phone_number
MY_PHONE=your_phone_number
```

5️⃣ **Run the project**  
```bash
python src/main.py
```

---

## **📌 Example SMS Notification**  

📩 **Flight Alert:**  
✈️ **New York → London**  
📅 **Departure:** 2024-06-15  
💰 **Price:** $299  

_"Hurry up! This deal won't last long!"_

---
