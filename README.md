<h1 align="center">
📖 Arachnida - 42 Cibersecurity
</h1>

<p align="center">
	<b><i>Web Scrapping Projects Bootcamp</i></b><br>
</p>

<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/Falitomal/Arachnida?color=lightblue" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/Falitomal/Arachnida?color=yellow" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Falitomal/Arachnida?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Falitomal/Arachnida?color=green" />
</p>



## ✏️ Summary
```

Metadata is information that is used to describe other data; essentially, it is **data about data**.

It is often used in images and documents, **and may reveal sensitive information** about those who created or manipulated it.

```
## 💡 About the project

```
Create 2 tools ($texttt{spider}$ and $texttt{scorpion}$) that allow to extract information from a website automatically and then analyze it to know or remove sensitive data.
Functions or libraries that allow to create HTTP requests and handle files can be used,
but the logic of each program must be developed by me, i.e. $texttt{wget}$, $texttt{scrapy}$, or similar libraries cannot be used.


```
## 🛠️ Usage
```
```
# spider
```
This program must receive as argument a URL from which it will extract the images.

```shell
python3 spider.py -h
```
```
 python spider.py [-r] [-l MAX_DEPTH] [-p PATH] URL
   url: the URL to start the spider
   -r, --recursive: recursively download images
   -l, --max-depth [N]: maximum depth level of the recursive download (default: 5)
   -p, --path [PATH]: path to save downloaded files (default: ./data/)     


```


# scorpion

This program must receive as argument path, one or several images from which it will extract its metadata.


```shell
python3 scorpion.py -h
```
```
usage: usage python scorpion.py image1.jpg image2.jpg doc.pdf

Home-made tool that displays metadata of images and pdfs.

positional arguments:
  path Directory to parse.
  IMAGE Image to analyze
  IMAGES Images to parse.

optional arguments:
  -h, --help show this help message and exit



```
