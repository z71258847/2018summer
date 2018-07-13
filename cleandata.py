import os

p="D:\\nyush\\2018research\\data\\"
target="midi.lab.corrected.lab"
if os.path.exists(p):
    os.chdir(p)
L=os.listdir()
ans=0
valid_list=[]
for i,x in enumerate(L):
    if os.path.isdir(x):
        if os.path.exists(x+"\\"+target) and os.path.exists(x+"\\lyric.lab") and os.path.exists(x+"\\zrc.txt"):
            ans+=1
            valid_list.append(i+1)
            #print(x)
            lyric_f=open(x+"\\lyric.lab", mode="r", encoding="utf-16-le")
            lyric_l=lyric_f.readlines()
            lyric_f.close()
            lyric=[]
            for i in range(len(lyric_l)):
                lyric_l[i]=lyric_l[i].strip('\ufeff').strip('\n')
                lyric.append(lyric_l[i].split('\t'))
            para_f=open(x+"\\zrc.txt", "r",encoding="utf-8")
            para_l=para_f.readlines()
            para_f.close()
            i = -1
            end_time=[]
            for sentence in para_l:
                for ch in sentence:
                    if ch=='>':
                        i+=1
                if i>=0:
                    #print(i, lyric[i])
                    end_time.append(float(lyric[i][1]))
            #print(end_time)
            pitch_f=open(x+"\\"+target, mode="r", encoding="utf-8")
            pitch_l=pitch_f.readlines()
            pitch_f.close()
            pitch=[]
            for i in range(len(pitch_l)):
                pitch_l[i]=pitch_l[i].strip('\ufeff').strip('\n')
                pitch.append(pitch_l[i].split('\t'))
            output=[]
            end_i=0
            lyric_i=0
            first_p=True
            for i, p in enumerate(pitch):
                if float(p[1])<float(lyric[lyric_i][0]):
                    continue
                temp=[]
                temp.append(float(p[0]))
                temp.append(float(p[1]))
                temp.append(float(p[2]))
                if first_p:
                    temp.append(lyric[lyric_i][2])
                    first_p=False
                else:
                    temp.append('-')
                if float(p[1])==end_time[end_i]:
                    temp.append(1)
                    end_i+=1
                else:
                    temp.append(0)
                if float(p[1])>=float(lyric[lyric_i][1]):
                    lyric_i+=1
                    first_p=True
                output.append(temp)
                if lyric_i==len(lyric):
                    break
            #print(output)
            output_f=open("output/"+x+".txt", "w")
            for p in output:
                temp_s=""
                for o in p:
                    temp_s= temp_s + str(o) + " "
                temp_s=temp_s[:-1]+"\n"
                output_f.write(temp_s)
            output_f.close()
    
