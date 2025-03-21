from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter
from tkinter import ttk
modifyno = 2
ip = False
window = tkinter.Tk()
window.title("Falcon's Validator")
window.minsize(width=450,height=450)
window.config(padx=50, pady=50)

def setip():
    ip=True
    print(ip)
def update_credentials():
    global uname
    global pass1
    uname = username.get()
    pass1 = password.get()
    print(uname,pass1)
def fill_values():
    driver.switch_to.default_content()
    iframe = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[5]/div[2]/div[2]/div/iframe")
    driver.switch_to.frame(iframe)
    wbcno = 7
    neutno = 1
    lymno = 2
    eosno = 3
    monono = 4
    basno = 5
    print(ip)
    if(ip==True):
        difno= 9
        hbno= 11
        mcvno = 13
        mchno = 14
        pltno = 18
        rdwno = 16
        textareano = 24
    else:
        hbno = 9
        mcvno = 11
        mchno = 12
        pltno = 14
        rdwno = 17
        difno = 15
        textareano = 22



    for x in range(modifyno-1):
        print(modifyno)
        wbc = valueextractor(wbcno, None)
        hb = valueextractor(hbno, None)
        mcv = valueextractor(mcvno, None)
        mch = valueextractor(mchno, None)
        plt = valueextractor(pltno, None)
        rdw = valueextractor(rdwno, None)
        neut = valueextractor(difno, neutno)
        eos = valueextractor(difno, eosno)
        mono = valueextractor(difno, monono)
        bas = valueextractor(difno, basno)

        print(wbc)
        print(type(wbc))
        Plttext = ""
        Rbctext = ""
        Wbctext = ""
        Neuttext = ""
        if (plt == "Rerun"):
            Plttext = "Rerun"
        elif (plt < 140):
            if (plt < 25):
                Plttext = "Check Sample"
            else:
                Plttext = "Thrombocytopenia"

        elif (plt > 430):
            if (plt > 600):
                Plttext = "Check Sample"
            else:
                Plttext = "Thrombocytosis"
        else:
            Plttext = "Adequate"
        mcvtext = ""
        if (mcv == "Rerun"):
            mcvtext = "Rerun"
        elif (mcv > 103):
            mcvtext = "Macrocytes+"
        elif (mcv < 78):
            mcvtext = "Microcytes"
        else:
            mcvtext = "Normocytic"
        wbctext = ""
        if (wbc == "Rerun"):
            wbctext = "Rerun"
        elif (wbc > 12):
            if (neut>80):
                wbctext = "Neutrophilic Leucocytosis"
            wbctext = "Leucocytosis"
        elif (wbc < 3.5):
            wbctext = "Leucopenia"
        else:
            if(neut > 80):
                wbctext = "Relative neutrophilia"
            wbctext = "Within normal limits"


        if (neut == "Rerun"):
            neuttext = "Check Sample"

        mchtext = ""
        if (mch == "Rerun"):
            mchtext = "Rerun"
        elif (mch > 35):
            mchtext = "hyperchromic"
        elif (mch < 26):
            mchtext = "hypochromic"

        else:
            mchtext = "normochromic"

        if (rdw>16):
            rdwtext = "Anisocytosis "
        else:
            rdwtext = " "

        Totaltext = f"RBC\n{rdwtext}{mcvtext},{mchtext}\nWBC\n{wbctext}\nPlatelet\n{Plttext}"
        print(Totaltext)
        textarea = driver.find_element(By.XPATH, f"/html/body/form/table[{textareano}]/tbody/tr/td[3]/div/textarea")
        print(textareano)
        textarea.send_keys(Totaltext)

        if(ip==True):
            wbcno += 22
            hbno += 22
            mcvno += 22
            mchno += 22
            pltno += 22
            difno += 22
            rdwno += 22
            textareano += 22
        else:
            wbcno += 20
            hbno += 20
            mcvno += 20
            mchno += 20
            pltno += 20
            difno += 20
            rdwno += 20
            textareano += 20


def start_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    global driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://tgehmis.dcservices.in/AHIMSG5/hissso/loginLogin")

    element = driver.find_element(By.ID, "UserName")
    e2 = driver.find_element(By.ID, "pwd")


    print(uname)
    element.send_keys(uname)
    e2.send_keys(pass1)


def show():
    modifyno = clicked.get()
    print(modifyno)
    if (modifyno==1):
        print(modifyno)
        modifyno = 2
    print(type(modifyno))
    print(modifyno)



button1 = tkinter.Button(text="Fill Values", command=fill_values)
button1.grid(row=0, column= 0)
options = [
    1,
    2,3,4,5,6,7,8,9,10
]
clicked = tkinter.IntVar()
clicked.set(1)
drop = tkinter.OptionMenu(window,clicked,*options )
drop.grid(row=1, column=0)
button3= tkinter.Button(text="Confirm patients", command=show)
button3.grid(row=1, column=1)
button2 = tkinter.Button(text="Start Chrome", command=start_chrome)
button2.grid(row=3, column=0)
username = tkinter.ttk.Entry()
username.grid(row=5, column=1)
password = tkinter.ttk.Entry()
password.grid(row=6,column=1)
button4 = tkinter.Button(text="Update", command=update_credentials)
button4.grid(row=7,column=1)
checkbutton = tkinter.Checkbutton(window,text="IP",command=setip)
checkbutton.grid(row=8,column=2)
def valueextractor(num1,num2):
 val1 = ""
 if num2 == None:
    try:
        val1 = driver.find_element(By.XPATH, f"/html/body/form/table[{num1}]/tbody/tr/td[3]/div/div[2]/table[3]/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div/input").get_attribute("value")
    except:

        val1 = driver.find_element(By.XPATH, f"/html/body/form/table[{num1-1}]/tbody/tr/td[3]/div/div[2]/table[3]/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div/input").get_attribute("value")

 else:
    try:
        val1 = driver.find_element(By.XPATH, f"/html/body/form/table[{num1}]/tbody/tr/td[3]/div/div[2]/table[3]/tbody/tr[{num2}]/td[2]/div/table/tbody/tr/td[1]/div/input").get_attribute("value")
    except:

        val1 = driver.find_element(By.XPATH,
                                   f"/html/body/form/table[{num1-1}]/tbody/tr/td[3]/div/div[2]/table[3]/tbody/tr[{num2}]/td[2]/div/table/tbody/tr/td[1]/div/input").get_attribute(
            "value")
 try:
  rval = float(val1)
 except:
     rval = "Rerun"
 return rval









window.mainloop()







