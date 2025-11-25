import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('comptagevelo2012.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("Перші 5 рядків датафрейму:")
print(df.head())
print("\n" + "=" * 50 + "\n")

print("Інформація про датафрейм:")
print(df.info())
print("\n" + "=" * 50 + "\n")

print("Статистичний опис датафрейму:")
print(df.describe())
print("\n" + "=" * 50 + "\n")

df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df.iloc[:, 1], dayfirst=True)
df = df.set_index('DateTime')

df = df.drop(columns=['Date', df.columns[1]])

df.columns = ['Rachel_Papineau', 'Berri1', 'Maisonneuve_2', 'Maisonneuve_1',
              'Brébeuf', 'Parc', 'PierDup', 'CSC', 'Pont_Jacques_Cartier']

print("Очищені дані:")
print(df.head())
print("\n" + "=" * 50 + "\n")

print("Перевірка пропущених значень:")
print(df.isnull().sum())
print("\n" + "=" * 50 + "\n")

df_filled = df.fillna(0)

total_cyclists_year = df_filled.sum().sum()
print(f"Загальна кількість велосипедистів за рік на усіх велодоріжках: {total_cyclists_year:,}")
print("\n" + "=" * 50 + "\n")

cyclists_per_lane = df_filled.sum()
print("Загальна кількість велосипедистів за рік на кожній велодоріжці:")
for lane, count in cyclists_per_lane.items():
    print(f"{lane}: {count:,}")
print("\n" + "=" * 50 + "\n")

selected_lanes = ['Berri1', 'Rachel_Papineau', 'Pont_Jacques_Cartier']

df_filled['Month'] = df_filled.index.month

print("Найпопулярніші місяці для обраних велодоріжок:")
month_names = {
    1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень',
    5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
    9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
}

for lane in selected_lanes:
    monthly_totals = df_filled.groupby('Month')[lane].sum()
    most_popular_month = monthly_totals.idxmax()
    most_popular_count = monthly_totals.max()

    print(f"{lane}: {month_names[most_popular_month]} ({most_popular_count:,} велосипедистів)")
print("\n" + "=" * 50 + "\n")

print("Детальна статистика по місяцям:")
for lane in selected_lanes:
    print(f"\n{lane}:")
    monthly_data = df_filled.groupby('Month')[lane].sum()
    for month in range(1, 13):
        count = monthly_data[month]
        print(f"  {month_names[month]}: {count:>6,}")

print("\n" + "=" * 50 + "\n")

berri1_monthly = df_filled.groupby('Month')['Berri1'].sum()

plt.figure(figsize=(12, 6))
months_short = ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер', 'Лип', 'Сер', 'Вер', 'Жов', 'Лис', 'Гру']
plt.bar(months_short, berri1_monthly.values, color='skyblue', alpha=0.7)
plt.plot(months_short, berri1_monthly.values, marker='o', color='darkblue', linewidth=2, markersize=6)

plt.title('Завантаженість велодоріжки Berri1 по місяцям (2012)', fontsize=14, fontweight='bold')
plt.xlabel('Місяць', fontsize=12)
plt.ylabel('Кількість велосипедистів', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

for i, v in enumerate(berri1_monthly.values):
    plt.text(i, v + 1000, f'{v:,}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

print("Топ-3 найзавантаженіших велодоріжок:")
top_3_lanes = cyclists_per_lane.nlargest(3)
for i, (lane, count) in enumerate(top_3_lanes.items(), 1):
    print(f"{i}. {lane}: {count:,}")

print("\n" + "=" * 50 + "\n")

print("Загальна статистика:")
print(f"Всього велодоріжок: {len(df_filled.columns) - 1}")
print(f"Днів спостереження: {len(df_filled)}")
print(f"Середньоденна кількість велосипедистів: {df_filled.sum().sum() / len(df_filled):.0f}")

plt.figure(figsize=(14, 8))
colors = ['blue', 'red', 'green']
for i, lane in enumerate(top_3_lanes.index[:3]):
    monthly_data = df_filled.groupby('Month')[lane].sum()
    plt.plot(months_short, monthly_data.values, marker='o', label=lane,
             linewidth=2, color=colors[i], markersize=6)

plt.title('Порівняння завантаженості трьох найпопулярніших велодоріжок по місяцям (2012)',
          fontsize=14, fontweight='bold')
plt.xlabel('Місяць', fontsize=12)
plt.ylabel('Кількість велосипедистів', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

monthly_total = df_filled.groupby('Month').sum().sum(axis=1)

plt.figure(figsize=(12, 6))
plt.bar(months_short, monthly_total.values, color='lightgreen', alpha=0.7)
plt.plot(months_short, monthly_total.values, marker='o', color='darkgreen', linewidth=2, markersize=6)

plt.title('Загальна завантаженість всіх велодоріжок по місяцям (2012)', fontsize=14, fontweight='bold')
plt.xlabel('Місяць', fontsize=12)
plt.ylabel('Кількість велосипедистів', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

for i, v in enumerate(monthly_total.values):
    plt.text(i, v + 5000, f'{v:,}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()