#-*-coding:utf-8-*-
import hmje
import sys
import config
print('훈민정음 프로젝트. 버전: '+config.VERSION)
print(f'개발자 : {config.developer_name}  깃허브: {config.developer_github}')
print('종료하려면 exit, 종료 혹은 control + c 를 입력해 주세요')
while True:
    try:
        text = input(config.shell)
    except KeyboardInterrupt:
        print('\n훈민정음 프로젝트 종료.')
        sys.exit()
    if text == 'exit' or text == '종료':
        print('훈민정음 프로젝트 종료.')
        sys.exit()
    result, error = hmje.run('<표준입력>', text)
    if error:
        print(error.as_string())
        print('훈민정음 프로젝트 종료.')
        sys.exit()
    elif result:
        print(result)
