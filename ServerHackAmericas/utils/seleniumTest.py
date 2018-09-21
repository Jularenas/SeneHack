from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select
import os

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\chromedriver.exe"

# go to Google and click the I'm Feeling Lucky button

def electricistas24Horas ( name, phone , email , desc ) :
    print("Llego a electricistas24Horas")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    driver.get("http://www.electricistas24horasbogota.com/contactenos")
    ## lucky_button = driver.find_element_by_css_selector("[name=btnI]")
    nameField = driver.find_element_by_id("page93_inputsinglevalue1_inputsinglevalue1")
    nameField.clear()
    nameField.send_keys(name)

    phoneField = driver.find_element_by_id("page93_inputsinglevalue2_phone")
    phoneField.clear()
    phoneField.send_keys(phone)

    emailField = driver.find_element_by_id("page93_inputsinglevalue3_email")
    emailField.clear()
    emailField.send_keys(email)

    comentarioField = driver.find_element_by_id("page93_inputsinglevalue4_inputsinglevalue4")
    comentarioField.clear()
    comentarioField.send_keys(desc)

    submit=driver.find_element_by_id("page93_formcontainer1_form")
    print("-------------")
    print("-------------")
    submit.submit()


	#lucky_button.click()
    print(driver.title)
	# capture the screen
    driver.get_screenshot_as_file("captureElectricistas24Horas.png")
    driver.close()
 
def expertoYa(name,phone,email,desc,dir,now,date,time):
    print("Llego a expertoYa")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    print("ENTRE AL METODO")

    driver.get("https://www.expertoya.com")
    print("ENTRE A EXPERTOYA")
    print(driver.title)
	#lucky_button = driver.find_element_by_css_selector("[name=btnI]")
    nameField = driver.find_element_by_id("edit-field-user-name-und-0-value")
    nameField.clear()
    nameField.send_keys(name)

    phoneField = driver.find_element_by_id("edit-field-phone-und-0-value")
    phoneField.clear()
    phoneField.send_keys(phone)

    emailField = driver.find_element_by_id("edit-mail")
    emailField.clear()
    emailField.send_keys(email)

    comentarioField = driver.find_element_by_id("edit-body-und-0-value")
    comentarioField.clear()
    comentarioField.send_keys(desc)

    direccionField= driver.find_element_by_id("edit-title")
    direccionField.send_keys(dir)

    ya = driver.find_element_by_id("edit-field-cuando-und-0")
    #
    programada=driver.find_element_by_id("edit-field-cuando-und-1")
    dateField=driver.find_element_by_id("edit-field-service-date-und-0-value-datepicker-popup-0")
    timeField=driver.find_element_by_id("edit-field-service-date-und-0-value-timepicker-popup-1")
    if now == 1:
        ya.click()
    else:
        programada.click()
        dateField.send_keys(date)
        timeField.send_keys(time)
    terms = driver.find_element_by_id("edit-legal-accept")
    submit = driver.find_element_by_id("edit-submit")

    driver.get_screenshot_as_file("captureExpertoYaSinEnviar.png")

    print("-------------")
    print("-------------")
    terms.click()
    submit.click()
    print(driver.title)
    element2 = driver.find_element_by_id("main-content")
	#element3=element2.find_element_by_id("block-views-user-listing-block-2")
    print (element2.get_attribute('innerHTML'))

	# element2.find_element_by_xpath(".//span[@class='tecnico_ya']").getText()



	#lucky_button.click()
    print(driver.title)
    driver.get_screenshot_as_file("captureExpertoYa.png")

  # def doctorSolucion(name,phone,phone2,email,desc,departamento,ciudad,barrio,):
   # driver.get("http://www.doctorsolucion.co/cita-presupuesto")
   # #lucky_button = driver.find_element_by_css_selector("[name=btnI]")
   # nameField = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtNome_I")
  # nameField.clear()
   # nameField.send_keys(name)

   # emailField = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtEmail_I")
   # emailField.clear()
   # emailField.send_keys(email)

   # phoneField = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtTelefoneCelular_I")
   # phoneField.clear()
   # phoneField.send_keys(phone)

 # phoneField2 = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtTelefone_I")
 # phoneField2.clear()
 # phoneField2.send_keys(phone2)
 
 
 # direccionField = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtEndereco_I")
 # direccionField.clear()
 # direccionField.send_keys()
 
 # selectDepartamento = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboEstado_I")
 # selectDepartamento.clear()
 # selectDepartamento.send_keys(departamento)
 
 
 # #selectCiudad = WebDriverWait(driver, secs).until(find,ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboCidade_I)
 
 # #selectCiudad = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboCidade_I")
 # selectCiudad.clear()
 # selectCiudad.send_keys(ciudad)
 
 # driver.implicitly_wait(30)
 
 # selectBarrio = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboBairro_I")
 # selectBarrio.clear()
 # selectBarrio.send_keys(barrio)
 
 # driver.implicitly_wait(30)
 
 # selectComo = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboMidia_I")
 # selectComo.clear()
 # selectComo.send_keys("Internet")
 
 # driver.implicitly_wait(15)
 
 # selectDonde = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboMidia_I")
 # selectDonde.clear()
 # selectDonde.send_keys("Email")
 
 # driver.implicitly_wait(15)
 
 # descripcionField=driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtMensagem_I")
 # descripcionFieldclear()
 # descripcionField.send_keys(desc)
 
 # driver.implicitly_wait(15)
 
 # submitBtn=driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_btnEnviar")
 # driver.get_screenshot_as_file("capturaDoctorAntesEnvio.png") 
 # submitBtn.click()

 # print("-------------")
 # print("-------------")


 # #lucky_button.click()
 # print(driver.title)
 # # capture the screen
 # driver.get_screenshot_as_file("capturaDoctorDespuesEnvio.png") 
 
 # def find(driver,id):
    # element = driver.find_elements_by_id(id)
    # if element:
        # return element
    # else:
          # return False
