import streamlit as st
import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

st.header("project name")
df=pd.read_csv("clean.csv")


df_urban = df[[ 'Country name', 'Year', 'Aggregation level',
                'Sub-national region name' , 'Number of individual cases in dataset for region' , 
                'Number of households in dataset for region' , '% population in urban areas' 
                ]] 
df_wealth = df[['Country name', 'Year','Mean International Wealth Index (IWI) score of region',
       '% poor households (with IWI value under 70)',
       '% poorer households (with IWI value under 50)',
       '% poorest households (with IWI value under 35)',
       'Gini coefficient wealth inequality', 'Theil-T wealth inequality',
       'Wealth inequality within groups (THeil-T)']]

df_years_edu = df[['Country name', 'Year','Mean years education of adults aged 20+',
       'Mean years education of women aged 20+',
       'Mean years education of men aged 20+',
       'Mean years education of adults aged 25+',
       'Mean years education of women aged 25+',
       'Mean years education of men aged 25+',
       'Mean years education of adults aged 20-39',
       'Mean years education of women aged 20-39', 
       'Mean years education of men aged 20-39',
       'Mean years education of adults aged 40-59',
       'Mean years education of women aged 40-59',
       'Mean years education of men aged 40-59',
       'Mean years education of adults aged 60+',
       'Mean years education of women aged 60+',
       'Mean years education of men aged 60+']]

df_educ = df[['Country name', 'Year',
       'Educational attendance children 6-8',
       'Educational attendance children 9-11',
       'Educational attendance children 12-14',
       'Educational attendance children 15-17',
       'Educational attendance children 18-20',
       'Educational attendance children 21-23',
       'Educational attendance girls 6-8', 
       'Educational attendance girls 9-11',
       'Educational attendance girls 12-14',
       'Educational attendance girls 15-17',
       'Educational attendance girls 18-20',
       'Educational attendance girls 21-23', 
       'Educational attendance boys 6-8',
       'Educational attendance boys 9-11', 
       'Educational attendance boys 12-14',
       'Educational attendance boys 15-17', 
       'Educational attendance boys 18-20', 
       'Educational attendance boys 21-23']]


df_fert = df[['Country name', 'Year','Total Fertility Rate', 'Age-specific fertility rate age 10-14',
       'Age-specific fertility rate age 15-19',
       'Age-specific fertility rate age 20-24',
       'Age-specific fertility rate age 25-29',
       'Age-specific fertility rate age 30-34',  
       'Age-specific fertility rate age 35-39', 
       'Age-specific fertility rate age 40-44',
       'Age-specific fertility rate age 45-49']] 

df_pop = df[['Country name', 'Year','Total area population in millions',
       'Share of population living in area', '% population aged 0-9',
       '% population aged 10-19', '% population aged 20-29',
       '% population aged 30-39', '% population aged 40-49',
       '% population aged 50-59', '% population aged 60-69', 
       '% population aged 70-79', '% population aged 80-89',
       '% population aged 90+', 'Average household size', 'Dependency ratio',
       'Youth dependency ratio', 'Old age dependency ratio',
       'Demographic Window Phase', '% population aged under 15',
       '% population aged 15-65', '% population aged over 65']]

df_mortality = df[['Country name', 'Year','Infant mortality rate', 'Under five mortality rate',
       'Neo-natal mortality rate', 'Post-neonatal mortality rate',
       'Child mortality rate']] 

st.write(df_mortality)
