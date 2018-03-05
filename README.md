[![Build Status](https://travis-ci.org/DEV3L/measure-me-jenkins.svg?branch=master)](https://travis-ci.org/DEV3L/measure-me-jenkins?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/DEV3L/measure-me-jenkins/badge.svg?branch=master)](https://coveralls.io/github/DEV3L/measure-me-jenkins?branch=master)
[![Code Climate](https://codeclimate.com/github/DEV3L/measure-me-jenkins/badges/gpa.svg)](https://codeclimate.com/github/DEV3L/measure-me-jenkins)


# measure-me-jenkins

Application to extract build health metrics from Jenkins


## Prerequisites
* Python3 installed
    * <https://www.python.org/downloads/>
* virtualenv installed
    * <https://virtualenv.pypa.io/en/latest/>
    * sudo pip3 install --upgrade virtualenv virtualenvwrapper


# Usage/Setup Instructions
```bash
# environment variables
set GITHUB_USERNAME={github username w/o 2fa}
set GITHUB_PASSWORD={github password for username}

# clone project
git clone https://github.com/DEV3L/measure-me-jenkins.git
cd measure-me-jenkins

# runtime environment
mkvirtualenv -p /usr/local/bin/python3 measure-me-jenkins
python setup.py develop

pythun run.py

```


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-kata`
3. Commit your changes: `git commit -am 'Add some kata template'`
4. Push to the branch: `git push origin my-kata`
5. Submit a pull request :D
