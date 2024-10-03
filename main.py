import tkinter as tk
from tkinter import filedialog, messagebox

root=tk.Tk()
root.geometry('950x300')
root.title('DNATriplex')
root.resizable(False, False)
root.iconbitmap('dna.ico')


def disable_all():
    input3.config(state="disabled")
    input4.config(state="disabled")
    input5.config(state="disabled")
    codonc1.config(state="disabled")
    codonc2.config(state="disabled")
    codonc3.config(state="disabled")
    codonp1.config(state="disabled")
    codonp2.config(state="disabled")
    codonp3.config(state="disabled")
    sm1.config(state="disabled")
    sm2.config(state="disabled")
    sm3.config(state="disabled")
    codons1.config(state="disabled")
    codons2.config(state="disabled")
    codons3.config(state="disabled")


def remove_all_text():
    input3.config(state="normal")
    codonp1.config(state="normal")
    codonc1.config(state="normal")
    codons1.config(state="normal")
    sm1.config(state="normal")

    input4.config(state="normal")
    codonp2.config(state="normal")
    codonc2.config(state="normal")
    codons2.config(state="normal")
    sm2.config(state="normal")

    input5.config(state="normal")
    codonp3.config(state="normal")
    codonc3.config(state="normal")
    codons3.config(state="normal")
    sm3.config(state="normal")

    input3.delete(1.0, tk.END)
    input4.delete(1.0, tk.END)
    input5.delete(1.0, tk.END)
    codonc1.delete(1.0, tk.END)
    codonc2.delete(1.0, tk.END)
    codonc3.delete(1.0, tk.END)
    codonp1.delete(1.0, tk.END)
    codonp2.delete(1.0, tk.END)
    codonp3.delete(1.0, tk.END)
    codons1.delete(1.0, tk.END)
    codons2.delete(1.0, tk.END)
    codons3.delete(1.0, tk.END)
    sm1.delete(1.0, tk.END)
    sm2.delete(1.0, tk.END)
    sm3.delete(1.0, tk.END)


