It contains the materials cloud global theme common in all frontends.

Update the scss files to make any changes in global theme and generate 
mcloud_theme.css file which will be used in other frontend repositories.

*NOTE*: sass/theme.scss file internally imports bootstrap-sass and materials design styles. So the
generated mcloud_theme.css becomes 229K in size.

## Install packages

#### Ubuntu 14.04

Install nodejs and nam:

```bash
sudo apt-get install nodejs npm
```

> **Note:** If you get errors like **"E: Unable to correct problems, you have held broken packages**", install the packages from source distribution. 

Install ruby gems for SaSS
```bash
sudo gem install sass bundler
```

Install yo, bower, grunt
```bash
sudo npm install --global bower
```

#### OSX

Download and Install node and npm from OSX [installer](https://nodejs.org/en/download/)

Update npm
```bash
sudo npm install -g npm
```

Install grunt-cli, bower, yo, generator-karma, generator-angular:
```bash
sudo npm install -g bower
```

Install ruby gems for SaSS
```bash
sudo gem install sass bundler
```


## Building

```bash
git clone git@github.com:materialscloud-org/frontend-theme.git
cd frontend-theme
sudo bundle install
npm install && bower install
```


### Start the server to watch and compile sass file(s) into css file with command:

```bash
sass --watch sass/theme.scss:mcloud_theme.css
```