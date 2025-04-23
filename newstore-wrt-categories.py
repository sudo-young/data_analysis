import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로딩
df = pd.read_excel('국세청_100대_생활업종_신규사업자_현황.xlsx')

# 업종별 월별 신규사업자 수 집계
df_grouped = df.groupby(['업종명', '월'])['신규사업자수'].sum().reset_index()

# 시각화
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_grouped, x='월', y='신규사업자수', hue='업종명')
plt.title('업종별 월별 신규사업자 수')
plt.xlabel('월')
plt.ylabel('신규사업자 수')
plt.legend(title='업종명', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()