"""Small, independently testable feature for a fork contribution."""
def completion_percent(done, total):
    if not isinstance(done,int) or isinstance(done,bool) or not isinstance(total,int) or isinstance(total,bool):
        raise TypeError('Task counts must be integers.')
    if done<0 or total<0 or done>total:
        raise ValueError('Require 0 <= done <= total.')
    return round(100*done/total,2) if total else 0.0
