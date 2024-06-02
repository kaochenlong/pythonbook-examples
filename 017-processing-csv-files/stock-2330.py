import csv
from matplotlib import pyplot as plot


def draw_candlestick(date, opening, closing, highest, lowest):
    delta_open_close = closing - opening
    delta_high_low = highest - lowest

    # 設定漲跌顏色
    color = "red" if delta_open_close > 0 else "green"
    bottom = opening if delta_open_close > 0 else closing

    # 實線（開、收盤價）
    plot.bar(date, abs(delta_open_close), bottom=bottom, width=0.6, color=color)
    # 影線（最高、最低價）
    plot.bar(date, delta_high_low, bottom=lowest, width=0.1, color=color)


with open("STOCK_DAY_2330_202405.csv", encoding="big5") as f:
    title = next(f).replace('"', "")  # 標題

    # 設定中文字型（蘋果儷宋體）
    plot.rc("font", family="Apple LiSung")

    data = csv.DictReader(f, restval=None)

    for row in data:
        if row["成交股數"] is not None:
            date = int(row["日期"].split("/")[-1])
            opening = int(float(row["開盤價"]))
            closing = int(float(row["收盤價"]))
            highest = int(float(row["最高價"]))
            lowest = int(float(row["最低價"]))

            draw_candlestick(date, opening, closing, highest, lowest)

    plot.xlabel(title)
    plot.show()