#electricistas24Horas("Ricardo","3000000000","t.kavanagh@uniandes.edu.co","Necesito que arrglen a mi perro aaaaaaaaaaaaaaaaaaaaaa xp")
#expertoYa("Jairo","3000000000","jularenas11@gmail.com","necesito un cerrajero ","cll 66#32-21",1,"10 Mayo 2018","20")
#doctorSolucion("Ricardo","3142352865","305717646","jularenas@gmail.com","envio de prueba","Bogotá","Bogotá","BOCHICA")

def sosExpertos(name,phone,email,desc,tipo,ciudad,barrio):
    print("ENTRE AL METODO")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)	
    driver.get("http://sosexpertos.com/formulario.html")
    print("ENTRE A sosExpertos")
    print(driver.title)
    #lucky_button = driver.find_element_by_css_selector("[name=btnI]")
    listField = driver.find_elements_by_id("icon_prefix")
    
	
    nameField =listField[0]
    nameField.clear()
    nameField.send_keys(name)

    phoneFields = driver.find_elements_by_id("icon_telephone")
    phoneField=phoneFields[0]
    phoneField2=phoneFields[1]
    phoneField.send_keys(phone)
    phoneField2.send_keys(phone)
    print(phoneFields)

    emailField = listField[1]
    emailField.clear()
    emailField.send_keys(email)

    comentarioField = driver.find_element_by_id("descripcion")
    comentarioField.clear()
    comentarioField.send_keys(desc)

    ciudadField= driver.find_element_by_id("ciudad")
    ciudadField.send_keys(ciudad)

    barrioField= driver.find_element_by_id("barrio")
    barrioField.send_keys(barrio)

    radio_casa=driver.find_element_by_id("casa")
    radioEdificio=driver.find_element_by_id("edificio")
    radioTienda=driver.find_element_by_id("tienda")

#    if tipo==1:
#        radio_casa.click()
#   elif tipo ==2:
#        wait(driver, 30).until(EC.visibility_of_element_located((By.ID, "edificio"))).click()  # wait for radio-button visibility + click
#    else:
#        radioTienda.click()

    submit = driver.find_element_by_xpath("html/body/div[3]/div[1]/form[1]/div[3]/div[1]/button[1]")
    print(submit.get_property("innerHTML"))
    submit.click()

    driver.get_screenshot_as_file("captureSosExpertos.png")

    print("-------------")
    print("-------------")
    print(driver.title)
    #element2 = driver.find_element_by_id("main-content")
    #element3=element2.find_element_by_id("block-views-user-listing-block-2")
    #print (element2.get_attribute('innerHTML'))

   # element2.find_element_by_xpath(".//span[@class='tecnico_ya']").getText()



    #lucky_button.click()
    print(driver.title)
   # capture the screen
    driver.get_screenshot_as_file("captureSosExpertosAfterSubmit.png")

