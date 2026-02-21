import os
import pathlib
import re

SRC = pathlib.Path('~/src/moreati.org.uk/_posts').expanduser()
DST = pathlib.Path('~/src/moreati.org.uk/content/blog').expanduser()

for dst in DST.glob('*'):
    os.remove(dst)

for src in sorted(SRC.glob('*.md')):
    m = re.match(
        r'(\d\d\d\d-\d\d-\d\d)-(.+)',
        str(src.name),
    )
    if not m: raise ValueError(src)

    content = src.read_text()
    content = re.sub(
        '\nlayout: post',
        f'\ndate: {m.group(1)}',
        content,
    )
    content = re.sub('\n---\n\n', '\ntype: post\n---\n\n', content, re.MULTILINE)
    content = re.sub(r'\{\{ site\.url \}\}', '', content)
    content = re.sub(r'\{% raw %\}|\{% endraw %\}', '', content)
    content = re.sub('<del>|</del>', '~~', content)
    content = re.sub('<sub>|</sub>', '~', content)
    content = re.sub('<span class="userInput">| *</span>', '', content)
    content = re.sub(
        r'<img alt="(.*?)" src="(.*?)" width="(.*?)">',
        r'![\1](\2)]',
        content
    )
    content = re.sub(
        '<iframe width="560" height="315" src="https://www.youtube.com/embed/dSVc2SrXVIk" frameborder="0" allowfullscreen></iframe>',
        '{{< youtube dSVc2SrXVIk >}}',
        content,
    )
    content = re.sub(
        r'(\[.+?\])\(\d\d\d\d/\d\d/\d\d/(.+?)/\)',
        r'\1({{< relref "\2.md" >}})',
        content,
    )
    if 'Money for Nothing' in content:
        content = re.sub('\n<br>\n', '  \n', content)

    dst = DST / m.group(2)

    dst.write_text(content)
