title: How to set up a blog in 42 minutes using Pelican, GitHub pages and namecheap
date: 22nd April 2020
author: Robin Beer
summary: How did I set up this blog? A full description of how to set up a blog using the Python package Pelican, GitHub pages and namecheap.
tags: HowTo, Python, GitHub, 

What? If you knew it might only take 42 minutes you would also have created your own blog to share your thoughts with the world? Let's see whether it holds true. Read this post and then time how long it takes you. :)

## Create a git repository supporting GitHub Pages

In order to use [GitHub Pages](https://help.github.com/en/github/working-with-github-pages/getting-started-with-github-pages) you first have to [create a new GitHub repository](https://help.github.com/en/github/working-with-github-pages/creating-a-github-pages-site#creating-a-repository-for-your-site) using your username, such that the following repository results:

```
https://github.com/username/username.github.io
```

Just leave it empty for now and clone it using:

```
git clone https://github.com/username/username.github.io blog
```

Subsequently, create a content branch that will be used to track the markdown source files:

```
git checkout -b content
```

Therewith, the source files (markdown, Pelican config, ...) in the `content branch` can be separated from the web content, that needs to be pushed to the `master branch` for GitHub Pages to automatically publish them. So let's set up Pelican!

## Install and Configure Pelican

First of all, I suggest to create a virtual environment of your choice, for example using [conda env](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands):

```
conda create -n blog python=3
```
and activate it using `conda activate blog`.

Subsequently, install the following Python packages:
```
pip install pelican ghp-import Markdown
```

Now you can generate the Pelican files using `pelican-quickstart`. You can take the default values, but probably want to set the `website title`, your `author name` and the `time zone` appropriately. You definitely have to choose:

```
> Do you want to upload your website using GitHub Pages? (y/N) y
```

Now, your folder should contain the following files:

```
$ ls -l
.
..
Makefile
content
output
pelicanconf.py
publishconf.py
tasks.py
```

Subsequently, initialize the `content branch` to be able to revert to this state, just in case:

```
git add .
git commit -m 'initial Pelican commit to content'
git push origin content
```

Great, you are all set up to ...

## Edit your blog

Add your first content by creating some dummy pages:

```
cd content
touch first-post.md
touch pages/about.md
```

Edit the markdown files, for example as follows:

`first-post.md`:

```
title: Hello World!
date: <today's date>
author: Your Name Here

This is my first post on my new blog. While not super informative it
should convey my sense of excitement and eagerness to engage with you,
the reader!
```

`pages/about.md`:
```
title: About
date: <today's date>
<p style = "font-family:georgia,garamond,serif;font-size:24px;line-height:1.4">
<q>
This is a quote describing my mission statement...
</q>
</p>

You can [contact me via email](mailto:) or on [twitter](https://twitter.com/), [LinkedIn](https://www.linkedin.com/in/) or [GitHub](https://github.com/).

Cheers!

<username>
```

Basically, you can create your blog posts by simply adding markdown files in the content folder. If you want to cluster your articles in different categories, you can create the articles in the folders `content/category_1`, `content/category_1`, etc. and Pelican will automatically create these categories.

You normally want to add static pages such as `about.md` in the pages directory.

Now, let's get this content online!

## Commit and Publish your Changes

As described above, the content will be published using the `master branch` and the source files will be version controlled using the `content branch`.

### Publish

First, generate the web content using Pelican:

```bash
pelican content -o output -s publishconf.py
```

Now, add the web content files that are generated in the `output` directory to the `master branch` using `ghp-import`:

```
ghp-import -m "Generate Pelican site" --no-jekyll -b master output
```

Finally, push the changes to the `master branch`:

```
git push origin master
```

Congratulations, you have just published your changes to https://github.com/username/username.github.io. Check it out!

### Version Control

Although your changes are published, the source markdown files are not yet version-controlled!

Therefore, version-control them using:
```
git add content
git commit -m 'added a first post and an about page'
git push origin content
```

Now, for each new blog article you want to write, you can create a new `article branch` based on the `content branch`, write the article and merge it into `content branch`.

## [www.your-domain.com](https://www.namecheap.com)

In order to bring your blog to a custom URL such as www.robin-beer.de instead of https://github.com/Zaubeerer/zaubeerer.github.io you first need to buy a domain.

Therefore, I used [namecheap](https://www.namecheap.com) as it enables you to search for a domain:

![search for domain name](namecheap_domain_search.png)

And informs you about the availability and costs of the possible domains:

![](namecheap_domain_search_results.png)
Once purchased, you need to inform GitHub pages about the custom URL and vice-versa.

<!-- #TODO: explain how to  link GitHub and namecheap-->

Therefore:
settings

Maybe you have to wait a bit, but then your blog should be reachable via your custom domain! =]

## (Semi-) Automatic Deployment

Great! Now you just have to write articles on article branches, publish them using master and merge them into the content branch right?

No, whenever you push to GitHub, it turns out that the custom domain gets reset so that you have to rewrite it manually. Or, do you? 

The reason ...
<!-- TODO: explain how to solve CNAME bug -->
CNAME github bug

Therefore: add locally and push

## Conclusion

For a long time, I wanted to create my own blog, but hesitated because I thought that it would take both quite some time to set it up and to write articles. But thanks to [PyBites](pybit.es), I finally got my blog online much faster than expected and started writing.

I was able to set up a draft version of my blog quickly based on [this Pelican blog article](https://opensource.com/article/19/5/run-your-blog-github-pages-python) by Erik O'Shaughnessy but spent quite some time on creating my own domain and connecting it with GitHub pages.

Therefore, I hope that I can cut your learning curve with this article to get you up and running faster! Of course, you can spend endless time on fine-tuning the blog in terms of style and functionality, which I partly describe in [an upcoming article](). However, that's totally optional and it's much better to have a minimalistic blog with good articles than no blog or a fancy blog without articles, right?

So, let me know whether it was doable in 42 minutes (excluding the time you take to think about a proper domain :D) and share your blog address in the comment section below.

Looking forward to reading from you!

Robin