def aquaFachada(name, phone, email, localidad,desc):
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    driver.get("http://www.lavadoenbogota.com/fachadas-bogota,-d.c..html")
    ## lucky_button = driver.find_element_by_css_selector("[name=btnI]")
    nameField = driver.find_element_by_id("contact_request_requester_name")
    nameField.clear()
    nameField.send_keys(name)
	
    localidadField=driver.find_element_by_id("contact_request_locality")
    localidadField.clear()
    localidadField.send_keys(localidad)

    phoneField = driver.find_element_by_id("contact_request_requester_number")
    phoneField.clear()
    phoneField.send_keys(phone)

    emailField = driver.find_element_by_id("contact_request_requester_email")
    print(emailField)
    emailField.send_keys(email)

    comentarioField = driver.find_elements_by_name("contact_request[requester_description]")
    comentarioField[0].send_keys(desc)

    comentarioField = driver.find_element_by_id("contact_request_requester_privacy")
    comentarioField.click()

    driver.get_screenshot_as_file("aquaFachada1.png")
    submit = driver.find_element_by_name("commit")
    print("-------------")
    print("-------------")
    submit.click()

    # lucky_button.click()
    print(driver.title)
    # capture the screen
    driver.get_screenshot_as_file("aquaFachada2.png")
    driver.close()

def serviradar(name, lastname,phone, email,desc=""):
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    driver.get("http://serviradar.com/bogota/electricistas/")
    ## lucky_button = driver.find_element_by_css_selector("[name=btnI]")
    nameField = driver.find_element_by_id("nombres_input")
    nameField.clear()
    nameField.send_keys(name)

    lastnameField = driver.find_element_by_id("apellidos_input")
    lastnameField.clear()
    lastnameField.send_keys(lastname)

    phoneField = driver.find_element_by_id("telefono_input")
    phoneField.clear()
    phoneField.send_keys(phone)

    emailField = driver.find_element_by_id("email_input")
    print(emailField)
    emailField.send_keys(email)

    driver.get_screenshot_as_file("serviradar1.png")
    submit = driver.find_element_by_xpath("//button")
    print(submit)
    print("-------------")
    print("-------------")
    submit.click()
    driver.implicitly_wait(5)
    # lucky_button.click()
    print(driver.title)
    # capture the screen
    driver.get_screenshot_as_file("serviradar2.png")
    driver.close()

def hogaru(name, email, phone, city,week, horas):
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    driver.get("https://www.hogaru.com/")
    nameField = driver.find_element_by_id("client_lead_name")
    nameField.clear()
    nameField.send_keys(name)

    phoneField = driver.find_element_by_id("client_lead_telephone")
    phoneField.clear()
    phoneField.send_keys(phone)

    emailField = driver.find_element_by_id("client_lead_email")
    print(emailField)
    emailField.send_keys(email)

    citySelector = Select(driver.find_element_by_id("client_lead_city_id"))
    citySwitcher={
        1: "Bogotá",
        2: "Cali",
        3: "Medellin"
    }
    citySelector.select_by_value(citySwitcher.get(city))

    weekSelector = Select(driver.find_element_by_id("client_lead_num_days_interested"))
    weekSwitcher={
        1: "1 Día por semana",
        2: "2 Día por semana",
        3: "3 Día por semana",
        4: "4 Día por semana",
        5: "5 Día por semana",
        6: "6 Día por semana"
    }
    citySelector.select_by_value(weekSwitcher.get(week))

    if horas == 4:
        radio1 = driver.find_element_by_id("client_lead_hours_interested_4")
        radio1.click()
    else:
        radio2 = driver.find_element_by_id("client_lead_hours_interested_8")
        radio2.click()

    driver.get_screenshot_as_file("hogaru.png")
    submit = driver.find_element_by_xpath("new_client_lead")
    print(submit)
    print("-------------")
    print("-------------")
    submit.submit()
    # lucky_button.click()
    print(driver.title)
    # capture the screen
    driver.get_screenshot_as_file("serviradar2.png")
    driver.close()

#hogaru("Rafel", "rafarz333@gmail.com","3194244150",1,3,4 )
#serviradar("Julian", "Arenas", "3124326578","rafarz333@gmail.com")

#sosExpertos("Julian","3142352865","jularenas2@gmail.com","quiero remodelar mi terraza",1,"Bogotá","alqueria")

