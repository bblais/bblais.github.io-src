title: Something Satisfying About Building Pelican Themes
date: 7/03/2020
image: katarzyna-urbanek-l0PCrW_4J4A-unsplash.jpg

[Pelican is a Python package] for developing static websites.  I started out my blog with Wordpress and then toyed with Wix and Weebly.  But I found I didn't like the idea of a company holding my content -- if that company suddenly started to charge for the services, or disappeared altogether I didn't want my information caught in the middle.  I also liked the control that a static site builder, like [Pelican] gives you.  Finally, I like working in [Markdown] for my blog content (and most of my other content as well).

There are a lot of [themes for Pelican] to choose from, and although I have [used some before] I find them looking a little dated.  So for the past few designs of this website what I've done is head over to [Colorlibs Free Web Templates] and find a template that looks good, like [Elen], [Miniblog], or [Philosophy].  For good measure, get a pelican theme to help with comparisons, something like [Plummage].  Make sure to have the [Creating Pelican Themes] site handy!  After that, it's pretty straightforward to port the web template over to a pelican theme -- but I still do a lot of trial and error! 

I think the satisfying parts of the developing a Pelican theme is to see years of articles instantly look like new.  For example, in the [Philosophy] template `index.html` there is this snippet which presents the summary of a blog article,

```html
<article class="masonry__brick entry format-standard" data-aos="fade-up">
        
    <div class="entry__thumb">
        <a href="single-standard.html" class="entry__thumb-link">
            <img src="images/thumbs/masonry/lamp-400.jpg" 
                    srcset="images/thumbs/masonry/lamp-400.jpg 1x, images/thumbs/masonry/lamp-800.jpg 2x" alt="">
        </a>
    </div>

    <div class="entry__text">
        <div class="entry__header">
            
            <div class="entry__date">
                <a href="single-standard.html">December 15, 2017</a>
            </div>
            <h1 class="entry__title"><a href="single-standard.html">Just a Standard Format Post.</a></h1>
            
        </div>
        <div class="entry__excerpt">
            <p>
                Lorem ipsum Sed eiusmod esse aliqua sed incididunt aliqua incididunt mollit id et sit proident dolor nulla sed commodo est ad minim elit reprehenderit nisi officia aute incididunt velit sint in aliqua...
            </p>
        </div>
        <div class="entry__meta">
            <span class="entry__meta-links">
                <a href="category.html">Design</a> 
                <a href="category.html">Photography</a>
            </span>
        </div>
    </div>

</article> <!-- end article -->
```

This is repeated once for many different articles, making for a long `index.html` file.  In the pelican theme, the `index.html` loops over all of the articles and generates this long list using [Jinja] syntax,

```html
{% for article in articles_page.object_list %}

    <article class="masonry__brick entry format-standard" data-aos="fade-up">
            
        <div class="entry__thumb">
            <a href="{{ SITEURL }}/{{ article.url }}" class="entry__thumb-link">

                {% if article.image %}
                    <img src="{{ SITEURL }}/images/{{ article.image }}">
                {% else %}
                    <img src="{{ SITEURL }}/images/default.png">
                {% endif %}
            </a>
        </div>

        <div class="entry__text">
            <div class="entry__header">
                
                <div class="entry__date">
                    <a href="{{ SITEURL }}/{{ article.url }}">{{ article.locale_date }}</a>
                </div>
                <h1 class="entry__title"><a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }} {%if article.subtitle %} <small> {{ article.subtitle }} </small> {% endif %} </a></h1>
                
            </div>
            <div class="entry__excerpt">
                <p>
                    {{ article.summary}}
                </p>
            </div>
            <div class="entry__meta">
                <span class="entry__meta-links">
                    <a href="{{ SITEURL }}/{{ article.category.url }}">{{ article.category }}</a> 
                </span>
            </div>
        </div>

    </article> <!-- end article -->

{% endfor %}
```

Notice the injection of Python here: 

* a loop to generate the html
* variables, like `article.date` and `article.category`, to put in article-specific information
* if-statements to include option content, like subtitles
* if-statements to include default behavior, in case no image is given for example

