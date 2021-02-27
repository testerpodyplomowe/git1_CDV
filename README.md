# git1_CDV

### About project in CDV for GIT TRAINING

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

---
