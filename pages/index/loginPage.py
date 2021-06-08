'''
    统一登陆界面

'''
from common import basePage
from selenium import webdriver


class LoginPage(basePage.BasePage):

    '''统一登录网址'''
    url="http://10.95.152.140:8080/"

    '''
        系统相关元素
    '''
    #button=('xpath','/html/body/div[10]/div[2]/div[3]/ul/li[1]')
    username=('id',"username")
    userpass=('id','userpass')
    #login_button=('//*[@id="login"]')
    login_button=('id','login')


    '''
        系统相关组件
    '''
    def crm_login(self,username="secadmin",password="111111111a!"):
        '''登陆系统'''
        self.get(self.url)
        #self.click(self.crm_button)
        self.sendKeys(self.username,text=username)
        self.sendKeys(self.userpass,text=password)
        self.click(self.login_button)



if __name__ == '__main__':

    driver=webdriver.Chrome()
    login_page=LoginPage(driver)
    login_page.crm_login()


