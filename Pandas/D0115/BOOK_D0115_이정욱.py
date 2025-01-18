# p.397
korean, english, mathmatics, science = 100, 86, 81, 91

def get_max_score(*args):
    max_score = max(args)
    return max_score

max_score = get_max_score(korean, english, mathmatics, science)
print('높은점수', max_score)
max_score = get_max_score(english, science)
print('높은점수', max_score)

#p.398
# korean, english, mathmatics, science = map(int,input().split())
korean, english, mathmatics, science = 100, 86, 81, 91

def get_min_max_score(*args):
    max_score = max(args)
    min_score = min(args)
    return min_score, max_score

def get_average(**kwargs):
    total = sum(kwargs.values())
    average_score = sum(kwargs.values())/len(kwargs)
    return average_score


min_score, max_score = get_min_max_score(korean, english, mathmatics, science)
average_score = get_average(korean = korean, english = english,
                            mathmatics = mathmatics, science=science)

print(f"낮은 점수 : {min_score:0.2f}, 높은 점수 : {max_score:0.2f}, 평균 점수 : {average_score:0.2f}")


#p417
files = ['font', '1.png', '10.png', '11.gif', '2.jpg', '3.png', 'table.xlsx', 'spec.docs']
print(files[2].find('png'))
print(list(filter(lambda x:x.find('jpg') >= 0  or x.find('png') >= 0, files )))

# find - 찾는 문자열의 시작인덱스를 반환.


#p418
files = '1.jpg 10.png 11.png 2.jpg 3.png'
files = files.split() 

x = list(map(lambda x: "{0:03d}.{1}".format(int(x.split('.')[0]),x.split('.')[1]),files))
print(x)


