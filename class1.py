import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# It's best practice to put the PATH in the code level not in system level.
os.environ['PATH'] += r"C:/selenium-pylibrary"  # a "rstring" ignora os caracteres especiais

driver = webdriver.Chrome()
driver.get(r'C:\Users\Win10\OneDrive\Documentos\Estudos\html-css\desafios\d012.2\quicktest.html')
driver.implicitly_wait(30)  # Espera um tempo antes de retornar erro
# implicitly_wait é + eficaz do que um time.sleep() porque continua tentando enquanto o tempo não acaba
button = driver.find_element_by_id('button')  # Esse métod já está em desuso, atualmente usa-se:

# button = driver.find_element('id', 'button')


button.click()

# As linhas baaixo não capturam o momento em que o download é concluído, para isso, as próximas linhas serão mais eficientes.
#text_progress = driver.find_element_by_class_name('status')
#print(f'{text_progress.text == "Completed"}')

# Neste código, espera-se por 30 segundos a aparição de "Download Complete!"
# Dentro do elemento de classe "status"
a = WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'status'),  # Element filtration
        'Download complete!'  # The expected text
    )
)
print(a) # Retorna True assim que "Download complete!" aparecer

# Caso queira testar a funcionalidade do implicitly_wait(30), apenas libere o código abaixo:
# element = driver.find_element_by_id('ierwi')
# Ao tentar executá-lo (não há elemento com id = 'ierwi'), o programa não irá dar erro na hora, mas
# sim esperar por 30s e, durante esse tempo, procurar pelo HTML o id = 'ierwi', cessado o tempo, retornará erro


# There is tons of options to use EC (Expected Conditions).
# A maioria é particularmente intuitiva, então teste livremente.