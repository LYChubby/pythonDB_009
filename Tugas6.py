import sqlite3
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

def tambahData():
  Nama = entryInputNama.get()
  Biologi = int(entryInputBiologi.get())
  Fisika = int(entryInputFisika.get())
  Inggris = int(entryInputInggris.get())
  
  if Biologi > Fisika and Biologi > Inggris :
    prediksi = "KEDOKTERAN"
  elif Fisika > Biologi and Fisika > Inggris :
    prediksi = "TEKNIK"
  else :
    prediksi = "BAHASA"
  
  cekLabel = tk.Label(InputFrame, text = f"Prodi Pilihan Kamu Adalah : {prediksi} ")
  cekLabel.pack(padx = 10, pady = 5, fill = "x", expand = True)
  
  conn = sqlite3.connect('SQLite.db')
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS Nilai_Siswa (
                      Nama TEXT,
                      Biologi INTEGER,
                      Fisika INTEGER,
                      Inggris INTEGER,
                      Prediksi TEXT)''')
  cursor.execute("INSERT INTO Nilai_Siswa (Nama, Biologi, Fisika, Inggris, Prediksi) VALUES (?, ?, ?, ?, ?)",
                (Nama, Biologi, Fisika, Inggris, prediksi))
  conn.commit()
  conn.close()


uiApp = tk.Tk()
uiApp.configure(background = 'Black')
uiApp.geometry("500x500")
uiApp.resizable(False, False)
uiApp.title("Aplikasi Prediksi Prodi Pilihan")

InputFrame = tk.Frame(uiApp)
InputFrame.pack(padx = 10, fill = "x", expand = True)

InputLabel = tk.Label(InputFrame, text = "Aplikasi Prediksi Prodi Pilihan")
InputLabel.pack(padx = 10, pady = 5, fill = "x", expand = True)

InputNama = tk.Label(InputFrame, text = "Masukkan Nama")
InputNama.pack(padx = 10, pady = 5, fill = "x", expand = True)

entryInputNama = tk.Entry(InputFrame)
entryInputNama.pack(padx = 10, pady = 5, fill = "x", expand = True)

InputBiologi = tk.Label(InputFrame, text = "Masukkan Nilai Biologi")
InputBiologi.pack(padx = 10, pady = 5, fill = "x", expand = True)

entryInputBiologi = tk.Entry(InputFrame)
entryInputBiologi.pack(padx = 10, pady = 5, fill = "x", expand = True)

InputFisika = tk.Label(InputFrame, text = "Masukkan Nilai Fisika")
InputFisika.pack(padx = 10, pady = 5, fill = "x", expand = True)

entryInputFisika = tk.Entry(InputFrame)
entryInputFisika.pack(padx = 10, pady = 5, fill = "x", expand = True)

InputInggris = tk.Label(InputFrame, text = "Masukkan Nilai B. Inggris")
InputInggris.pack(padx = 10, pady = 5, fill = "x", expand = True)

entryInputInggris = tk.Entry(InputFrame)
entryInputInggris.pack(padx = 10, pady = 5, fill = "x", expand = True)

ButtonSubmit = tk.Button(InputFrame, text = "CEK PRODI PILIHAN", command = tambahData)
ButtonSubmit.pack(padx = 10, pady = 5, fill = "x", expand = True)




uiApp.mainloop()