import pandas as pd
import os

def list_df(path, end_string):
    # file_list 생성
    file_list = os.listdir(path) #listdir은 리스트형태로 원하는데이터를 바꿔주는
    # 확장자가 end_string과 같은 경우의 리스트만 추출
   #case 1
    file_list2 = []
    for i in file_list:
        if i.endswith(end_string):
            file_list2.append(i)
    #case 2
    file_list3 = [i for i in file_list if i.endswith(end_string)]
    print(file_list2 == file_list3)

    # file_list2 의 리스트 항목들을 데이터프레임화하여 하나의 데이터프레임으로 결합
    # 하나의 데이터 프레임으로 결합
    # 비어있는 데이터 프레임 생성

    total_df = pd.DataFrame()

    for i in file_list2:
       if end_string == '.csv':
          df = pd.read_csv(path + i)
       elif end_string == '.json':
          df = pd.read_json(path + i)
       elif end_string == '.xlsx':
          df = pd.read_excel(path + i)
       else:
          return '확장자가 잘못되었습니다'
       #path 는 매개변수, i는 file_list2 항목 값
    total_df = pd.concat([total_df, df], axis=0, ignore_index=True) # 불러온데이터프레임을 total_df 에 단순한 행 결합
    return total_df