def load_fasta():

    codon = input1.get()
    color = input2.get().lower()
    valid_colors = {'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'black', 'white'}

    if len(codon) != 3 or color not in valid_colors:
        messagebox.showerror("Input Error",
                             "Please enter a valid codon (3 letters) and a valid color (red, blue, green, etc.).")
        return
    remove_all_text()

    file_path=filedialog.askopenfilename(title='Select a Fasta file',filetypes=[('FASTA Files','*.fasta;*.fa')])
    if file_path:
        sequence1 = ''
        with open(file_path,'r') as file:
            for line in file:
                if not line.startswith('>'):
                  sequence1+=line.strip()

    # ----seq1------



    l1 = len(sequence1)
    count1 = 0
    positions1 = []

    input3.insert(1.0, sequence1)
    start_index = 1.0

    while True:
        start_index = input3.search(codon, start_index, stopindex=tk.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len(codon)}c"
        input3.tag_add("highlight", start_index, end_index)
        count1 += 1

        start_index = end_index
    input3.tag_configure("highlight", foreground=color)
    codonc1.insert(1.0, str(count1))
    start = 0
    while True:
        start = sequence1.find(codon, start)
        if start == -1:
            break
        positions1.append(start + 1)
        start += 1

    sum1 = sum(positions1[i + 1] - positions1[i] for i in range(len(positions1) - 1))
    codons1.insert(1.0, str(sum1))
    codep1 = ','.join(map(str, positions1))
    codonp1.insert(1.0, codep1)
    sm1.insert(tk.END, '---')





    file_path=filedialog.askopenfilename(title='Select a Fasta file',filetypes=[('FASTA Files','*.fasta;*.fa')])
    if file_path:
        sequence2 = ''
        with open(file_path,'r') as file:
            for line in file:
                if not line.startswith('>'):
                  sequence2+=line.strip()

    # ---seq2----



    l2 = len(sequence2)
    count2 = 0
    positions2 = []

    input4.insert(1.0, sequence2)
    start_index = 1.0

    while True:
        start_index = input4.search(codon, start_index, stopindex=tk.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len(codon)}c"
        input4.tag_add("highlight", start_index, end_index)
        count2 += 1
        start_index = end_index

    input4.tag_configure("highlight", foreground=color)
    codonc2.insert(1.0, str(count2))

    start = 0
    while True:
        start = sequence2.find(codon, start)
        if start == -1:
            break
        positions2.append(start + 1)
        start += 1

    codep2 = ','.join(map(str, positions2))
    codonp2.insert(1.0, codep2)
    sum2 = sum(positions2[i + 1] - positions2[i] for i in range(len(positions2) - 1))
    codons2.insert(1.0, str(sum2))

    if count1 == 0:
        sm2.insert(tk.END, '0')
    else:
        if sum1 == 0:
            sum1 = 1
        if sum2 == 0:
            sum2 = 1
        df = float(abs((count1 * sum1) - (count2 * sum2)) / float(count1 * sum1)) * 100.00
        dfh = round(100.00 - df, 2)
        if dfh < 0:
            dfh = 0
        if dfh > 80.00:
            sm2.config(fg="green")
        else:
            sm2.config(fg="red")
        s1 = str(dfh) + '%'
        sm2.insert(tk.END, s1)



    file_path=filedialog.askopenfilename(title='Select a Fasta file',filetypes=[('FASTA Files','*.fasta;*.fa')])
    if file_path:
        sequence3 = ''
        with open(file_path,'r') as file:
            for line in file:
                if not line.startswith('>'):
                  sequence3+=line.strip()

    # --- seq3 ------


    codon = input1.get()
    l3 = len(sequence3)
    color = input2.get()
    count3 = 0
    positions3 = []

    input5.insert(1.0,sequence3)
    start_index = 1.0

    while True:
        start_index = input5.search(codon,start_index,stopindex=tk.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len(codon)}c"
        input5.tag_add("highlight",start_index,end_index)
        count3+=1


        start_index=end_index
    input5.tag_configure("highlight",foreground=color)
    codonc3.insert(1.0,str(count3))
    start = 0
    while True:
        start= sequence3.find(codon,start)
        if start == -1:
            break
        positions3.append(start+1)
        start +=1


    codep3 = ','.join(map(str,positions3))
    codonp3.insert(1.0,codep3)
    sum3 = sum(positions3[i+1]-positions3[i] for i in range(len(positions3)-1))
    codons3.insert(1.0,str(sum3))
    if count1 == 0:
        sm3.insert(tk.END, '0')
    else:
        if sum1 == 0:
            sum1 = 1
        if sum3 == 0:
            sum3 = 1
        df = float(abs((count1 * sum1) - (count3 * sum3)) / float(count1 * sum1)) * 100.00
        dfh = round(100.00 - df, 2)
        if dfh < 0:
            dfh = 0
        if dfh > 80.00:
            sm3.config(fg="green")
        else:
            sm3.config(fg="red")
        s2 = str(dfh) + '%'
        sm3.insert(tk.END, s2)
    disable_all()



browse = tk.Button(root,text="Browse FASTAs",font=("arial",10),relief="raised",width=15,command=load_fasta)
browse.place(relx=0.05,rely=0.34)
label1 = tk.Label(root,text="Enter any Codon",font=("arial bold",10),anchor="center")
label1.place(relx=0.06,rely=0.44)
input1=tk.Entry(root,width=21)
input1.place(relx=0.05,rely=0.54)

label2 = tk.Label(root,text="Color",font=("arial bold",10),anchor="center")
label2.place(relx=0.1,rely=0.64)
input2=tk.Entry(root,width=21)
input2.place(relx=0.05,rely=0.74)

label3 = tk.Label(root,text="Seq1",font=("arial bold",10),anchor="center")
label3.place(relx=0.2,rely=0.34)
input3=tk.Text(root,width=25,height=1)
input3.place(relx=0.25,rely=0.34)

label4 = tk.Label(root,text="Seq2",font=("arial bold",10),anchor="center")
label4.place(relx=0.2,rely=0.54)
input4=tk.Text(root,width=25,height=1)
input4.place(relx=0.25,rely=0.54)

label5 = tk.Label(root,text="Seq3",font=("arial bold",10),anchor="center")
label5.place(relx=0.2,rely=0.74)
input5=tk.Text(root,width=25,height=1)
input5.place(relx=0.25,rely=0.74)

label6 = tk.Label(root,text="Codon\nPositions",font=("arial bold",10),anchor="center")
label6.place(relx=0.5,rely=0.19)
codonp1=tk.Text(root,width=7,height=1)
codonp1.place(relx=0.5,rely=0.34)
codonp2=tk.Text(root,width=7,height=1)
codonp2.place(relx=0.5,rely=0.54)
codonp3=tk.Text(root,width=7,height=1)
codonp3.place(relx=0.5,rely=0.74)

label7 = tk.Label(root,text="Codon\nCount",font=("arial bold",10),anchor="center")
label7.place(relx=0.61,rely=0.19)
codonc1=tk.Text(root,width=7,height=1)
codonc1.place(relx=0.6,rely=0.34)
codonc2=tk.Text(root,width=7,height=1)
codonc2.place(relx=0.6,rely=0.54)
codonc3=tk.Text(root,width=7,height=1)
codonc3.place(relx=0.6,rely=0.74)


label8 = tk.Label(root,text="Sum of\nPositions diff",font=("arial bold",10),anchor="center")
label8.place(relx=0.71,rely=0.19)
codons1=tk.Text(root,width=7,height=1)
codons1.place(relx=0.72,rely=0.34)
codons2=tk.Text(root,width=7,height=1)
codons2.place(relx=0.72,rely=0.54)
codons3=tk.Text(root,width=7,height=1)
codons3.place(relx=0.72,rely=0.74)

label9 = tk.Label(root,text="Codon based\nSeq similarity(%)",font=("arial bold",10),anchor="center")
label9.place(relx=0.815,rely=0.19)
sm1=tk.Text(root,width=7,height=1)
sm1.place(relx=0.84,rely=0.34)
sm2=tk.Text(root,width=7,height=1)
sm2.place(relx=0.84,rely=0.54)
sm3=tk.Text(root,width=7,height=1)
sm3.place(relx=0.84,rely=0.74)

disable_all()


header_label = tk.Label(root,fg="#EEEEEE", text="Codon Position-based Sequence Similarity Identification Tool",font=("Tahoma bold",15), bg="#201E43")
header_label.place(relwidth=1, rely=0.0,relheight=.15)
header_label.config(anchor='center')


footer_label = tk.Label(root,fg="#F5F5F7", text="Support: anik.bioinfo@example.com  Version 1.0  October 2024  © 2024", bg="#201E43")
footer_label.place(relwidth=1, rely=0.9,relheight=.1)
footer_label.config(anchor='center')
# bojk ipxmbefs
root.mainloop()

