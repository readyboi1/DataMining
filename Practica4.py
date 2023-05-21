import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')


# Realizar el ANOVA
model = ols('NA_Sales ~ EU_Sales + JP_Sales', data=df).fit()
anova_table = anova_lm(model)

# Interpretar los resultados con el nivel de confianza del 95%
alpha = 0.05
anova_table['Significance'] = anova_table['PR(>F)'].apply(lambda p: 'Significant' if p < alpha else 'Not Significant')

# Imprimir la tabla ANOVA
print(anova_table)