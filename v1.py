from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter
from tkinter import ttk, IntVar
from analyzer import BloodPanelAnalyzer


global ip
global xn1000
xn1000 = False
ip = False
mindray = False

import re


def parse_patient_string(text: str) -> dict:
    """
    Parses a patient demographic string (e.g., '7 D/F') into usable data.
    """
    # Regex pattern breakdown:
    # (\d+)       -> Capture 1 or more digits (the number)
    # \s*         -> Ignore any spaces
    # ([a-zA-Z]+) -> Capture 1 or more letters (the unit: D, min, wk, etc.)
    # \s*/\s*     -> Look for the slash, ignoring spaces around it
    # ([MFmf])    -> Capture the gender (M, m, F, or f)
    pattern = re.compile(r"(\d+)\s*([a-zA-Z]+)\s*/\s*([MFmf])")
    match = pattern.search(text)

    if not match:
        raise ValueError(f"Could not parse the format of: '{text}'")

    value = int(match.group(1))
    unit = match.group(2).lower()  # Convert to lowercase for easy matching
    gender = match.group(3).upper()  # Normalize gender to uppercase

    return {
        "original": text,
        "value": value,
        "unit": unit,
        "gender": gender
    }


def get_age_in_days(parsed_data: dict) -> float:
    """
    Converts the parsed time unit into total days.
    """
    value = parsed_data["value"]
    unit = parsed_data["unit"]

    # Map different unit variations to days
    if unit in ['min', 'mins', 'h', 'hr', 'hours']:
        return 0  # We'll treat anything under a day as 0 days
    elif unit in ['d', 'day', 'days']:
        return value
    elif unit in ['wk', 'wks', 'week', 'weeks']:
        return value * 7
    elif unit in ['m', 'mo', 'month', 'months','mth']:
        return value * 30 # Average days in a month
    elif unit in ['y', 'yr', 'yrs', 'year', 'years']:
        return value * 365  # Account for leap years
    else:
        raise ValueError(f"Unknown time unit: '{unit}'")


def map_to_reference_bucket(days: float) -> str:
    """
    Maps total days to the exact string keys used in the reference dictionary.
    You can adjust these thresholds based on exact medical standards.
    """
    if days < 1:
        return "Birth"
    elif days <= 3:
        return "Day-3"
    elif days <= 7:
        return "Day-7"
    elif days <= 14:
        return "Day-14"
    elif days <= 30:
        return "1 month"
    elif days <= 60:
        return "2 months"
    elif days <= 180:  # Roughly 6 months
        return "3-6 months"
    elif days <= 365:  # 1 year
        return "1 yr"
    elif days <= 2190:  # 6 years (6 * 365)
        return "2-6 yrs"

    elif days <= 4380:
        return "6-12 yrs"
    else:
        return "Adult"




def checkbox():
    #driver.switch_to.default_content()
    check = driver.find_elements(By.NAME, "chkResultValidationPatient")

    for x in check:

        x.click()
window = tkinter.Tk()
window.title("Falcon's Validator")
window.minsize(width=450,height=450)
window.config(padx=50, pady=50)

def setip():
    global ip

    if (checkbuttonvar.get() == 1):
        ip = True
    else:
        ip = False


def XN1000():
    global xn1000
    if (checkbuttonvar1.get() ==1):
        xn1000 = True
    else:
        xn1000 = False
    print(f"xn1000{xn1000}")



def MRAY():
    global mindray
    if (checkbuttonvar2.get() ==1):
        mindray = True
    else:
        mindray = False
    print(f"mindray{mindray}")

def update_credentials():
    global uname
    global pass1
    uname = username.get()
    pass1 = password.get()

def updateir():
    global ir
    ir = irinput.get()



