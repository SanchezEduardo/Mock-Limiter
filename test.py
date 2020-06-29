#!/usr/bin/env python3

import time
import random

class MyClass():
  def __init__(self, rate, per, rate2, per2): 
    self.rate = rate
    self.per = per

    self.rate2 = rate2
    self.per2 = per2

    self.total = 0
    self.totalT = 0
    
    self.total2 = 0
    self.totalT2 = 0
    self.wait = 0 

    print(f'API LIMIT: {self.rate}:{self.per},{self.rate2}:{self.per2}\n')

  def MockRequest(self):
    # mimic random times in which you recieve the packages
    time.sleep(random.uniform(0.1, 0.4))
    print('RESPONSE DATA HERE')

  def Limiter(self):
    start = time.time()
    self.MockRequest()
    # request was made so add 1 to self.total for every new request
    passed = time.time() - start
    print(f'Time passed since last request... {passed}')
    self.totalT += passed
    self.totalT2 += passed
    print(f'Total time passed... {self.totalT}\n')
    self.total += 1
    self.total2 += 1

    if(self.totalT > self.per):
      print(f'{self.totalT} > {self.per}\n')
      print('========== RESETTING 1 SECOND INTERVAL ==========\n')
      self.totalT = 0
      self.total = 0

    if(self.totalT2 > self.per2):
      print(f'{self.totalT2} > {self.per2}\n')
      print('========== RESETTING 120 SECOND INTERVAL ==========\n')
      self.totalT2 = 0
      self.total2 = 0

    if(self.total == self.rate and self.totalT > self.per):
      self.wait = 5
      print(f'condition 1 met: Reached request limit, too many requests in {self.per} seconds... setting throttle. Waiting {self.wait} seconds to continue...\n')
      self.totalT = 0
      self.total = 0
      time.sleep(self.wait)

    
    if(self.total >= self.rate and self.totalT < self.per):
      self.wait = self.per - self.totalT
      print(f'condition 2 met: Reached request limit... setting throttle. Waiting {self.wait} seconds to continue...\n')
      self.totalT = 0
      self.total = 0
      time.sleep(self.wait)

    if(self.total2 == self.rate2 and self.totalT > self.per):
      self.wait = self.per2 - self.totalT2
      print(f'condition 3 met: Reached request limit... setting throttle. Waiting {self.wait} seconds to continue...\n')
      self.totalT2 = 0
      self.total2 = 0
      time.sleep(self.wait)

    if(self.total2 >= self.rate2 and self.totalT2 < self.per2):
      self.wait = self.per2 - self.totalT2
      print(f'condition 3 met: Reached request limit... setting throttle. Waiting {self.wait} seconds to continue...\n')
      self.totalT2 = 0
      self.total2 = 0
      time.sleep(self.wait) 
    

if __name__ == '__main__':
  '''
  Doing 200 requests...
  RIOT LIMITS: 20:1, 100:120

  rate1/per1 = 20/1
  rate2/per2 = 100/120
  '''

  rate1 = 20
  per1 = 1

  rate2 = 100
  per2 = 120

  x = MyClass(rate1, per1, rate2, per2)
  for i in range(1,400):
    print(f'Making request... {i}')
    x.Limiter()

