#!/usr/bin/python3
import os
import re
import time
import sys
import subprocess
import pandas as pd
import linecache
#os.mkdir("pepstats") 
#os.mkdir("profa")
#os.mkdir("raw_protein_sequence")
#os.mkdir("conservation")
#os.mkdir("motifone")
#os.mkdir("motiftwo")
#os.mkdir("motif3")

#subprocess.call("clear")
#text='Introduction of the program'
#print (text.center(110))
#time.sleep(2.5)
#print("\033[1;35;40m1. Specify the protein famlily and the taxonomic group\n2. Obtain the relevant protein sequence data\n3.Plot the level of the conservation between the protein sequence\n4. Scan the protein sequence of interests with motifs from the PROSITE database\n5.Do the appropriate EMBOSS analysis.\033[0m")


#time.sleep(2.5)

#To get the initial sequence with answer-question method
def answer(question):
    answer=input(question)
    while answer != "yes" and answer != "no":
          print("Error,please try again with the 'yes' and 'no' !")
          answer=input(question)
    return answer


#Ask the user if they want to start the program
#answer1=answer("Start now?(yes/no)")
#time.sleep(1)
#if answer1 == "yes":
#   print("Thank you, let's begin")
#else:
#   sys.exit(1)

#Search the protein and extract the information for the user to decide
#def search():
#    toxonomic=input("Enter the toxonomic groups:")
#    protein_family_name=input("Enter the protein family:")
#    print("Please choose:\n1._None_\n2.Not Partial\n3.Not Predicted\n4.Not Partial,Not Predicted")
#    options=["","NOT PARTIAL","NOT PREDICTED","NOT PARTIAL NOT PREDICTED"]
#    youroption=int(input("Choose with the number 1 to 4:"))
#    myfile="./raw_protein_sequence/species"
#    print("If you find the screen have not changes, do not panic ,you may have to wait for a while!")
#    subprocess.call("esearch -db protein -query \"%s[organism] AND %s %s\" | efetch -format gpc | xtract -pattern INSDSeq -element INSDSeq_accession-version INSDSeq_organism> ./raw_protein_sequence/species" %(toxonomic,protein_family_name,options[youroption-1]), shell=True)
#    filesize=os.path.getsize(myfile)
#    return filesize 

#fsize=search()     
#while fsize==0:
#      print("Error!Please try again.")
#      fsize=search()      

#species=pd.read_csv('./raw_protein_sequence/species',sep='\t',header=None)
#speciename=species.iloc[:,1]
#ids=list(species.iloc[:,0])
#eliminate rundant element
#sp=set(speciename)
#flist=speciename.value_counts()
#print('Now, there are'+str(len(ids))+'sequences in '+ str(len(ids))+'different species')
#print(flist)

#answer2=answer("Do you want to continue to analysis all of the species?(yes/no)")
#if answer2=="yes":
#   for sequence in ids:
#       subprocess.call("esearch -db protein -query %s|efetch -db protein -format fasta >>./raw_protein_sequence/sequence.fasta"%(sequence),shell=True)
#else:
#   print("There are the name of the species below, you can chooses the specie you do not want to analysis",sp)
#   deletename=input("Enter one of the name you want to give up.(enter \"stop\" to stop the delete step):").strip()
#   while deletename !="stop":
#         with open("./raw_protein_sequence/species","r") as r:
#              lines=r.readlines()
#         with open("./raw_protein_sequence/species","w") as w:
#              for l in lines:
#                  if deletename not in l:
#                     w.write(l)
#         species=pd.read_csv('./raw_protein_sequence/species',sep='\t',header=None)
#         speciename=species.iloc[:,1]
#         ids=list(species.iloc[:,0])
#         sp=set(speciename)
#         print("There are",len(ids),"sequences and",len(sp),"species")
#         deletename=input("Enter A species to delete(enter \"stop\" to stop the delete step):")
#         if deletename =="stop": 
#           print("Please wait for a while, downloading..")
#            for sequence in ids:
#                subprocess.call("esearch -db protein -query %s|efetch -db protein -format fasta >>./raw_protein_sequence/sequence.fasta"%(sequence),shell=True)
 
#if len(speciename)>1000:
#   answer4=("The sequence is more than 1000, do you want to continue the analysis?(yes/no)")
#   if answer4 == "no":
#      sys.exit(1)  



#def conservation250():
#select=[]
   #multiple sequence alignment
