# git1_CDV

### About project in CDV for GIT TRAINING

[Link to GIT tutorial](https://www.udemy.com/course/git-od-podstaw-dla-kazdego/)

### Sample code Python+Selenium Webdriver 
import unittest
from selenium import webdriver
```Python
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
 ```       

### Links 
  

### Picture  


### Fav git commands


### Fav terminal commands 

#### Manual post-release actions

The job will also create a Merge Request of this tag back to `develop` branch.
This MR is just a reminder – it is always impossible to merge it from GUI because there are conflicts.

Make sure you have maintainer role to the repo (required to directly push to `develop` branch) and execute:
```
git pull
git checkout develop
git merge <tag>
<manually resolve conflicts on CHANGELOG.md>
git commit
git push
```

Then close the MR without merging.

### Hotfix

Hotfix = bug is on production but you don't want to release develop.
As result the fix will be deployed from the last existing release branch.

We have a policy to create MR to both release branch and `develop` to see problems on `develop` faster (E2E tests run only on `develop`).

1. Create a branch from release branch: `git checkout -b yourbranch release-x.y`
1. Commit fixes to your branch
1. Create a branch from develop and cherry-pick your fixes: `git checkout -b yourbranch-dev develop && git cherry-pick yourbranch`
1. `git push -u origin yourbranch yourbranch-dev`
1. Create a Merge Request of _yourbranch_ to the old release branch
1. Create a Merge Request of _yourbranch-dev_ to `develop`
1. Accept MRs to the release branch and `develop`
1. Test on stage
1. Run release (see above) on release branch


```python
if __name__ == "__main__":
    # ...to uruchamiam testy
    unittest.main(verbosity=2)
```
