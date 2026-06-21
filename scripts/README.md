# Scripts

This folder contains the scripts to generate the actual website for ease of navigation by users.


## Website update

```bash
python3 scripts/builder/builder.py

cp -r scripts/builder/build /tmp/update_website
git switch github-pages
rm -rf docs
cp -r /tmp/update_website docs
git add .
git commit -m "Update website"

git switch main
```