import os
import random
import pandas as pd

# የKeno ዳታ የሚቀመጥበት ፋይል ስም
DATA_FILE = "keno_history.csv"


def generate_mock_live_data():
    """እውነተኛው API እስኪገኝ ድረስ በየደቂቃው 20 የKeno ቁጥሮችን በዘፈቀደ የሚሰጥ"""
    return sorted(random.sample(range(1, 81), 20))


def save_and_predict():
    # 1. አዲስ ቁጥሮችን ማግኘት
    live_numbers = generate_mock_live_data()
    print(f"የአሁኑ ዙር ቁጥሮች: {live_numbers}")

    # 2. ዳታውን በCSV ፋይል ውስጥ ማስቀመጥ
    new_data = pd.DataFrame([live_numbers])
    if not os.path.exists(DATA_FILE):
        new_data.to_csv(DATA_FILE, index=False)
    else:
        new_data.to_csv(DATA_FILE, mode="a", header=False, index=False)

    # 3. ያለፉትን ቁጥሮች በመተንተን ቀጣዩን መገመት (Frequency Analysis)
    df = pd.read_csv(DATA_FILE)
    all_numbers = df.values.flatten()
    # በብዛት የወጡ 5 ቁጥሮችን መለየት
    hot_numbers = pd.Series(all_numbers).value_counts().head(5).index.tolist()

    print(f"--- [Winner's Mindset Prediction] ---")
    print(f"ለቀጣዩ ዙር በብዛት ሊወጡ የሚችሉ (Hot) ቁጥሮች: {hot_numbers}")


if __name__ == "__main__":
    save_and_predict()
