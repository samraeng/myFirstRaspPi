import rx
from rx import Observable, Observer

class MyObserver(Observer):
  def on_next(self, x):
    print("on_next %s" % x)

  def on_error(self, e):
    print("on_error %s" % e)

  def on_completed(self):
    print("on_completed")


if __name__ == "__main__":
  xs = Observable.from_iterable(["red", "green", "orange"])
  d = xs \
      .map( lambda x: "process %a" % x ) \
      .subscribe(MyObserver())