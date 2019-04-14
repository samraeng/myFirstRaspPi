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


if __name__ == "__main__":
  xs = Observable.from_iterable(range(10)).publish()
  d = xs \
      .map(lambda x: "Correct" if x == 45 else "In Correct") \
      .subscribe(MyObserver())

  # e = xs \
  #     .map(lambda x: "non-delayed %s" % x) \
  #     .subscribe(MyObserver())

  powerEvent = Observable.from_callback()

  it = Observable.interval(1000).publish()

  processedXs = xs \
    .map(lambda x: x * x) \
    .filter(lambda x: x > 30) \
    .reduce(lambda x, y: x + y, 0)

  throttledSequences = processedXs.zip(it, lambda asx, ait: asx) \
      .map(lambda x: "Throttled %s" % x) \
      .subscribe(MyObserver())

  xs.connect()
  it.connect()

  print("before sleep")
  time.sleep(10)
  print("finished execution")


  