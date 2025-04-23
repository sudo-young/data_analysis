import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로딩
df = pd.read_csv('corporate_financial_data.csv')

# 업종별 평균 매출 계산
avg_sales = df.groupby('업종')['매출'].mean().sort_values(ascending=False)

# 시각화
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_sales.index, y=avg_sales.values)
plt.title('업종별 평균 매출')
plt.xlabel('업종')
plt.ylabel('평균 매출')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
