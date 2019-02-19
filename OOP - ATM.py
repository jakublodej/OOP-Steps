
# coding: utf-8

# In[1]:


class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    
    def __str__(self):
        return ("Account owner :{}. Your balance is {}.".format(self.owner,self.balance))
        
    def deposit(self,dep):
        self.balance +=dep
        return ('Deposit accepted')
    def withdraw(self,wdraw):
        if self.balance >= wdraw:
            self.balance -= wdraw
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


# In[2]:


firstclinet=Account("Kuba",200)


# In[3]:


print(firstclinet)


# In[4]:


firstclinet.deposit(200)


# In[5]:


print(firstclinet)


# In[6]:


firstclinet.withdraw(300)


# In[7]:


print(firstclinet)


# In[9]:


firstclinet.withdraw(300)

