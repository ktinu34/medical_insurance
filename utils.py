import pickle
import json
import numpy as np
import config





class MedicalInsurance():

    def __init__(self,age,gender,bmi,children,smoker,region):
        print("this is init function")

        self.age       = age
        self.gender    = gender
        self.bmi       = bmi
        self.children  = children
        self.smoker    = smoker
        self.region    = region


    def __load_saved_data(self):

   
        

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_predicted_price(self):
        self.__load_saved_data()


        gender = self.json_data['gender'][self.gender]
        smoker = self.json_data['smoker'][self.smoker]
        region = 'region_'+self.region

        region_index = self.json_data['columns_names'].index(region)
     
        test_array = np.zeros([1,self.model.n_features_in_])

        test_array[0,0] = self.age
        test_array[0,1] = gender
        test_array[0,2] = self.bmi
        test_array[0,3] = self.children
        test_array[0,4] = smoker
        test_array[0,region_index] = 1
        
        predicted_charges = self.model.predict(test_array)[0]
        return round(predicted_charges,3)