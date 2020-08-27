import hmje
import sys
import config
print('훈민정음 프로젝트. 버전: '+config.VERSION)
print(f'개발자 : {config.developer_name} 깃허브: {config.developer_github}')
while True:
    text = input('> ')
    if text == 'exit':
        print('훈민정음 프로젝트 종료.')
        sys.exit()
    result, error = hmje.run('<stdin>', text)
    if error:
        print(error.as_string())
        sys.exit()
    else:
        print(result)
