import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def Ratios(inp):
    bal_sheet= pd.DataFrame()
    driver=webdriver.Chrome(r"path")
    driver.get("https://www.google.com/")
    driver.find_element_by_name('q').send_keys("https://www.moneycontrol.com/financials/"+inp.replace(" ", "")+"/ratiosVI/")
    webelem = driver.find_element(By.XPATH,'//*[@id="tsf"]/div[2]/div/div[3]/center/input[2]')
    webelem.click()
    sym = driver.find_element(By.XPATH, '//*[@id="nChrtPrc"]/div[1]').text
    symbol = []
    i1 = 17
    while sym[i1] != '|':
        symbol.append(sym[i1]);
        i1 = i1 + 1
    sym = ''.join(symbol)

    x=0
    while x<38:
        test=driver.find_element(By.XPATH,'//*[@id="mc_mainWrapper"]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[2]/tbody/tr['+str(x+6)+']').text
        if test == "":
            break
        y=0
        string=driver.find_element(By.XPATH, '//*[@id="mc_mainWrapper"]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[2]/tbody/tr['+str(x+6)+']/td['+str(y+1)+']').text
        if x==11 or x==21 or x==29:
            pass
        else:
            while y<=5:
                bal_sheet.loc[x,y]=driver.find_element(By.XPATH, '//*[@id="mc_mainWrapper"]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[2]/tbody/tr['+str(x+6)+']/td['+str(y+1)+']').text
                y=y+1
        x=x+1
    bal_sheet.set_index(0,inplace=True)
    print(bal_sheet.to_string())
    return sym


