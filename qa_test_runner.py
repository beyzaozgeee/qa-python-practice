# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def username_test(username):
    username = username.strip() 
    if username == "":
        return "FAIL"
    if len(username) < 5:
        return "FAIL - En az 5 karakter olmalı"
    return      "PASS"


    
def password_test(password):
    if len(password) < 8:
        return "FAIL En az 8 karakter olmalı"
    if not any(c.islower() for c in password):
        return "FAIL Küçük harf giriniz"
    if not any(c.isupper() for c in password):
        return "FAIL Büyük harf giriniz"
    if not any(c.isdigit() for c in password):
        return "FAIL Bir rakam giriniz"
    return "PASS Şifre Başarılı"

def email_test(email):
    if "@" not in email or "." not in email :
        return "FAIL"
    return "PASS"


def run_all_tests(username, password, email):
    print("\n--- TEST SONUCLARI ---")
    print("Username Test:" , username_test(username))
    print("Password Test:" , password_test(password))
    print("Email Test :" , email_test(email)) 
    
    
    
username = input("Username gir: ")
password = input("Password gir: ")
email = input("Email gir: ")

run_all_tests(username, password, email)