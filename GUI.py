from tkinter import*
from PIL import Image, ImageTk
import action
import speech_to_text
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#6F8FAF")

# ask fun

def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val= action.Action(user_val)
    text.insert(END,'User--->'+user_val+"\n")
    if bot_val !=None:
        text.insert(END,"BOT <---"+str(bot_val)+"\n")
    if bot_val =="ok sir":
        root.distroy()

    

def send():
    send =  entry.get()
    bot =action.Action(send)
    text.insert(END,'User--->'+send+"\n")
    if bot !=None:
        text.insert(END,"BOT <---"+str(bot)+"\n")
    if bot =="ok sir":
        root.distroy()
    


def delete():
    text.delete('1.0',"end")
  

#frame
frame = LabelFrame(root, padx=100, pady=7,borderwidth=3,relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=1,padx=55,pady=10)

#text Label

Text_label = Label(frame, text="AI Assistant" , font=("comic Sans ms",14,"bold"), bg="#356696")
Text_label.grid(row=0,column=0,padx=20,pady=10)


Display_Image = ImageTk.PhotoImage(Image.open("D:/AI Desktop/myphoto.png"))
Image_Lable = Label(frame, image= Display_Image)
Image_Lable.grid(row = 1 ,  column=0 , pady=20)



# Add a text widget

text=Text(root , font= ('Courier 10 bold') , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100) 

#entry widgt

entry = Entry(root, justify=CENTER)
entry.place(x=100,y=500,width=350,height=30)


#buttom

Button1 = Button(root, text="ASK", bg="#356696", pady=16 , padx=40, borderwidth=3, relief=SOLID,command=ask)
Button1.place(x=70, y=575)

Button2 = Button(root, text="Send", bg="#356696", pady=16 , padx=40, borderwidth=3, relief=SOLID,command=send)
Button2.place(x=400, y=575)

Button3 = Button(root, text="Delete", bg="#356696", pady=16 , padx=40, borderwidth=3, relief=SOLID,command=delete)
Button3.place(x=225, y=575)









root.mainloop()
