
# coding: utf-8

# In[1]:


import requests
apikey = 'WD3QHXU7171B7EAKIVPAXACFC97KVNWSUT'

start = 5124843
end  = 5435029


url = f'https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock=0&toBlock=latest&address=0x622dFfCc4e83C64ba959530A5a5580687a57581b&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'#\
#&apikey='+apikey
request = requests.get(url)
results = request.json()
# print(len(results['result']))
results


# In[6]:


import requests
apikey = 'WD3QHXU7171B7EAKIVPAXACFC97KVNWSUT'

start = 5124843
end  = 5435029

# for i in range(start, end+1000, 500):
#     url = f'https://api.etherscan.io/api?module=logs&action=getLogs\
#     &fromBlock={i}\
#     &toBlock={i+999}\
#     &address=0x622dFfCc4e83C64ba959530A5a5580687a57581b\
#     &topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'#\
#     #&apikey='+apikey
#     request = requests.get(url)
#     results = request.json()
#     print(len(results['result']))
#     for result in results['result']:
#         print('transactionHash : ' + result['transactionHash'])
#         print('block number : %d' %int(result['blockNumber'],0))
#         print('data : %d' %(int(result['data'],0)/1e18 ))
#         print('from : 0x%040x' %eval(result['topics'][1]))
#         print('to   : 0x%040x' %eval(result['topics'][2]))


# In[ ]:


import requests
apikey = 'WD3QHXU7171B7EAKIVPAXACFC97KVNWSUT'

start = 5124843
end  = 5435029
with open('CubeEtherTransfer_EdgeList_interval_30' + '.csv' , 'w') as CET:
    CET.write('"TxHash","Block Height","Source","Target","Weight","Quantity"\n')
    for i in range(start, end+1000, 30):
        url = f'https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={i}&toBlock={i+999}&address=0x622dFfCc4e83C64ba959530A5a5580687a57581b&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'#\
        #&apikey='+apikey
        request = requests.get(url)
        results = request.json()
        print(url)
        if len(results['result']) < 1000:
            print(len(results['result']))
        else:
            print('length exceed 1000!!!')
        for i,result in enumerate(results['result']):
            print(type(result))
            TxHash = result['transactionHash']
            BlockNum = int(result['blockNumber'],0)
            Quantity = int(result['data'],0)/1e18
            Source = eval(result['topics'][1])
            Target = eval(result['topics'][2])
            
            CET.write('"%s","%d","0x%040x","0x%040x","1","%d"\n' %(TxHash,BlockNum,Source,Target,Quantity))
            print('transactionHash : ' + TxHash)
            print('block number : %d' %BlockNum)
            print('data : %d' %(int(result['data'],0)/1e18 ))
            print('from : 0x%040x' %eval(result['topics'][1]))
            print('to   : 0x%040x' %eval(result['topics'][2]))


# In[16]:


for i in range(123,456,50):
    print(f'{i},{i+49}')


# In[15]:


print(f'0x{eval("0x4e4a63"):040X}')


# In[14]:


len('823d4b1e126684b7fbc5198a07e745508f7b97e325e8965be70f134ba26d1975')

