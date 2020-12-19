import pandas as pd
import json
import csv


class BMICalculation:
    def __init__(self,input_Filename):
        self.input_Filename=input_Filename
        self.reffile='rangereference.csv'
        self.ref_data=[[]]
        self.counts={}
        self.inpdf=pd.DataFrame()
        self.outputdf=pd.DataFrame()


    def calculateBMI(self,weight,heightcm):
        
        if  type(heightcm) is not int:            
            raise ValueError('Invalid data type of Height Value')
        if type(weight) is not int:
            raise ValueError('Invalid data type of Weight Value')
        
        if heightcm==0:
            raise ZeroDivisionError('Height Value is Zero')
        if heightcm<0:
            raise ValueError('Height Value is less than Zero',heightcm)
            
        if weight<=0:
            raise ValueError('Weight Value is Invalid',weight)
        try:
            
            height=heightcm/100
            bmi=weight/(height*height)
        except ZeroDivisionError:
            print('Height Value is zeroo')
        return bmi
    
    def readInputFile(self):    
        try:
            df=pd.read_json(self.input_Filename)
            
            return df
        except Exception as e:
            #raise IO('Input File Not found')
            print('Input File Not found')
    
    def loadreference(self):
        try:
            with open(self.reffile,'r') as referfile:
                self.ref_data=list(csv.reader(referfile))
        except IOError as e:
            raise IOError('Reference File Not Found')
            print('Reference File Not found')
            print(e)
        
    
    def checkBMIRange(self,bmi):        
        
        if bmi<=0:
            raise ValueError('BMI should be greater than 0',bmi)
        if type(bmi) is not float:
            raise ValueError('Invalid BMI Value',bmi)
            
        if bmi<=18.4:
            return self.ref_data[1]
        elif bmi>=18.5 and bmi<=24.9:
            return self.ref_data[2]
        elif bmi>=25 and bmi<=29.9:
            return self.ref_data[3]
        elif bmi>=30 and bmi<=34.9:
            return self.ref_data[4]
        elif bmi>=35 and bmi<=39.9:
            return self.ref_data[5]
        else:
            return self.ref_data[6]
    
    def getCounts(self,inpdf):
        co=inpdf.groupby("Category")["HeightCm"].count()
        self.counts=co.to_dict()
    
    def getOutputDF(self):
        temp=self.inpdf.apply(lambda x: self.checkBMIRange(self.calculateBMI(x.WeightKg,x.HeightCm)),axis=1)
        temp.columns=['Category','Range','Health']

        self.outputdf=pd.concat([BMIObj.inpdf,temp],axis=1)

filename='sample.json'
BMIObj=BMICalculation(filename)
BMIObj.loadreference()
BMIObj.inpdf=BMIObj.readInputFile()
BMIObj.getOutputDF()
#temp=BMIObj.inpdf.apply(lambda x: BMIObj.checkBMIRange(BMIObj.calculateBMI(x.WeightKg,x.HeightCm)),axis=1)
#temp.columns=['Category','Range','Health']
#
#BMIObj.outputdf=pd.concat([BMIObj.inpdf,temp],axis=1)
BMIObj.getCounts(BMIObj.outputdf)

print('Detailed Count for different Categories')
for key,value in BMIObj.counts.items():
    
    print(key,value)










