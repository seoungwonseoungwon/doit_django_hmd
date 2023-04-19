import os
import django
import csv
import sys

# 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
# django 환경설정 파일 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doit_django_prj.settings")
# django settings 메모리 로딩 적용
django.setup()

# Food 클래스와 연결된 테이블에 data를 ORM으로 업로딩하기 위해 import함
from food_sales.models import Foods

# csv 파일 위치 변수로 정의
CSV_PATH = './datas/food_sales.csv'

with open(CSV_PATH, 'r', encoding='utf-8') as file:
    data_rows = csv.reader(file, skipinitialspace=True)
    # header(첫번째 줄) 제외
    next(data_rows, None)

    # 비어있는 줄 없애기
    data_rows = filter(None, list(data_rows))
    # print(data_rows)

    for row in data_rows:
        # print(row)
        print(row[0])
        if row[0] != None or row[0] != '':
            # 무조건 upload, 중복 데이터 발생가능
            # Foods.objects.create(
                # cook_name=row[0],
                # count=row[1],
                # unit_price=row[2],
            # )

            # 중복 회피, 업로딩
            Foods.objects.update_or_create(
                # filter : 중복을 체크할 값
                # cook_name : Foods 클래스의 속성 => 연결된 테이블의 cook_name 속성
                # cook_name과 하나의 menu_name 값과 비교함, 값이 있는지 없는지 체크하는 역할
                cook_name = row[0],

                # 새로 crate할 value : filter에 의해 중복값이 없을때
                defaults={
                  'cook_name' :row[0],
                  'count' :row[1],
                  'unit_price' :row[2],
                }
            )

    