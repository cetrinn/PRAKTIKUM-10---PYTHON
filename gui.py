import tkinter as tk

def hitung():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())

    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    text_hasil.delete("1.0", tk.END)
    text_hasil.insert(tk.END, f"Luas Persegi Panjang : {luas}\n")
    text_hasil.insert(tk.END, f"Keliling Persegi Panjang : {keliling}")

window = tk.Tk()
window.title("Program Persegi Panjang")

label_panjang = tk.Label(window, text="Masukan Panjang")
label_panjang.grid(row=0, column=0, padx=10, pady=10)
entry_panjang = tk.Entry(window)
entry_panjang.grid(row=0, column=1, padx=10, pady=10)

label_lebar = tk.Label(window, text="Masukan Lebar")
label_lebar.grid(row=1, column=0, padx=10, pady=10)
entry_lebar = tk.Entry(window)
entry_lebar.grid(row=1, column=1, padx=10, pady=10)

tombol_hitung = tk.Button(window, text="Hitung", command=hitung)
tombol_hitung.grid(row=2, column=0, padx=10, pady=10)

text_hasil = tk.Text(window, height=5, width=40)
text_hasil.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()