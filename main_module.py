import rx
from rx import Observable, Observer
import time

class MyObserver(Observer):
  def on_next(self, x):
    print("on_next %s" % x)

  def on_error(self, e):
    print("on_error %s" % e)

  def on_completed(self):
    print("on_completed")

class CoinDispenser(Observer):
  def on_next(self, coin):
    self.ignoreNewCoin(True)

  def on_error(self, error):
    print("error")

  def on_completed(self):
    print("completed")

  def ignoreNewCoin(self, ignore):
    pass


class CoinLCDOutputObserver(Observer):
  def on_next(self, coin):
    self.outputLCD(coin)

  def on_error(self, error):
    print("error")

  def on_completed(self):
    print("completed")

  def outputLCD(self, digits):
    print("Implement here")



class StartMachine(Observer):
  def on_next(self, coin):
    print("StartMachine %s" % coin)

  def on_error(self, error):
    print("error")

  def on_completed(self):
    print("completed")

class WaterLevelController(Observer):
  def on_next(self, coin):
    self.pushButton()

  def on_error(self, error):
    print("error")

  def on_completed(self):
    print("completed")

  def pushButton(self):
    pass


    

if __name__ == "__main__":

  coinEvents = Observable.from_list([5, 10, 5, 5, 10, 5]).publish()



  Observable.from_iterable(range(4)) \
    .zip(Observable.interval(250)) \
    .subscribe(WaterLevelController())

  totalCoinEvent = Observable.from_iterable(range(6)) \
    .flat_map(lambda r: coinEvents.take(r) \
      .reduce(lambda a, b: a + b, 0)
    )

  totalCoinEvent.subscribe(CoinLCDOutputObserver())

  totalCoinEvent \
    .filter(lambda x: x > 20) \
    .map(lambda x: True) \
    .subscribe(CoinDispenser())

  totalCoinEvent \
    .filter(lambda x: x == 20) \
    .subscribe(StartMachine())

    
  coinEvents.subscribe(on_next=lambda x: print("This is coin event %s" % x))
  totalCoinEvent.subscribe(on_next=lambda x: print("This is total coin event %s" % x))

  coinEvents.connect()


  print("before sleep")
  time.sleep(10)
  print("finished execution")


  