import google.generativeai as genai
def main(user_input):
    
    Apikeys=["AQ.Ab8RN6K5FTsEoEbDQF6Spo5c-htnlrpOxOE8UcnLRmSG2SYILA","AQ.Ab8RN6Llx2qoSp4Peo7-Riq5LGFhlpp8uY2mwrKSq-773KaWkg"]
    genai.configure(api_key="AQ.Ab8RN6K5FTsEoEbDQF6Spo5c-htnlrpOxOE8UcnLRmSG2SYILA")
    try:
        genai.configure(api_key ="AQ.Ab8RN6K5FTsEoEbDQF6Spo5c-htnlrpOxOE8UcnLRmSG2SYILA")
        model =genai.GenerativeModel(
            "models/gemini-2.5-flash")
         
        response = model.generate_content(user_input)
        return (response.text)
        pass
    
    except Exception as P:  
        
        #print(P)
        try:
            genai.configure(api_key="AQ.Ab8RN6Llx2qoSp4Peo7-Riq5LGFhlpp8uY2mwrKSq-773KaWkg")
            model =genai.GenerativeModel(
                "models/gemini-2.5-flash")
            response = model.generate_content(user_input)
            return(response.text)
        except Exception as T:
             return(T)
#userinput=input("enter your prompt")
#house=main(user_input)
#print(house)

 



        
        
            
     
    
            
       

            
            


            
        

       
    

    