This provides a level of control that is hard to match.  

To make the theme, as shown in the docs, you need to just make the following files

```
  ├── static
  │   ├── css
  │   └── images
  └── templates
      ├── archives.html         // to display archives
      ├── period_archives.html  // to display time-period archives
      ├── article.html          // processed for each article
      ├── author.html           // processed for each author
      ├── authors.html          // must list all the authors
      ├── categories.html       // must list all the categories
      ├── category.html         // processed for each category
      ├── index.html            // the index (list all the articles)
      ├── page.html             // processed for each page
      ├── tag.html              // processed for each tag
      └── tags.html             // must list all the tags. Can be a tag cloud.
```

Starting from the free web template, I break off the parts that are included in all of the files and put it in `base.html`, copying the [Jinja] parts from a pelican theme.  Like,

```html
<!DOCTYPE html>
<html class="no-js" lang="en">
<head>

    <!--- basic page needs
    ================================================== -->
    <meta charset="utf-8">
    <title>{% block title %}{{ SITENAME|striptags }}{% endblock title %}</title>
    <meta name="description" content="">
    <meta name="author" content="Brian Blais">

    <!-- mobile specific metas
    ================================================== -->
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

    {% block head_links %}

    <!-- CSS
    ================================================== -->
    <link rel="stylesheet" href="{{ SITEURL }}/theme/css/base.css">
    <link rel="stylesheet" href="{{ SITEURL }}/theme/css/vendor.css">
    <link rel="stylesheet" href="{{ SITEURL }}/theme/css/main.css">

    {% block extra_css %}{% endblock %}
    <!-- favicons
    ================================================== -->
    <link rel="shortcut icon" href="{{ SITEURL }}/favicon.ico" type="image/x-icon">
    <link rel="icon" href="{{ SITEURL }}/favicon.ico" type="image/x-icon">

    <!-- script
    ================================================== -->
    <script src="{{ SITEURL }}/theme/js/modernizr.js"></script>
    <script src="{{ SITEURL }}/theme/js/pace.min.js"></script>
    {% endblock head_links %}

</head>


<body id="top">

    {% include 'header.html' %}

        {% block content %}
        {% endblock content %}


        {% include 'footer.html' %}


    <!-- preloader
    ================================================== -->
    <div id="preloader">
        <div id="loader">
            <div class="line-scale">
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>
    </div>


    {% block script %}

    <!-- Java Script
    ================================================== -->
    <script src="{{ SITEURL }}/theme/js/jquery-3.2.1.min.js"></script>
    <script src="{{ SITEURL }}/theme/js/plugins.js"></script>
    <script src="{{ SITEURL }}/theme/js/main.js"></script>
    {% block extra_js %}{% endblock %}

    {% endblock script %}

</body>

</html>
```

which you can compare to the first and last parts of the `index.html` of the [Philosophy] template.   

It took me about a week to iron out most of the nits to get the final version, but the process was just fun.  There is something really satisfying about constructing something like a website by scripting.   Every time I learn something new.  One thing was to include `{% block extra_css %}{% endblock %}` and `{% block extra_js %}{% endblock %}` allowing some of the pages to include specific css and js files, which was instrumental in getting the tipue search working.  

Questions about my process?  Or any other part of this project, please [contact me]!


[Pelican is a Python package]: https://docs.getpelican.com/en/stable/
[Pelican]: https://docs.getpelican.com/en/stable/
[themes for Pelican]: http://pelicanthemes.com
[used some before]: https://elegant.oncrashreboot.com
[Colorlibs Free Web Templates]: https://colorlib.com/wp/templates/
[Elen]: https://colorlib.com/wp/template/elen/
[Miniblog]: https://colorlib.com/wp/template/miniblog/
[Philosophy]: https://colorlib.com/wp/template/philosophy/
[Plummage]: https://github.com/kdeldycke/plumage
[Creating Pelican Themes]: https://docs.getpelican.com/en/latest/themes.html
[Jinja]: https://jinja.palletsprojects.com/en/2.11.x/
[contact me]: http://bblais.github.io/contact.html
[Markdown]: https://www.markdownguide.org/basic-syntax