#    subprocess.call("clustalo -i ./raw_protein_sequence/sequence.fasta --guidetree-out=GT.gt --full --force --threads=10 -o ./conservation/Multiple.fasta", shell=True)
#    subprocess.call("cons ./conservation/Multiple.fasta ./conservation/protein.cons",shell=True)
#    subprocess.call("makeblastdb -in ./raw_protein_sequence/sequence.fasta -dbtype prot -out proteindb", shell=True)
#    subprocess.call("blastp -db proteindb -query ./conservation/protein.cons  -outfmt 0 > ./conservation/blast1.txt", shell=True)
 #extract the first 250 sequences based on e-value and bit score
#    with open("./conservation/blast1.txt","r") as inputfile:
#         a=inputfile.readlines()

#    with open("./conservation/blast1.txt","w") as inputfile:
#         b=''.join(a[29:279])
#         inputfile.write(b)
#    with open("./conservation/blast1.txt","r") as alignfile:
#    lines=alignfile.readlines()
#    for l in lines:
#         chooseid=l.split()
#         select.append(chooseid[0])

#    with open("./conservation/selectid.txt","w") as input:
#     for sequence in select:
#         input.write(sequence+'\n')        
#    subprocess.call("/localdisk/data/BPSM/Assignment2/pullseq  -i  ./raw_protein_sequence/sequence.fasta  -n  ./conservation/selectid.txt  >>./conservation/select_protein.fasta",shell = True)

#conservation250()

#answer5=answer("Do you want to draw a map of protein conservation?(yes/no)")
#if answer5 == "yes":
#   subprocess.call("plotcon -sequences ./conservation/select_protein.fasta -graph svg -winsize 2 -goutfile ./conservation/graph",shell=True)
#else:
#    sys.exit(1)

#def show():
#    answer6=answer("Do you want to show the graph on the screen?(yes/no)")
#    while answer6 == "yes":
#       print("Okay,Please wait...")
#       os.system("eog ./conservation/graph.svg")
#    while answer6 == "no":
#          break

#show()

#def scanmotif():
#    answer7=answer("Do you want to scan protein with motif from PROSITE database?(yes/no)")
#    if answer7 == "yes":
#       cid=[]
#       num=0
#       with open("./conservation/selectid.txt","r") as sfile:
#            lines=sfile.readlines()
#            for line in lines:
           
#                sid=line.split()
#                cid.append(sid[0])
#       for x in cid:
#           num+=1
#           sequenceid=x.strip()
#           subprocess.call("echo \"%s\" > ./motifone/%d.txt" %(sequenceid,num),shell=True)
#           subprocess.call("/localdisk/data/BPSM/Assignment2/pullseq -i ./raw_protein_sequence/sequence.fasta -n ./motifone/%d.txt>./motif3/pro%d.fasta"%(num,num),shell=True)
#           subprocess.call("patmatmotifs -sequence ./motif3/pro%d.fasta -outfile ./motiftwo/%d"%(num,num),shell=True)
#    else:
#         sys.exit(1)   

#scanmotif()

#def searchmotif():    
#    mdir=os.listdir("./motiftwo")
#    for files in mdir:
#        fdir="./motiftwo/"+files
#        line=linecache.getline("./motiftwo/"+files,14)
#        if re.search("HitCount: 0",line):
#            pass
#        else:
#            subprocess.call("cat %s >> ./motif.txt"%fdir,shell=True)

#searchmotif()
#def hint():
#        f="./motif.txt"
#        subprocess.call("grep -E 'Sequence:|Motif' %s >> result.txt" %f, shell=True)
#        answer8=answer("Now, you can find the sequence id and motif of them in the result.txt, do you want it show on the screen?(yes/no)")
#        if answer8=="yes":
#           subprocess.call("cat result.txt",shell =True)
#hint()


#def spt():
#    with open("./raw_protein_sequence/sequence.fasta") as openseq:
#         number=0
#         for line in openseq:
#          if ">" in line:
#             number+=1
#             lines=line.strip("/n")
#             subprocess.call("echo \"%s\">>./profa/pro%d.fa"%(lines,number),shell=True)
#          else:
#              lines=line.strip("/n")
#              subprocess.call("echo \"%s\">>./profa/pro%d.fa"%(lines,number),shell=True)



#def static():
#    answer9=answer("Do you want to do the protein static?(yes/no)")
#    if answer9=="yes":
#       print("Prepare...wait...")
#       spt()
#       mdir=os.listdir("./profa")
#       for files in mdir:
#           fdir="./profa/"+files 
#           subprocess.call("pepstats -sequence %s -outfile ./pepstats/%s.txt"%(fdir,files),shell=True)
#    else:
#        sys.exit()
#static()
#print("The result of the protein static locate at the pepstates!")

endword='Congratulation!Complete!'
print (endword.center(110))


