# Website

This folder contains the actual website to publish.


## Website update

```bash
cp -r website /tmp/update_website
git switch github-pages
rm -rf docs
cp -r /tmp/update_website docs
rm -rf docs
git add .
git commit -m "Update website"
git push

git switch main
```