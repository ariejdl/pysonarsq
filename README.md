# This is a port of [PySonar2](https://github.com/yinwang0/pysonar2) from Java to Python: 'PySonarSquared'

## Copyright
See [PySonar2](https://github.com/yinwang0/pysonar2)'s copyright

## Installation

`python setup.py install`

## Example Usage
`python ./scripts/run_analyzer.py /usr/lib/python2.7 ./genned-html`

or

```
git clone https://github.com/ariejdl/pysonarsq.git
cd pysonarsq
mkdir genned-html
python scripts/temp_test.py tests/all.py
```

## Remaining failing tests
these shouldn't be hard to fix compared to already passing ones, they are less important to me, pull requests welcome.

- date_time.py
- reassign.py
- tmpattr.py

## Minor bugs
- the cache directory is sometimes relative...other things more important


## Useful future features
- `dict` key and value inference

## Info

- **Pull Requests welcome**
- Code is ugly from java conversion [java2python](https://code.google.com/p/java2python/)
- Much manual porting was done
- tested on Python 2.7 only

### Some lessons learned from porting

- java2python:
	- seems to omit casts, this slowed progress down a lot
	- it isn't sure when to use getName or `__name__`
	- method overrides are time consuming to fix, `___0()`, `___1()` etc.
	- other things...
- hashCode and compareTo are implicitly used in java for things like HashMaps, the equivalent in python are `__hash__` and `__cmp__`
- ...
