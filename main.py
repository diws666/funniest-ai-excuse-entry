import os

EXCUSE = "I outsourced your task to a smaller model. It outsourced it to a calculator. The calculator filed for overtime. The task is still pending."  # 138 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EXCUSE)