def fill_values():
    driver.switch_to.default_content()
    iframe = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[5]/div[2]/div[2]/div/iframe")
    driver.switch_to.frame(iframe)
    sample = 4

    extendno = 3
    wbcno = 9
    ir = 14
    difno = 10
    hbno = 7
    mcvno = 13
    mchno = 14
    pltno = 8
    # rdwno = 17
    textareano = 16

    neutno = 1
    lymno = 2
    eosno = 3
    monono = 4
    basno = 5
    ageno = 5
    if xn1000 == True:
        #for complete blood picture
        print(f'{xn1000}xn1000')
        sample = 4

        extendno = 3
        wbcno = 9
        ir = 14
        difno = 10
        hbno = 7
        mcvno = 13
        mchno = 14
        pltno = 8
        #rdwno = 17
        textareano = 16

    elif ip == True:
        sample = 4

        extendno = 3
        wbcno = 8
        hbno = 7
        pltno = 9
        ir = 8
        textareano = 10

    else:
        sample = 4

        extendno = 3
        wbcno = 14
        ir = 17
        difno = 15
        hbno = 8
        mcvno = 10
        mchno = 11
        pltno = 16
        # rdwno = 17
        textareano = 19






    for x in range(modifyno):

        extend = driver.find_element(By.XPATH,f"/html/body/form/table[{extendno}]/tbody/tr/td/span/table/tbody/tr/td[2]/div/b/img[1]")
        extend.click()
        age = driver.find_element(By.XPATH, f"/html/body/form/div[{ageno}]/table/tbody/tr[1]/td[2]/div/font").text


        sampleno = driver.find_element(By.XPATH, f"/html/body/form/table[{sample}]/tbody/tr/td[6]/div/font").text

        comment = driver.find_element(By.XPATH,f"/html/body/form/table[{textareano}]/tbody/tr/td[3]/div/textarea")

        ageno+=1
        extendno+=ir
        sample+=ir
        textareano+=ir
        Plttext = ""
        Rbctext = ""
        Wbctext = ""
        Neuttext = ""
        mcvtext = ""
        mchtext = ""
        lymtext = ""


        hb = valueextractor(hbno, None)
        mcv = valueextractor(mcvno, None)
        mch = valueextractor(mchno, None)
        if mindray:
            plt = 100*(valueextractor(pltno, None))
            wbc = (valueextractor(wbcno, None)) / 1000
        else:
            plt = valueextractor(pltno, None)
            wbc = (valueextractor(wbcno, None))
        #rdw = valueextractor(rdwno, None)
        neut = valueextractor(difno, neutno)
        eos = valueextractor(difno, eosno)
        mono = valueextractor(difno, monono)
        bas = valueextractor(difno, basno)
        lym = valueextractor(difno, lymno)


        wbcno += ir
        hbno += ir
        mcvno += ir
        mchno += ir
        difno += ir
        pltno += ir
        try:
            # 1. Parse the text
            parsed = parse_patient_string(age)

            # 2. Convert to days
            days = get_age_in_days(parsed)

            # 3. Map to your dictionary key
            bucket = map_to_reference_bucket(days)

            #parsed_display = f"{parsed['value']} {parsed['unit']}, {parsed['gender']}"
            #print(f"{age:<15} | {parsed_display:<30} | {days:<17.2f} | {bucket}")

        except ValueError as e:
            print(f"Error parsing '{age}': {e}")
        anal = BloodPanelAnalyzer()
        hb,mcv,wbc,plt,mch,neut,lym = [0 if isinstance(v, str) else v for v in [hb,mcv,wbc,plt,mch,neut,lym]]


        patient_data = {
            "Hb": hb,
            "MCV": mcv,
            "WBC": wbc,
            "Platelets": plt ,
            "MCH" : mch,
            "M": wbc*(mono/100),
            "N": wbc*(neut/100),
            "L": wbc*(lym/100),
            "E": wbc*(eos/100),

        }

        full_report = anal.evaluate_panel(age_group=bucket, patient_results=patient_data)

        for item in full_report:
            #print(f"  - {item['index']}: {item['value']} | Status: {item['status']}")
            match item['index']:
                case "Hb":
                    if item['value'] <4:
                        Rbctext = "Check Sample"
                case "MCV":
                    if item['status'] == "Low":
                        mcvtext = "Microcytic"
                    elif item['status'] == "High":
                        mcvtext = "Macrocytic"
                    elif item['status'] == "Normal":
                        mcvtext = "Normocytic"
                    else:
                        mcvtext = " "
                case "N":
                    if item['status'] == "High":
                        Neuttext = "Neutrophilic"
                    else:
                        Neuttext = " "
                case "L":
                    if item['status'] == "High":
                        lymtext = "Lymphocytosis"
                    else:
                        lymtext = " "
                case "WBC":
                    if item['value'] >40:
                        Wbctext = "Check Sample"
                    elif item['status'] == "High":
                        Wbctext = "Leucocytosis"
                    elif item['status'] == "Normal":
                        Wbctext = "WNL"
                    elif item['status'] == "Low":
                        Wbctext = "Leucopenia"
                    else:
                        Wbctext = " "
                case "Platelets":
                    if item['value'] <20 or item['value'] > 800:
                        Plttext = "Check Sample"
                    elif item['status'] == "Low":
                        Plttext = "Thrombocytopenia"
                    elif item['status'] == "High":
                        Plttext = "Thrombocytosis"
                    elif item['status'] == "Normal":
                        Plttext = "Adequate"
                    else:
                        Plttext = " "
                case "MCH":
                    if item['status'] == "Low":
                        mchtext = "Hypochromic"
                    elif item['status'] == "Normal":
                        mchtext = "Normochromic"
                    else:
                        mchtext = " "
                case "E":
                    if item['status'] == "High":
                        Wbctext = "Check Sample - E"

                case "M":
                    if item['status'] == "High":
                        Wbctext = "Check Sample - M"


        if (Plttext == "Thrombocytopenia" and Wbctext == "Leucopenia"):
            print(Rbctext, Wbctext, Plttext)
            T.insert(tkinter.END, f"{sampleno}\n")
        if Rbctext == "Check Sample" or  "Check Sample" in Wbctext or Plttext == "Check Sample" or lymtext == "Lymphocytosis":
            print(Rbctext, Wbctext, Plttext)
            T.insert(tkinter.END, f"{sampleno}{Wbctext}{wbc*(mono/100)}\n")
        else:
            Rbctext = mcvtext+mchtext



        Totaltext = f"RBC-{Rbctext}\nWBC-{Wbctext}\nPlatelet-{Plttext}"
        comment.send_keys(Totaltext)













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


