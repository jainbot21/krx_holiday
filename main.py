from pandas import DataFrame
import requests
import datetime

def get_krx_holiday(year : str) -> list:
        
    url = 'http://open.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD/01/0110/01100305/mkd01100305_01'
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {'bld': 'MKD/01/0110/01100305/mkd01100305_01', 'name': 'form',
              '_': str(int(datetime.datetime.now().timestamp() * 1000))}
    code = requests.get(url, headers=headers, params=params)
    url = 'http://open.krx.co.kr/contents/OPN/99/OPN99000001.jspx'
    params = {'search_bas_yy': year, 'gridTp': 'KRX', 'code': code.text,
              'pagePath': '%2Fcontents%2FMKD%2F01%2F0110%2F01100305%2FMKD01100305.jsp'}

    resp = requests.post(url, headers=headers, data=params)
    result = resp.json()
    result_key = list(result.keys())[0]
    result_col = list(result[result_key][0].keys())
    df = DataFrame(data=result[result_key], columns=result_col)
    result_list = df.values.tolist()
    return result_list

if __name__ == '__main__':
  print(get_krx_holiday("2022"))
  
  
