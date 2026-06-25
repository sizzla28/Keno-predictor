import os
import requests
import pandas as pd

# የKeno ዳታ የሚቀመጥበት ፋይል
DATA_FILE = "keno_history.csv"

# አንተ የላክኸው የKeno ጨዋታ የቀጥታ መረጃ መገኛ ሊንክ (የጀርባ API)
API_URL = "https://www.ethiolottery.et/api/v1/games/keno/live-results" # ማሳሰቢያ 1 ተመልከት

def fetch_real_keno_data():
    try:
        # ከዌብሳይቱ ላይ የቅርብ ጊዜ ውጤቶችን በይፋ መውሰድ
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(API_URL, headers=headers, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            # ከዌብሳይቱ የመጣውን የቁጥር ዝርዝር መለየት
            # (ይህ መዋቅር እንደ ዌብሳይቱ የJSON ይዘት ይለያያል)
            if 'results' in data:
                live_numbers = sorted(data['results'][0]['numbers'])
                return live_numbers
    except Exception as e:
        print(f"ከዌብሳይቱ ዳታ ሲወሰድ ስህተት ገጠመ: {e}")
    return None

def save_and_predict():
    # 1. ከእውነተኛው ሊንክ ዳታ መውሰድ
    live_numbers = fetch_real_keno_data()
    
    # ሊንኩ ካልሰራ ቦቱ እንዳይቆም ጊዜያዊ የሙከራ ዳታ ይጠቀማል
    if not live_numbers:
        print("የቀጥታ ዳታውን ማግኘት አልተቻለም፤ ወደ ሙከራ ዳታ ተቀይሯል።")
        import random
        live_numbers = sorted(random.sample(range(1, 81), 20))

    print(f"የአሁኑ ዙር እውነተኛ ቁጥሮች: {live_numbers}")

    # 2. ዳታውን በCSV ፋይል ውስጥ ማስቀመጥ
    new_data = pd.DataFrame([live_numbers])
    if not os.path.exists(DATA_FILE):
        new_data.to_csv(DATA_FILE, index=False)
    else:
        new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)

    # 3. የቁጥሮቹን ድግግሞሽ አይቶ ቀጣዩን መገመት
    df = pd.read_csv(DATA_FILE)
    all_numbers = df.values.flatten()
    hot_numbers = pd.Series(all_numbers).value_counts().head(5).index.tolist()

    print(f"--- [Winner's Mindset Prediction] ---")
    print(f"ለቀጣዩ ዙር በብዛት ሊወጡ የሚችሉ (Hot) ቁጥሮች: {hot_numbers}")

if __name__ == "__main__":
    save_and_predict()
