
# coding: utf-8

# In[9]:


from collections import OrderedDict
import matplotlib.pyplot as plt
import seaborn as sns
from lxml import etree
import pickle
sns.set()


# In[10]:


datamap=OrderedDict()
datamap["android"]="android.stackexchange.com"
datamap["dba"]="dba.stackexchange.com"
datamap["softwareEng"]="softwareengineering.stackexchange.com"
datamap["serverfault"]= "serverfault.com"
datamap["superuser"]="superuser.com"
datamap["stackoverflow"]="stackoverflow.com-"


# In[12]:


def read_prog_lang(filename):
    data=OrderedDict()
    f=open(filename,"r")
    for l in f:
        row=l.split("\t")
        key=row[0].lower().strip()
        data[key]=[]
        for element in row[1].split(","):
            data[key].append(element.strip().lower())
    return data

def atleast_one(a, b):
    return not set(a).isdisjoint(b)

def refine_tags(tags):
    if tags!=None:
        l=tags.split('><')
        l=[i.replace('>','').replace('<','').lower() for i in l]
        return l
    else:
        return ["???"]

def init_data(logtags):
    data=OrderedDict()
    for lang in logtags:
        key=lang.lower()
        data[key]=OrderedDict()
        start_year=2008
        start_month=8
        end_year=2017
        end_month=12
        for year in range(start_year,end_year+1):
           
                data[key][str(year)]=0
     
    
    return data

def read_tags(filename):
    logtags=[]
    for row in open(filename,"r"):
        logtags.append(row.split(",")[0].strip().lower())   
    return logtags

def intersect(a, b):
    return list(set(a) & set(b))

tag_info={}
def add_tag(web,lang,tags,htags):
    
    itags=intersect(tags,htags)
    
    if lang not in tag_info[web]:
        tag_info[web][lang]={}
    for tag in itags:
        if tag not in tag_info[web][lang]:
            tag_info[web][lang][tag]=[[],0]
        tag_info[web][lang][tag][1]+=+1
        tag_info[web][lang][tag][0].extend(tags)
        #print(tag_info)

def check_tags(website,data,tags):
    for lang in langs:
        #print(tags,logtags[lang])
        if atleast_one(tags,prog_tags[lang]):
            # Atleast one logging tag
            #print("--",tags)
            add_tag(website,lang,tags,prog_tags[lang])
            return 1,lang

        elif atleast_one(tags,general_tags):
            if lang=="javascript":
                check=[lang,"js"]
            else:
                check=[lang]
            if atleast_one(tags,check):
                add_tag(website,lang,tags,general_tags)
                #print("?-",tags)
                return 1, lang
    return 0,0


# In[13]:


prog_tags=read_prog_lang("logging - Sheet4.tsv")
general_tags=list(set(read_tags("logging - Sheet3.csv")))
for i in prog_tags:
    general_tags.extend(prog_tags[i])
general_tags=list(set(general_tags))
langs=[i for i in prog_tags.keys()]


# In[5]:


def distribute_posts(logtags):
   
    data=init_data(prog_tags)
    data_o=init_data(prog_tags)
    for website in list(datamap.keys())[0:6]:
        fname=website
        tag_info[website]={}
        total_q,accepted_q,logging_q,total_logging_q=0,0,0,0
        
        if fname=="stackoverflow" and datamap[fname]=="stackoverflow.com-":
            datamap[fname]=datamap[fname]+"Posts"

        
        f=open("data/"+datamap[website]+"/Posts.xml","rb")
        next(f)
        next(f)
        for l in f:
            try:
                total_q+=1
                row=etree.XML(l)  
                posttypeid=row.get("PostTypeId") 
                acceptedanswerID=row.get("AcceptedAnswerId")
                tags=refine_tags(row.get("Tags"))
                
                
                if atleast_one(tags,general_tags):
                    result,lang=check_tags(website,data_o,tags)
                    total_logging_q+=1
                    if result==1:
                        
                        date=row.get("CreationDate")
                        key=date.split("T")[0][0:4]
                        if key not in data_o[lang]:
                            data_o[lang][key]=0
                        data_o[lang][key]+=1
                if posttypeid=="1" and acceptedanswerID!=None:
                    # Means it has an accepted answer
                    accepted_q+=1
                    
                    result,lang=check_tags(website,data,tags)
                    
                    if atleast_one(tags,general_tags):
                        logging_q+=1
                    
                    if result==1:
                        date=row.get("CreationDate")
                        key=date.split("T")[0][0:4]
                        if key not in data[lang]:
                            data[lang][key]=0
                        data[lang][key]+=1
                    
                    #print(tags)

            
            except:
                print(l)
        print(website,total_q,accepted_q,total_logging_q,logging_q)      
        f.close()
    return data,data_o


# In[39]:



# for prog in tag_info:
#     print(prog)
#     for tag in tag_info[prog]:
#         tags=list(set(tag_info[prog][tag][0]))
#         freq=tag_info[prog][tag][1]
#         print(tag,tags,freq)


# In[37]:


data,data_o=distribute_posts(prog_tags)
pickle.dump(tag_info,open("tag_info.txt","wb"))
# print(data_o)
# pickle.dump(data,open("results.txt","wb"))
# pickle.dump(data_o,open("results-2.txt","wb"))


# In[11]:


len("0")


# In[26]:


data

