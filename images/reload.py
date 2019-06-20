import os

new_list = {}

dir_list = {'wang':'wang','hu':'hu','women':'women'}
for typea in dir_list:
  dir = dir_list[typea]
  file_list = os.listdir(dir)
  for name in file_list:
      new_list[name.split('.')[0]] = typea


new_lists = sorted(new_list.keys())
for names in new_lists:
  dir = new_list[names]
  filename = names+'.jpg'
  file_path = 'images/'+dir+'/'+filename
  content = '''
        <div data-sjsel="%s">
            <div class="card">
                <a href="%s" target="_blank">
                  <img class="card__picture" src="%s">
                </a>
                <div class="card-infos">
                    <h2 class="card__title">%s</h2>
                    <p class="card__text">
                      这里是备注
                    </p>
                </div>
            </div>
        </div>''' % (dir,file_path,file_path,names)
  print(content)
