import csv # Importing csv allows VSCode to read directly from the .csv file

class Patient:
    allPatients = [] # List to hold all patient objects

    # Constructor with attributes of ____
    # def __init__(self, sex: str, age: int, yearsOfEducation: int, APOEgenotype: str, cognitiveStatus: str, aBeta40 : float, aBeta42: float, tTAU : float, pTAU : float): 
    #     self.sex = sex
    #     self.age = age
    #     self.yearsOfEducation = yearsOfEducation
    #     self.APOEgenotype = APOEgenotype
    #     self.cognitiveStatus = cognitiveStatus
    #     self.aBeta40 = aBeta40
    #     self.aBeta42 = aBeta42
    #     self.tTAU = tTAU
    #     self.pTAU = pTAU
    #     Patient.allPatients.append(self) # Adds the patient object to the allPatients list with the above data

    # # Representer: defines what will be shown when a patient object is printed
    # # Each variable defined in the constructor will be printed when a patient object is called, but there will be a label in front of the value so it is clear what the reader is looking at
    # def __repr__(self):  
    #     return f"(Sex: {self.sex}: Age: ({self.age} | Years of Education: {self.yearsOfEducation} | APOE Genotype: {self.APOEgenotype} | Cognitive Status: {self.cognitiveStatus} | Amyloid Beta-40 Status: {self.aBeta40} | Amyloid Beta-42: {self.aBeta42} | Total Tau: {self.tTAU} | Phosphorylated Tau: {self.pTAU})"

    # # Class method pulls objects from the .csv file and creates patient objects from this data
    # @classmethod 
    # def instantiate_from_csv(cls, filename: str):
        
    #     # The code below will open the .csv file and create a list of all the rows in the patient data spreadsheet
    #     with open(filename, encoding="utf8") as f:
    #         reader = csv.DictReader(f)
    #         rows_of_patients = list(reader)
                
    #         # The code below will create a patient object for each row, with the information declared in the constructor (sex, age, years of education, APOE genotype, cognitive status, aBeta-40, aBeta-42, tTAU, and pTAU): 
    #         # int and float are used on the columns that have whole numbers (int) or decimal numbers (float) to ensure they come in as the proper type for comparing the data later
    #         for row in rows_of_patients:
    #             Patient(
    #                 sex = row['Sex'],
    #                 age = (int(row['Age at Death'])),
    #                 yearsOfEducation = (int(row['Years of education'])),
    #                 APOEgenotype = row['APOE Genotype'],
    #                 cognitiveStatus = row['Cognitive Status'],
    #                 aBeta40 = (float(row['ABeta40 pg/ug'])),
    #                 aBeta42 = (float(row['ABeta42 pg/ug'])),
    #                 tTAU = (float(row['tTAU pg/ug'])),
    #                 pTAU = (float(row['pTAU pg/ug']))
    #             )