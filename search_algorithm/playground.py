#%%
#import and define necessary function and variable
import universal_function as uf
import search_algorithm.bruteforce as bf

answer = uf.getPassword()


#%%
#see how fast simple brute force reveals the password

bf.SimpleBurteForece(answer)
# %%
bf.adjBruteForece(answer)

