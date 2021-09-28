import requests
import base64
import csv


def main(email, key, grammar, size):
    grammar_base = base64.encodebytes(grammar.encode())
    url = 'https://fofa.so/api/v1/search/all?email=%s&key=%s&size=%s' \
          '&fields=host,title,ip,port,country_name,city&qbase64=%s' % (email, key, size, grammar_base.decode())
    data = requests.get(url).json()
    try:
        flag = data['results']
        files = open('result.csv', 'w', encoding='utf-8', newline="")
        writer = csv.writer(files)
        writer.writerow(['域名', '标题', 'ip', '端口', '国家', '城市'])
        writer.writerows(data['results'])
        files.close()
        print("写入完毕！")
    except:
        print(data['errmsg'])


if __name__ == '__main__':
    email = 'xxxxxx@qq.com'                       # email
    key = 'xxxxxxxxxxxxxxxx'                      # key

    grammar = 'country="CN"&&port="443"'          # 搜索语法
    size = 100                                    # 条数
    main(email, key, grammar, size)
