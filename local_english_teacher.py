import requests
import pandas as pd
from lxml import etree


class Job910(object):
    def __init__(self, max_page, com_type):
        # 外语培训爬取
        # self.start_urls = ['http://www.job910.com/search.aspx?funtype={}&keyword=英语老师&pageSize=20&'
        #                    'pageIndex={}'.format(com_type, i) for i in range(73, max_page+1)]
        # 小学
        # self.start_urls = ['http://www.job910.com/search.aspx?funtype={}&keyword=英语老师&jobType=1020&'
        #                    'pageIndex={}'.format(com_type, i) for i in range(86, max_page + 1)]
        # 幼儿
        # self.start_urls = ['http://www.job910.com/search.aspx?funtype={}&keyword=英语老师&jobType=1010&'
        #                    'pageIndex={}'.format(com_type, i) for i in range(1, max_page + 1)]
        # 初中
        # self.start_urls = ['http://www.job910.com/search.aspx?funtype={}&keyword=英语老师&jobType=1030&'
        #                    'pageIndex={}'.format(com_type, i) for i in range(98, max_page + 1)]
        # 初中
        # self.start_urls = ['http://www.job910.com/search.aspx?funtype={}&keyword=英语老师&jobType=1040&'
        #                    'pageIndex={}'.format(com_type, i) for i in range(89, max_page + 1)]
        #职业院校
        self.start_urls = ['http://www.job910.com/search.aspx?funtype={}&keyword=英语老师&jobType=15&'
                           'pageIndex={}'.format(com_type, i) for i in range(1, max_page + 1)]

    def get_data(self):
        for url in self.start_urls:
            res = requests.get(url)
            page = url.split('=')[-1]
            self.parse_data(res, page)
            print('成功爬取并保存第{}页数据!'.format(page))

    @staticmethod
    def parse_data(res, page):
        if res.status_code == 200:
            # print(res.text)
            parsed = etree.HTML(res.text)


            title = parsed.xpath('//*[@class="content-left-1-left"]/a/text()')
            print(title)
            link = parsed.xpath('//*[@class="content-left-1-left"]/a/@href')
            print(link)
            salary = parsed.xpath('//*[@class="content-left-2-left"]/li/p/text()')
            print(salary)
            company = parsed.xpath('//*[@class="content-left-1-right"]/a/text()')
            print(company)
            area = parsed.xpath('//*[@class="content-left-2-left"]//li[2]//text()')
            print(area)
            update_time1 = parsed.xpath('//*[@class="content-left-1-left"]/p//text()[2]')


            # print(update_time1[0])

            def get_first_digit_index(string):
                for i, char in enumerate(string):
                    if char.isdigit():
                        return i
                return -1  # 如果字符串中没有数字，返回 -1 或其他你认为合适的值
            # print(get_first_digit_index(update_time1[0]))
            update_time = []
            for j in range(len(update_time1)):
                s1 = ''
                for i in range(get_first_digit_index(update_time1[j]), len(update_time1[j]), 1):
                    if (update_time1[j][i] != '\n'):
                        s1 = s1 + update_time1[j][i]
                    else:
                        break
                update_time.append(s1)
                # print(s1)
            print(update_time)

            exp_title = []
            exp_title1 = parsed.xpath('//*[@class="content-left-2-left"]//li[3]//text()')
            # try:
            #     exp_title1 = parsed.xpath('//*[@class="content-left-2-left"]//li[3]//text()')
            # except(ValueError):
            #     pass

            exp_title2 = parsed.xpath('//*[@class="content-left-2-left"]//li[4]//text()')

            for index in range(len(exp_title1)):
                s2 = ''
                s2 = exp_title1[index]+'/' + exp_title2[index]
                exp_title.append(s2)
            # print(exp_title)

            data = pd.DataFrame({'title': title, 'link': link, 'salary': salary,
                                 'company': company, 'area': area, 'update_time': update_time,
                                 'exp_title': exp_title})
            if page == '1':
                data.to_csv('外语培训.csv', index=False, mode='a', header=True)
            else:
                data.to_csv('外语培训.csv', index=False, mode='a', header=False)
            # if page == '1':
            #     data.to_csv('小学.csv', index=False, mode='a', header=True)
            # else:
            #     data.to_csv('小学.csv', index=False, mode='a', header=False)
            # if page == '1':
            #     data.to_csv('幼儿园.csv', index=False, mode='a', header=True)
            # else:
            #     data.to_csv('幼儿园.csv', index=False, mode='a', header=False)
            # if page == '1':
            #     data.to_csv('初中.csv', index=False, mode='a', header=True)
            # else:
            #     data.to_csv('初中.csv', index=False, mode='a', header=False)
            # if page == '1':
            #     data.to_csv('高中.csv', index=False, mode='a', header=True)
            # else:
            #     data.to_csv('高中.csv', index=False, mode='a', header=False)
            if page == '1':
                data.to_csv('职业院校.csv', index=False, mode='a', header=True)
            else:
                data.to_csv('职业院校.csv', index=False, mode='a', header=False)

        else:
            print('链接{}请求不成功!'.format(res.url))


if __name__ == '__main__':
    job = Job910(22, 19)
    job.get_data()
"""
preschool: 207
certified: 547
ESL:561


"""