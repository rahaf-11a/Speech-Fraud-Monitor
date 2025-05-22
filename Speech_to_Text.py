import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox

def recognize_speech():
    r = sr.Recognizer()
    r.energy_threshold = 100
    r.dynamic_energy_threshold = False
    
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.3)
        label.config(text="قيد الاستماع...")
        root.update()
        
        audio2 = r.listen(source2)

        try:
            text = r.recognize_google(audio2, language="ar-AS")
            text = text[::-1]  
            label.config(text=f"{text[::-1]}")
            root.update()
            
            fraud_keywords = [
                "بطاقه", "كود", "الرقم السري", "تحويل", "رصيد", "حساب", "مبلغ", "بنكي",
                "سرقة", "اختراق", "تصيد", "هاكر", "رمز", "توثيق", "تحديث بيانات",
                "مصرف", "حوالة", "رسوم", "جائزه", "رابح", "مجاني", "شحن", "الدفع",
                "احتيال", "نصب", "خداع", "فوز", "تمويل", "استرجاع", "رصيد مجاني",
                "تحقق", "OTP", "رمز التفعيل", "رسالة تحقق", "كسب", "عروض", "تحذير",
                "اشعار", "استرجاع أموال", "حماية", "دعم فني", "معاملة", "إيقاف حساب",
                "إيداع", "سحب", "كسب المال", "رابط وهمي", "تحديث حسابك", "مدفوعات",
                "إلغاء قفل الحساب", "استرجاع حساب", "عاجل", "مسابقة", "دخول آمن",
                "تأمين الحساب", "كلمة المرور", "إعادة ضبط", "اختراق الحساب", "إرسال بيانات", "ربحت"
            ]
            fraud_keywords = [word[::-1] for word in fraud_keywords]
            
            flag = any(word in text for word in fraud_keywords)
            
            if flag:
                messagebox.showwarning("تنبية احتيال", "انتبه!!! عملية احتيال محتملة")
            else:
                messagebox.showinfo("حالة المكالمة", "مكالمة عادية")
        
        except sr.UnknownValueError:
            label.config(text="عذراً, لم يكن الكلام واضحاً")
        except sr.RequestError:
            label.config(text="لم يصل الطلب الى قوقل")

root = tk.Tk()
root.title("رصد مكالمة الاحتيال")
root.geometry("500x300")

label = tk.Label(root, text="اضغط على الزر لبدء الرصد", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="بدء الرصد", command=recognize_speech, font=("Arial", 12), bg="lightblue")
button.pack(pady=20)

root.mainloop()
