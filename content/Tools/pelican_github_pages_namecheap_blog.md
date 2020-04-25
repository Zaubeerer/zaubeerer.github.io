title: How fast can you set up your blog with Pelican, GitHub pages and namecheap?
date: 25th April 2020
author: Robin Beer
summary: Setting up my blog took me much less time than expected. Here, I show you how to do it even faster.
tags: HowTo, Python, GitHub,
status: published

For a long time, I wanted to create my own blog, but hesitated because I thought that it would take both quite some time to set it up and to write articles. But thanks to [PyBites](pybit.es), I finally got my blog online much faster than expected and started writing.

> Words are a lens to focus one's mind. - Ayn Rand

I was able to set up a draft version of my blog quickly (much less than 42 minutes) based on [this Pelican blog article](https://opensource.com/article/19/5/run-your-blog-github-pages-python) by Erik O'Shaughnessy. However, I spent quite some time on creating my own domain and connecting it with GitHub pages as Erik didn't cover that part. Therefore, I streamlined the tutorial and added my additional learnings.

So let's see how fast we can get you up and running. Read this post and then measure the time it takes you until you blog is online. :)

![Creative writing]({static}/Tools/images/pelican_github_pages_blog/writing_image.jpg)

## Create a git repository supporting GitHub Pages

In order to use [GitHub Pages](https://help.github.com/en/github/working-with-github-pages/getting-started-with-github-pages) you first have to [create a new GitHub repository](https://help.github.com/en/github/working-with-github-pages/creating-a-github-pages-site#creating-a-repository-for-your-site) using your username, such that the following repository results:

```bash
https://github.com/username/username.github.io
```

Just leave it empty for now and clone it using:

```bash
git clone https://github.com/username/username.github.io blog
```

Subsequently, create a content branch that will be used to track the markdown source files:

```bash
git checkout -b content
```

Therewith, the source files (markdown, Pelican config, ...) in the `content branch` can be separated from the web content, that needs to be pushed to the `master branch` for GitHub Pages to automatically publish them. :ok_hand:

So let's set up Pelican!

## Install and Configure Pelican

First of all, I suggest to create a virtual environment of your choice, for example using [conda env](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands):

```bash
conda create -n blog python=3
```

and activate it using `conda activate blog`.

Now, install the following Python packages:

```bash
pip install pelican ghp-import Markdown
```

You can generate the Pelican files using `pelican-quickstart`. You can take the default values, but probably want to set the `website title`, your `author name` and the `time zone` appropriately. You definitely have to choose:

```bash
> Do you want to upload your website using GitHub Pages? (y/N) y
```

Afterwards, your folder should contain the following files (use `dir` on Windows instead of `ls -l`):

```bash
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

```bash
git add .
git commit -m 'initial Pelican commit to content'
git push origin content
```

Great, you are all set up to ...

## Edit your blog

Add your first content by creating some dummy pages:

```bash
cd content
touch first-post.md
touch pages/about.md
```

Edit the markdown files, for example as follows:

`first-post.md`:

```bash
title: Hello World!
date: <today's date>
author: Your Name Here

This is my first post on my new blog. While not super informative it
should convey my sense of excitement and eagerness to engage with you,
the reader!
```

`pages/about.md`:

```bash
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

```bash
ghp-import -m "Generate Pelican site" --no-jekyll -b master output
```

Finally, push the changes to the `master branch`:

```bash
git push origin master
```

Congratulations, you have just published your changes to https://github.com/username/username.github.io. Check it out! :rocket:

### Version Control

Although your changes are published, the source markdown files are not yet version-controlled! :(

Therefore, version-control them using:

```bash
git add content
git commit -m 'added a first post and an about page'
git push origin content
```

Now, for each new blog article you want to write, you can create a new `article branch` based on the `content branch`, write the article and merge it into `content branch`. :pray:

## [www.your-domain.com](https://www.namecheap.com)

In order to bring your blog to a custom URL such as www.robin-beer.de instead of https://github.com/Zaubeerer/zaubeerer.github.io you first need to buy a domain. :moneybag:

Therefore, I used [namecheap](https://www.namecheap.com) as it enables you to search for a domain:

<!-- ![search for domain name]({filename}images/blog_images/namecheap_domain_search.png) -->

And informs you about the availability and costs of the possible domains:

<!-- ![domain search results]({filename}images/blog_images/namecheap_domain_search_results.png) -->

Once purchased, you need to inform GitHub pages about the custom URL and vice-versa.

Therefore, go to the settings of your GitHub pages repository, i.e. https://github.com/Zaubeerer/zaubeerer.github.io/settings for my blog:

<!-- ![repository settings]({filename}images/blog_images/2020-04-23-22-36-34.png) -->

Then, scroll down to the `GitHub pages` section and fill in your domain etc.:

<!-- ![GitHub pages settings]({filename}images/blog_images/2020-04-23-22-39-37.png) -->

Additionally, [you must create a CNAME file in your site's repository and configure a CNAME record with your DNS provider](https://help.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain).

The `CNAME` file was automatically generated when you filled in the custom domain in the `GitHub pages` settings. Additionally, you need to go to your DNS provider's site and create a `CNAME` record. For `namecheap`, you can find it as follows:

1. When logged in, click on `Domain List` in the left sidebar and then on `MANAGE` on the right of the respective domain.

   <!-- ![namecheap domain list]({filename}images/blog_images/2020-04-23-22-53-43.png) -->

2. Click on `Advanced DNS` and then `ADD NEW RECORD` on the bottom left.

    <!-- ![Advanced DNS settings in namecheap]({filename}images/blog_images/2020-04-23-22-53-11.png) -->

3. In the opening mask, select `CNAME Record` and fill in the data analogously to what is shown for my site's CNAME Record in the image above.

Maybe you have to wait a bit, but then your blog should be reachable via your custom domain! :)

## (Semi-) Automatic Deployment

Great! Now you just have to write articles on `article branches`, publish them using the `master branch` and merge them into the `content branch` right?

No, whenever you push to GitHub, it turns out that the custom domain gets reset so that you have to rewrite it manually in the `GitHub pages settings`. Or, do you? :thinking:

The reason why the custom domain is reset, is because when filling it in manually as shown above, a commit is created on remote, but overriden whenever you push to remote. Therefore, you need to pull and merge remote master into your local master, such that the `CNAME` file containing your custom branch persists. 

Now, you can `edit locally` and [publish as described above](#publish) and usually don't have to go to your GitHub pages repository anymore. :thumbsup:

## Conclusion

I hope that I can cut your learning curve with this article to get you up and running faster! Of course, you can spend endless time on fine-tuning the blog in terms of style and functionality, which I partly describe in [an upcoming article]({filename}pelican_blog_improvements.md). However, that's totally optional and it's much better to have a minimalistic blog with good articles than no blog or a fancy blog without articles, right?

So, let me know whether it was doable in 42 minutes (excluding the time you take to think about a proper domain name ;-)) and share your blog address in the comment section below.

Looking forward to reading from you! :man_technologist:

Robin