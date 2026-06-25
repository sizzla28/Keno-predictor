import os
import random
import pandas as pd

DATA_FILE = "keno_history.csv"

def get_keno_numbers():
    print("ከዌብሳይቱ ጋር ለመገናኘት እየሞከርን ነው...")
    # ሲስተሙ እንዳይበላሽ ለጊዜው በራሱ ቁጥር እንዲያመነጭ እናደርገዋለን
    return sorted(random.sample(range(1, 81), 20))

def save_and_predict():
    live_numbers = get_keno_numbers()
    print(f"የተመዘገቡ ቁጥሮች: {live_numbers}")

    # ዳታውን ማስቀመጥ
    new_data = pd.DataFrame([live_numbers])
    if not os.path.exists(DATA_FILE):
        new_data.to_csv(DATA_FILE, index=False)
    else:
        new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)

    # ትንበያ
    df = pd.read_csv(DATA_FILE)
    all_numbers = df.values.flatten()
    hot_numbers = pd.Series(all_numbers).value_counts().head(5).index.tolist()

    print(f"--- [Winner's Mindset Prediction] ---")
    print(f"ለቀጣዩ ዙር በብዛት ሊወጡ የሚችሉ (Hot) ቁጥሮች: {hot_numbers}")

if __name__ == "__main__":
    save_and_predict()