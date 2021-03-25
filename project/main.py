from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as pysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

mypass = "harsh"
mydatabase="dbs"

con = pysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("LIBRARY -- management         ")
root.geometry("700x523")
root.iconbitmap('library.ico')

#----------------------------------------------------------------------------#

# Adding a background image
background_image =Image.open('lib.jpg')
render = ImageTk.PhotoImage(background_image)
img= Label(root, image = render)
img.place(x=0,y=0)

#creating the frame for heading to place in..
headingFrame1 = Frame(root,bg="limegreen", bd=5)
headingFrame1.place(x=150,y=5,relwidth=0.54,relheight=0.2)

headingLabel = Label(headingFrame1, text="₩ɆⱠ₵Ø₥Ɇ ₮Ø \n Ⱡł฿Ɽ₳ⱤɎ", bg='black', fg='lime', font=('Courier',20))
headingLabel.place(x=1,y=0, relwidth=1, relheight=1)

#creating button for adding book
btn1 = Button(root,text="𝓪𝓭𝓭 𝓫𝓸𝓸𝓴 𝓭𝓮𝓽𝓪𝓲𝓵",bg='black', fg='green', command=addBook)
btn1.place(x=200,y=200, relwidth=0.45,relheight=0.1)

#creating button for deleting book
btn2 = Button(root,text="𝓭𝓮𝓵𝓮𝓽𝓮 𝓫𝓸𝓸𝓴",bg='black', fg='red', command=delete)
btn2.place(x=200,y=250, relwidth=0.45,relheight=0.1)

#creating button for viewing books
btn3 = Button(root,text="𝓿𝓲𝓮𝔀 𝓫𝓸𝓸𝓴 𝓵𝓲𝓼𝓽",bg='black', fg='yellow', command= View)
btn3.place(x=200,y=300, relwidth=0.45,relheight=0.1)

#creating button for viewing issued books
btn4 = Button(root,text="𝓘𝓼𝓼𝓾𝓮 𝓑𝓸𝓸𝓴 𝓽𝓸 𝓢𝓽𝓾𝓭𝓮𝓷𝓽",bg='black', fg='purple', command = issueBook)
btn4.place(x=200,y=350, relwidth=0.45,relheight=0.1)

#creating button for returning book..
btn5 = Button(root,text="𝓡𝓮𝓽𝓾𝓻𝓷 𝓑𝓸𝓸𝓴",bg='black', fg='pink', command = returnBook)
btn5.place(x=200,y=400, relwidth=0.45,relheight=0.1)

#creating button for quit window.. 
btn6 = Button(root, text="𝓠𝓾𝓲𝓽", bg="black", fg="silver",font=('doodls',10) ,command= root.destroy)
btn6.place(x=570, y=475,relwidth=0.20,relheight= 0.1)
root.mainloop()





#-------------------------------------------------------------------------------------------------------#

    
