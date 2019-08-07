from __future__ import unicode_literals

AUTHOR = u'Saurav Sengupta'
SITENAME = u'Saurav Sengupta'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

DEFAULT_METADATA = {
    'Status': 'draft',
}

SLUGIFY_SOURCE = 'basename'  # use the file name for slug

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('unicodeit.net', 'http://www.unicodeit.net'),
)

# Google Analytics
GOOGLE_ANALYTICS = 'UA-143413428-1'

# Social widget
SOCIAL = (
    ('github', 'https://github.com/ssen7/'),
    ('twitter', 'https://twitter.com/sauravsen111'),
    ('linkedin', 'https://www.linkedin.com/in/saurav-sengupta/'),
    ('file-text', '/files/cv.pdf'),
    ('rss', '/feeds/all.atom.xml'),
)
TWITTER_USERNAME = 'sauravsen111'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PATH = 'content'
PAGE_EXCLUDES = ['files', 'extras']
ARTICLE_EXCLUDES = ['files', 'pages', 'extras']

STATIC_PATHS = ['images', 'files', 'extras', 'posts']

EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    # 'extras/CNAME': {'path': 'CNAME'},
    # 'extras/nojekyll': {'path': '.nojekyll'},
}

THEME = "pure"

# plugins
PLUGIN_PATHS = ['../pelican-themes/pelican-plugins']
PLUGINS = [
    'sitemap', 'gravatar',  # 'pelican_jsmath',  # 'render_math',
    'liquid_tags.img', 'liquid_tags.video',
    'liquid_tags.youtube', 'liquid_tags.vimeo',
    'liquid_tags.include_code',
    # 'liquid_tags.notebook',
    'representative_image',
    # 'image_process',
    'pelican-cite',
    'related_posts',
    'pelican_dynamic',
    # 'disqus_static',
    # 'better_figures_and_images',
    # 'minchin.pelican.plugins.image_process',
    # 'pelican_advance_embed_tweet',
]

# sitemap plugin
SITEMAP = {
    'format': 'xml',
    'changefreqs': {
        'articles': 'monthly',
        'pages': 'monthly',
        'indexes': 'monthly'
    }
}

# related posts
RELATED_POSTS_MAX = 3

# advance embed tweet
# TWITTER_CARDS = 'hidden'
TWITTER_DNT = 'true'
TWITTER_ALIGN = 'center'

# Pelican cite plugin
# PUBLICATIONS_SRC = 'content/publications.bib'

# Image Process plugin
IMAGE_PROCESS = {
    'thumb': {'type': 'image',
              'ops': ["scale_in 300 300 True"],
              },
    'crisp': {'type': 'responsive-image',
              'srcset': [('1x', ["scale_in 800 600 True"]),
                         ('2x', ["scale_in 1600 1200 True"]),
                         ('4x', ["scale_in 3200 2400 True"]),
                         ],
              'default': '1x',
              },
    'large-photo': {'type': 'responsive-image',
                    'sizes': ('(min-width: 1200px) 800px, '
                              '(min-width: 992px) 650px, '
                              '(min-width: 768px) 718px, 100vw'),
                    'srcset': [('600w', ["scale_in 600 450 True"]),
                               ('800w', ["scale_in 800 600 True"]),
                               ('1600w', ["scale_in 1600 1200 True"]),
                               ],
                    'default': '800w',
                    },
}

# my pure theme specific
INTERNAL = False
# USE_LOCAL_ASSETS = True
COVER_IMG_URL = '/images/home-bg-2.jpg'
AUTHOR_EMAIL = 'sauravsengupta7@gmail.com'
AUTHOR_IMAGE = '/images/download.jpg'
TAGLINE = 'Research Scientist at the University of Virginia'
META_DESCRIPTION = 'my personal website'

DISQUS_SITENAME = 'ssen7-github-io'
# DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'
PAGE_URL = ''
PAGE_IDENTIFIER = '{slug}'

COPYRIGHT_YEARS = '2019 &ndash; 2019'
COPYRIGHT_FOOTER = (
    '<p>'
    '&copy; ' + SITENAME + '  ' + COPYRIGHT_YEARS +
    '. Published with <a href="https://github.com/getpelican/pelican">Pelican</a>.<br />'
    # 'This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.'
    '</p>'
)

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'
# Make about page the front page
INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_HOME_LINK = '/blog/'

# do not make pages of the type {slug}/index.html as this clashed with
# other github repositories with the same name as {slug}
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARCHIVES_SAVE_AS = 'blog/archives.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
TAGS_SAVE_AS = 'blog/tags.html'

MENUITEMS = [
    ('About', '/'),
    ('Projects', '/projects.html'),
    ('Blog', '/blog/'),
    ('Publications', '/publications.html'),
    ('Resume', '/files/cv.pdf'),
]
# DISPLAY_PAGES_ON_MENU = True

TYPOGRIFY = True
