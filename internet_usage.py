import pandas as pd
import janitor
import plotly.express as px


def get_clean(worldbank_raw,series_code,countries):
    df = worldbank_raw.copy()
    df.columns = [col[:4] if '[' in col else col for col in df.columns]
    df = df.clean_names()
    selected_columns = ['country_name', 'country_code', 'series_name', 'series_code']
    selected_years = [str(year) for year in range(1990, 2024)]
   
    df = df[selected_columns + selected_years]
    country_df = df[df['country_name'].isin(countries)]
    series_df = country_df[country_df['series_code'] == series_code]

    final_df = series_df.drop(columns=['country_code', 'series_name', 'series_code'])
    final_df.set_index('country_name',inplace=True)
    final_df = final_df.T

    final_df = final_df.replace('..', pd.NA)

    for country in final_df.columns:
        final_df[country] = pd.to_numeric(final_df[country], errors='coerce')

    final_df = final_df.ffill()
    final_df.index.name = 'Year'
    return final_df

def compare_countries(df,countries):
    fig = px.line(df, x=df.index, y=countries, title='Percentage of Internet Users by Country (1990-2023)')
    fig.show()

if __name__ == "__main__":
    worldbank_raw = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/internet-usage-analysis/refs/heads/master/data/worldbank-country-internet-data.csv')
    series_code = "IT.NET.USER.ZS"
    countries = ["United States", "China", "India", "Brazil", "Germany"] #  bisa dimodif sesuai dgn negara yg mau dibandingkan
    clean_df = get_clean(worldbank_raw, series_code, countries)
   
    print(clean_df)
    compare_countries(clean_df, countries)