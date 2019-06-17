import os

dir = 'marry/'

dir_list = os.listdir(dir)
for name in dir_list:
    filepath = 'images/'+dir+name

    content = '''
<div class="grid__item" data-size="1280x853"> <a href="%s" class="img-wrap"><img src="%s" alt="img1" />
    <div class="description description--grid">结婚证照片</div>
    </a> </div>
'''%(filepath,filepath)
    print(content)
