#pip install selenium
#pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

seu_email=""
sua_senha=""

#O link que nosso codigo vai acessar
driver.get("https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession")
# O Campo que ele vai procurar para digitar o email
driver.find_element_by_name("identifier").send_keys(seu_email)
# O btn que ele vai clicar
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
# O tempo que ele vai esparar
driver.implicitly_wait(5)
# O Campo que ele vai procurar para digitar a senha
driver.find_element_by_name("password").send_keys(sua_senha)
# O btn de proximo
driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()