import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r'C:/selenium-pylibrary'
driver = webdriver.Chrome()
driver.get(r'file:///C:/Users/Win10/OneDrive/Documentos/Estudos/javascript/exercicios/ex03-archives/ex03.html')

driver.implicitly_wait(5)

start = driver.find_element('id', 'first')
start.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)  # apenas para mostrar que posso mandar vários inputs de uma só vez.
end = driver.find_element('id', 'end')
end.send_keys(Keys.NUMPAD2, Keys.NUMPAD0)
step = driver.find_element('id', 'step')
step.send_keys(Keys.NUMPAD1)
# Preciso verificar o código abaixo (feito, explicação está abaixo).

verify = driver.find_element_by_css_selector('#button[onclick="contador()"]')  # Seletor CSS. Outra maneira de filtrar por um elemento.
verify.click()

# O código foi corrigido ao trocar "button" (que procura pelos inputs do tipo button e usa o primeiro a ser encontrado)
# por "#button", mas específico, o qual irá direto para o elemento de id="#button", no caso, o button que eu procuro.
# É útil usar o css selector. Não para o caso de id, como #button, haja vista que a ID é única no HTML,
# mas sim para o caso de elementos que não tenham uma id e sim, por exemplo, uma classe. Como a classe pode abarcar
# mais de um elemento, podemos usar o css_selector para dizer que, naquela classe, o nosso código deverá pegar o primeiro elemento
# HTML que possua uma função onclick "contador()", o que reduz as chances de erro.

# Para aprender mais sobre quais objetos podem ser aplicados ao css_selector, você pode visitar a w3schools na seção
# CSS Selector Reference.
# Por exemplo, lá você descobre que usando "*" você seleciona a todos os elementos.
# Pode ser útil, pois você pode procurar por todos elementos aquele que tenha uma função específica, por exemplo.
# Com .class1.class2, você seleciona duas classes de uma única vez. E por aí vaí.
# Adendo, outro caso bem interessante:
# Com [attribute$=value] + a[href=^"https", você procura por todos os <a> cujo href se inicia com
# https