#setting how many samples to fill
def show():
    global modifyno
    modifyno = clicked.get()
    print(modifyno)
    if (modifyno==1):
        print(modifyno)
        modifyno = 2
    print(type(modifyno))
    print(modifyno)

#textbox clear
def clear1():
    T.delete('1.0', tkinter.END)


#user interface
button1 = tkinter.Button(text="Fill Values", command=fill_values)
button1.grid(row=0, column= 0)
options = [
    1,
    2,3,4,5,6,7,8,9,10,15,20
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
checkbuttonvar = IntVar()
checkbutton = tkinter.Checkbutton(window,text="IP",variable=checkbuttonvar,offvalue=0, onvalue=1,command=setip)
checkbutton.grid(row=8,column=2)
checkbuttonvar1 = IntVar()
checkbutton1 = tkinter.Checkbutton(window,text="XN1000",variable=checkbuttonvar1,offvalue=0, onvalue=1,command=XN1000)
checkbutton1.grid(row=8,column=3)

checkbuttonvar2 = IntVar()
checkbutton2 = tkinter.Checkbutton(window,text="MR",variable=checkbuttonvar2,offvalue=0, onvalue=1,command=MRAY)
checkbutton2.grid(row=8,column=4)

allcheck = tkinter.Button(text="Check All", command=checkbox)
allcheck.grid(row=9, column= 2)
T= tkinter.Text(window,height=10, width=100)
T.grid(row=9, column=0)
clear = tkinter.Button(text = "Clear", command=clear1)
clear.grid(row = 9, column = 3)

irinput = tkinter.ttk.Entry()
irinput.grid(row=10, column=1)







def valueextractor(num1,num2):
 val1 = ""
 if num2 == None:
    try:
        val1 = driver.find_element(By.XPATH, f"/html/body/form/table[{num1}]/tbody/tr/td[3]/div/div[2]/table[3]/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div/input").get_attribute("value")
    except:

        #val1 = driver.find_element(By.XPATH, f"/html/body/form/table[{num1-1}]/tbody/tr/td[3]/div/div[2]/table[3]/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div/input").get_attribute("value")
        val1 = "Rerun"

 else:
    try:
        val1 = driver.find_element(By.XPATH, f"/html/body/form/table[{num1}]/tbody/tr/td[3]/div/div[2]/table[3]/tbody/tr[{num2}]/td[2]/div/table/tbody/tr/td[1]/div/input").get_attribute("value")
    except:

        #val1 = driver.find_element(By.XPATH,f"/html/body/form/table[{num1-1}]/tbody/tr/td[3]/div/div[2]/table[3]/tbody/tr[{num2}]/td[2]/div/table/tbody/tr/td[1]/div/input").get_attribute("value")
        val1 = "Rerun"
 try:
  rval = float(val1)
 except:
     rval = "Rerun"
 return rval









window.mainloop()


