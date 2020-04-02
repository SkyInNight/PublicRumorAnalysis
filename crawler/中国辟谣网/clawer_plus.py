import requests,json,urllib,os,time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class PiYaoSpiderInterface:
    def get_url(self):
        '''
        获取中国辟谣网站首页a标签中的网址和标签
        返回文章内容的标题和url用字典封装返回
        '''

    def get_article(self, article_url, article_title):
        '''
        获取中国辟谣网页文章的内容
        返回文章html文本内容
        '''
class PiYaoSpider(PiYaoSpiderInterface):
    def __init__(self,url="http://da.wa.news.cn/nodeart/page"):
        ua = UserAgent()
        self.__headers = {
                    'User-Agent':ua.chrome,
                    'Accept':"application/json, text/plain, */*",
                    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Accept-Encoding":"gzip, deflate, br",
                    "X-Requested-With":"XMLHttpRequest"
        }
        self.__url = url

    def get_url(self):
        article_directory = {}
        nid_list = [11158863,11158864,11158865,11158866,11158867]
        for i in range(11158879,11158915+1):
            nid_list.append(i)
        for i in nid_list:
            try:
                print("当前nid为："+str(i))
                data = {'nid':i}
                response = requests.get(self.__url,headers=self.__headers,params=data)
                content = response.content.decode('utf-8')
                message = json.loads(content)
                totalnum = message['totalnum']
                data = {'nid':i,'cnt':totalnum}
                response = requests.get(self.__url,headers=self.__headers,params=data)
                data_content = response.content.decode('utf-8')
                article_list = json.loads(data_content)['data']['list']
                for article in article_list:
                    article_directory[article['LinkUrl']] = article['Title']
                    print("获取页面内容为："+article['Title']+"\nURL为"+article['LinkUrl'])
                    self.get_article(article['LinkUrl'],article['Title'])
            except Exception as e:
                print(e)
        with open("out.txt",'w+',encoding='utf-8') as output_file:
            output_file.write(json.dumps(article_directory))

    def get_article(self,article_url,article_title):
        response = requests.get(article_url,headers=self.__headers)
        content = response.content.decode('utf-8')
        soup = BeautifulSoup(content,'lxml')
        article_content = soup.select("div[class='con_txt']")
        if not os.path.exists('./article'):
            os.mkdir('./article')
        with open('./article/'+article_title.replace("？","").replace('?','').replace(':','').replace('！',"").replace("|","").replace("\"","").replace(r"/","").replace(r"\"","")+'.html','w+',encoding='utf-8') as output_file:
            output_file.write(str(article_content))

if __name__ == '__main__':
    piyaospider = PiYaoSpider()
    piyaospider.get_url()
    
