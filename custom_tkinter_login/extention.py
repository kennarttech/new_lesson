from tkinter import *
from tk_html_widgets import HTMLLabel


root = Tk()
root.geometry('400x400')



def new_home():
  global root2
  root()
  root2.destroy()



def new_window():
  root2 = Tk()
  root2.geometry('300x300')
  root.destroy()




 




HTML = """
  <body>
    <p style="text-align: center;">
        <b>
          <a href="httyle="color:#%02x%02x%02x; font-size: 21px">forgot password</a>
        </b><button></button>
    </p>
  </body>
  """

html_label = HTMLLabel(root, html=HTML % (0, 0, 0), width=50)
html_label.pack(fill="both", expand=True)
html_label.fit_height()

button = Button(root, text='next', command=new_window)
button.pack()



root.mainloop()






