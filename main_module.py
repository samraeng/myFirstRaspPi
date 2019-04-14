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
    print("dispense coin %s" % coin)

  def on_error(self, error):
    print("error")

  def on_completed(self):
    print("completed")

class CoinLCDOutputObserver(Observer):
  def on_next(self, coin):
    print("display LCD %s" % coin)

  def on_error(self, error):
    print("error")

  def on_completed(self):
    print("completed")

if __name__ == "__main__":

  def handleInterrupt(coin):
    print("produce coin event")

  coinEvents = Observable.from_list([5, 10, 5, 5, 10, 5]).publish()


  totalCoinEvent = Observable.from_iterable(range(6)) \
    .flat_map(lambda r: coinEvents.take(r).reduce(lambda a, b: a + b, 0)) \

  totalCoinEvent.subscribe(CoinLCDOutputObserver())

  totalCoinEvent \
    .filter(lambda x: x > 20) \
    .subscribe(CoinDispenser())

  totalCoinEvent \
    .filter(lambda x: x == 20) \
    .subscribe(StartMachine())

  coinEvents.connect()


  print("before sleep")
  time.sleep(10)
  print("finished execution")


  