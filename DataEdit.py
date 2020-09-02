import pandas as pd 
from datetime import datetime, timedelta
from tkinter import messagebox

from GraphPage import GraphPage_

class DataEdit_:
      
    def select_cols_rows(self, start_col, end_col, start_row, end_row):
        """
        :rtype: object
        :param start_col:
        :param end_col:
        :param start_row:
        :param end_row:
        """
        start_col = start_col
        end_col = end_col

        df_info = self.controller.df.iloc[:, :2]
        
        #ovdje cemo pozvati funkciju clear_data() koja ce dio tablice procistiti 
        df_data = self.controller.df.iloc[:, 2:]
        header = []
        len_df = len(df_data.columns)+1
        for i in range(1,len_df):
            header.append(i) 
        df_data.columns = header

        #odabiremo jedinke koje smo unjeli u entryu
        df_data = df_data.loc[:, int(start_col):int(end_col)]

        #postavljamo redne brojeve od 1 na dalje kao oznaku za musicu
        header = []
        len_df = len(df_data.columns)+1
        for i in range(1,len_df):
            header.append(i) 
        #df_data.columns = header
        
        #spajamo sve u jedan dat frame 
        df = pd.concat([df_info, df_data], axis=1, sort=False)
        
        #ovdje vrsimo selekciju redaka
        start_time = datetime.strptime(start_row, '%Y-%m-%d %H:%M')
        end_time = datetime.strptime(end_row, '%Y-%m-%d %H:%M')

        df['datetime'] = pd.to_datetime(df['datetime'])
        mask = (df['datetime'] >= start_time) & (df['datetime'] <= end_time)
        df = df.loc[mask]
        self.controller.df = df.reset_index(drop=True)
        #vrijednosti se brisu zbog druge selekcije nad podatcima
        start_row=None
        end_row=None

        self.on_show_frame(self)
        
    def clear_data(self):
        """
        ova funkcija brise nepotrebne stupce koji nisu jedinke i kreira
        stupac time koji je u formatu dd-mm-yyyy hh:mm:ssss imati na umu 
        da se nakon time stupca dodaju 3 nova stupca gdje se racunaju vrijednosti

        :rtype: object
        """
        df = self.controller.df

        df_info = pd.concat([df.iloc[:, :3], df[[7]]], axis=1, sort=False)
        df_info.columns = ['old_index', 'date', 'time', 'name']

        df_info['datetime'] = df_info.date + ' ' + df_info.time

        df_info['datetime'] = pd.to_datetime(df_info['datetime'])
        # df_info = pd.to_datetime(df_info.stack()).unstack()
        # df_info['datetime'] = df_info['datetime'].dt.strftime('%Y-%m-%d %H:%M')

        df_info = df_info.drop(columns=['old_index', 'date', 'time'])
        df_info = df_info[['datetime', 'name']]
        df_info['datetime'] = df_info['datetime'].dt.strftime('%Y-%m-%d %H:%M')

        df_data = df.iloc[:, 10:]
        df_data.columns = range(1, len(df_data.columns) + 1)

        self.controller.df = pd.concat([df_info, df_data], axis=1, sort=False)
        
    def get_stats(self):
        """"
        ovdje se izracunavaju statisticke vrijednosti koje se pohranjhuju u 
        stupce tablice a to su: average, sum i stdev

        :rtype: object
        """
        df = self.controller.df
        
        df['mean'] = df.iloc[:,2:].mean(axis=1).round(2)
        df['se'] = df.iloc[:,2:].sem(axis=1).round(2)
        df['sum'] = df.iloc[:,2:].sum(axis=1).round(3)

        self.controller.df = df
        self.on_show_frame(self)
    
    def save_to_xlsx(df):
        df.to_excel("results/selected_data.xlsx")

    def save_to_txt(df):
        df.to_csv('results/selcted_data.txt', header=True, sep='\t', float_format='%.3f')

    def save_result_to_xlsx(df):
        df.to_excel("results/individual_result_table.xlsx")

    def save_result_to_txt(df):
        df.to_csv('results/individual_result_table.txt', header=True, index=False, sep='\t', float_format='%.3f')


    def select_col(df, start):
        start_time = datetime.strptime(start, '%H:%M')
        end_time = start_time + timedelta(minutes=30)

        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.loc[df['datetime'].dt.time.between(start_time.time(), end_time.time())]

        df = df.reset_index(drop=True)

        return df


    def d_stats(self):
        """
        """
        df = self.controller.df

        df_C = df[df.name.str.contains('^C')]
        df_C = df_C.groupby(['datetime']).mean()
        df_C = df_C.resample('H').sum().mean(axis=1)

        df_D = df[df.name.str.contains('^D')]
        df_D = df_D.set_index('datetime')

        df_D1 = df_D[df_D.name == 'D1'].drop(['name'], axis=1)
        df_D1 = df_D1.resample('H').mean().mean(axis=1)

        df_D2 = df_D[df_D.name == 'D2'].drop(['name'], axis=1)
        df_D2 = df_D2.resample('H').mean().mean(axis=1)

        df_D3 = df_D[df_D.name == 'D3'].drop(['name'], axis=1)
        df_D3 = df_D3.resample('H').mean().mean(axis=1)

        df_D4 = df_D[df_D.name == 'D4'].drop(['name'], axis=1)
        df_D4 = df_D4.resample('H').mean().mean(axis=1)

        df_all = pd.concat([df_D1, df_D2, df_D3, df_D4], axis=1)
        df_all.columns = ['D1', 'D2', 'D3', 'D4']

        self.controller.df = df_all
        self.on_show_frame(self)

