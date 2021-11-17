#%%
import random
import time
import universal_function as universal



def SimpleBurteForece(password):
    '''
    SimpleBurteForece() is a function for finding an answer by generating possible combination.
    This generates a certain length of String. Which then compares with the answer
    
    '''
    
    

    #Cracking starts
    startTime = time.time()
    char = "abcdefghijklmnopqrstuvwxyz0123456789"
    charList = list(char)
        
    #Generate random password
    generatedPass = universal.listToString(random.choices(charList, k=len(password)))
    
    #Generate possible combination for finding the password
    while(generatedPass != password):
        generatedPass = universal.listToString(random.choices(charList, k=len(password)))
        print(f"Generated Pass ===========>> {generatedPass}")

    endTime = time.time()
    processedTime = endTime - startTime
    print(f"=====> Processed Time =============>>>> {processedTime}")

    print("=====================>>>>>> DONE ")




def adjBruteForce(password):
    '''
    adjBruteForce() is adjusted for more efficiency. 
    This function generates a base-line. With this base-line, this function corrects wrong Strings along iteration.

    Through iteration, Function removes wrong String from the potential substitutes list if the String is classified as Wrong. 
    Thus this reduction of potential String reduces the overall iteration which then increases effieciency.
    '''

    #Cracking starts
    startTime = time.time()

    char = "abcdefghijklmnopqrstuvwxyz0123456789"
    charList = list(char)

    #Generate random password
    generatedPass = random.choices(charList, k=len(password))

    #Find out the password
    for i in range(len(password)):
        iteration_num = 0
        ite_charList = list(char)

        #Investigate correct letter on a certain position
        while(generatedPass[i]  != password[i]):
            generatedPass[i] = random.choice(ite_charList)
            
            if (generatedPass[i]  == password[i]):
                print(f'Detected at iteration {iteration_num} ===>> {generatedPass[i]}')
            else:
                ite_charList.remove(generatedPass[i])
                iteration_num += 1
                
    detectedPass = universal.listToString(generatedPass)

    endTime = time.time()
    processedTime = endTime - startTime
    print(f"=====> Detected Pass==========>> {detectedPass} ")
    print(f"=====> Actual Pass ===========>> {password}")
    print(f"=====> Processed Time =============>>>> {processedTime}")

# %%
