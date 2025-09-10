#https://www.google.com/search?q=weather+patna&sca_esv=0cc5f8e8113380e9&sxsrf=ADLYWIKErziE0eLeVMTK-cRxiCqWxk6D9A%3A1737466418147&source=hp&ei=MqKPZ_P4Btmnvr0PyeDI6Q8&iflsig=AL9hbdgAAAAAZ4-wQjyShsAPOefaw1XXiTGxON1bKD_Z&oq=weather+patna&gs_lp=Egdnd3Mtd2l6Ig13ZWF0aGVyIHBhdG5hKgIIADINEAAYgAQYywEYRhiAAjIIEAAYgAQYywEyCBAAGIAEGMsBMgUQABiABDIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMg0QABiABBgCGMsBGJ8BSOBwUNAIWOxgcAN4AJABAJgBwQSgAf8bqgEKMC4yLjEyLjUtMbgBAcgBAPgBAZgCEqACsRyoAgrCAgcQIxgnGOoCwgIKECMYgAQYJxiKBcICDBAjGIAEGBMYJxiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgoQABiABBhDGIoFwgIOEAAYgAQYsQMYgwEYxwXCAggQABiABBjHBcICCxAAGIAEGLEDGMcFwgIUEC4YgAQYsQMY0QMYgwEYxwUYxwHCAhIQIxiABBgnGIoFGJ0CGEYYgALCAg8QIxixAhgnGJ0CGEYYgALCAgcQIxixAhgnwgIKEAAYgAQYChjLAcICChAAGIAEGMcFGArCAgsQABiABBiRAhiKBcICDRAAGIAEGLEDGEMYigXCAggQABiABBixA5gDBvEFDZdU98Kq_K-SBwozLjEuMTMuMC4xoAe7Xw&sclient=gws-wiz
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36
# my user agent is : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
# print(r.html.find('title' , first= True).text) 
# requests-html==0.10.0
# lxml==4.9.1 (first install  this one)

from requests_html import HTMLSession
import speech_to_text

def Weather():
    s  =  HTMLSession()
    query = "patna"
    url = f'https://www.google.com/search?q=weather+patna&sca_esv=0cc5f8e8113380e9&sxsrf=ADLYWILrVWmagkSIkSsZfwbakDqsjhiz0g%3A1737466657803&ei=IaOPZ7a9MKGc4-EPiJjVMA&oq=&gs_lp=Egxnd3Mtd2l6LXNlcnAiACoCCAEyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gJInRxQkgNY2QtwAngBkAEEmAH9A6AByguqAQswLjEuMi4xLjAuMbgBAcgBAPgBAZgCA6AC-QKoAgrCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAAGIAEGEMYigXCAgUQABiABMICBRAAGO8FwgIIEAAYgAQYogSYAwTxBdOfqvJD8ADsiAYBkAYKkgcFMi4zLTGgB7sm&sclient=gws-wiz-serp+{query}'
    r  = s.get(url , headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})

    temp  = r.html.find('span#wob_tm' , first= True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
    desc  = r.html.find('span#wob_dc' , first= True).text
    return temp+" "+unit+" "+desc