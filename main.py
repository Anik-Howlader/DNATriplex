import tkinter as tk
from tkinter import filedialog


root=tk.Tk()
root.geometry('950x300')
root.title('Sequence Analysis')
root.resizable(False, False)
root.iconbitmap('dna.ico')


def load_fasta():
    file_path=filedialog.askopenfilename(title='Select a Fasta file',filetypes=[('FASTA Files','*.fasta;*.fa')])
    if file_path:
        sequence1 = ''
        with open(file_path,'r') as file:
            for line in file:
                if not line.startswith('>'):
                  sequence1+=line.strip()
    file_path=filedialog.askopenfilename(title='Select a Fasta file',filetypes=[('FASTA Files','*.fasta;*.fa')])
    if file_path:
        sequence2 = ''
        with open(file_path,'r') as file:
            for line in file:
                if not line.startswith('>'):
                  sequence2+=line.strip()
    file_path=filedialog.askopenfilename(title='Select a Fasta file',filetypes=[('FASTA Files','*.fasta;*.fa')])
    if file_path:
        sequence3 = ''
        with open(file_path,'r') as file:
            for line in file:
                if not line.startswith('>'):
                  sequence3+=line.strip()

    codon = input1.get()
    l1 = len(sequence1)
    color = input2.get()
    count1 = 0
    positions1 = []

    input3.insert(1.0,sequence1)
    start_index = 1.0

    while True:
        start_index = input3.search(codon,start_index,stopindex=tk.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len(codon)}c"
        input3.tag_add("highlight",start_index,end_index)
        count1+=1


        start_index=end_index
    input3.tag_configure("highlight",foreground=color)
    codonc1.insert(1.0,str(count1))
    start = 0
    while True:
        start= sequence1.find(codon,start)
        if start == -1:
            break
        positions1.append(start+1)
        start +=1

    sum1 = sum(positions1[i+1]-positions1[i] for i in range(len(positions1)-1))
    codons1.insert(1.0,str(sum1))
    codep1 = ','.join(map(str,positions1))
    codonp1.insert(1.0,codep1)
    sm1.insert(tk.END,'---')




    codon = input1.get()
    l2 = len(sequence2)
    color = input2.get()
    count2 = 0
    positions2 = []

    input4.insert(1.0,sequence2)
    start_index = 1.0

    while True:
        start_index = input4.search(codon,start_index,stopindex=tk.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len(codon)}c"
        input4.tag_add("highlight",start_index,end_index)
        count2+=1
        start_index=end_index

    input4.tag_configure("highlight",foreground=color)
    codonc2.insert(1.0,str(count2))

    start = 0
    while True:
        start= sequence2.find(codon,start)
        if start == -1:
            break
        positions2.append(start+1)
        start +=1


    codep2 = ','.join(map(str,positions2))
    codonp2.insert(1.0,codep2)
    sum2 = sum(positions2[i+1]-positions2[i] for i in range(len(positions2)-1))
    codons2.insert(1.0,str(sum2))

    df = float(abs((count1*sum1)-(count2*sum2))/float(count1*sum1))*100.00
    dfh = round(100.00-df,2)
    if dfh > 80.00:
        sm2.config(fg="green")
    else:
        sm2.config(fg="red")
    s1 = str(dfh)+'%'
    sm2.insert(tk.END,s1)


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
    df = float(abs((count1*sum1)-(count3*sum3))/float(count1*sum1))*100.00
    dfh =  round(100.00-df,2)
    if dfh > 80.00:
        sm3.config(fg="green")
    else:
        sm3.config(fg="red")
    s3 = str(dfh)+'%'
    sm3.insert(tk.END,s3)



browse = tk.Button(root,text="Browse FASTAs",font=("arial",10),relief="raised",width=15,command=load_fasta)
browse.place(relx=0.05,rely=0.25)
label1 = tk.Label(root,text="Enter any Codon",font=("arial bold",10),anchor="center")
label1.place(relx=0.06,rely=0.35)
input1=tk.Entry(root,width=21)
input1.place(relx=0.05,rely=0.45)

label2 = tk.Label(root,text="Color",font=("arial bold",10),anchor="center")
label2.place(relx=0.1,rely=0.55)
input2=tk.Entry(root,width=21)
input2.place(relx=0.05,rely=0.65)

label3 = tk.Label(root,text="Seq1",font=("arial bold",10),anchor="center")
label3.place(relx=0.2,rely=0.25)
input3=tk.Text(root,width=25,height=1)
input3.place(relx=0.25,rely=0.25)

label4 = tk.Label(root,text="Seq2",font=("arial bold",10),anchor="center")
label4.place(relx=0.2,rely=0.45)
input4=tk.Text(root,width=25,height=1)
input4.place(relx=0.25,rely=0.45)

label5 = tk.Label(root,text="Seq3",font=("arial bold",10),anchor="center")
label5.place(relx=0.2,rely=0.65)
input5=tk.Text(root,width=25,height=1)
input5.place(relx=0.25,rely=0.65)

label6 = tk.Label(root,text="Codon\nPositions",font=("arial bold",10),anchor="center")
label6.place(relx=0.5,rely=0.1)
codonp1=tk.Text(root,width=7,height=1)
codonp1.place(relx=0.5,rely=0.25)
codonp2=tk.Text(root,width=7,height=1)
codonp2.place(relx=0.5,rely=0.45)
codonp3=tk.Text(root,width=7,height=1)
codonp3.place(relx=0.5,rely=0.65)

label7 = tk.Label(root,text="Codon\nCount",font=("arial bold",10),anchor="center")
label7.place(relx=0.61,rely=0.1)
codonc1=tk.Text(root,width=7,height=1)
codonc1.place(relx=0.6,rely=0.25)
codonc2=tk.Text(root,width=7,height=1)
codonc2.place(relx=0.6,rely=0.45)
codonc3=tk.Text(root,width=7,height=1)
codonc3.place(relx=0.6,rely=0.65)


label8 = tk.Label(root,text="Sum of\nPositions diff",font=("arial bold",10),anchor="center")
label8.place(relx=0.71,rely=0.1)
codons1=tk.Text(root,width=7,height=1)
codons1.place(relx=0.72,rely=0.25)
codons2=tk.Text(root,width=7,height=1)
codons2.place(relx=0.72,rely=0.45)
codons3=tk.Text(root,width=7,height=1)
codons3.place(relx=0.72,rely=0.65)

label9 = tk.Label(root,text="Codon based\nSeq similarity(%)",font=("arial bold",10),anchor="center")
label9.place(relx=0.815,rely=0.1)
sm1=tk.Text(root,width=7,height=1)
sm1.place(relx=0.84,rely=0.25)
sm2=tk.Text(root,width=7,height=1)
sm2.place(relx=0.84,rely=0.45)
sm3=tk.Text(root,width=7,height=1)
sm3.place(relx=0.84,rely=0.65)

root.mainloop()

