# Django Form

- Form Class를 선언하는 것은 Model Class를 선언하는 것과 비슷함

- 사용하는 이유
  
  - 고객이 입력하는 데이터는 요청사항에 맞는 데이터만 입력하는게 아니라서 유효성 검증이 필요함
  
  - 이걸 쉽게 해주는게 Django Form



## Form class 선언

> - Model class 선언과 비슷하다.
>   
>   1. 앱 폴더에 forms.py 생성 후 ArticleForm class 선언
>   
>   2. ArticelForm에 들어갈 내용 작성
>      
>      1. title = forms.charField(max_length=30)
>      
>      2. content = forms.CharField()
>   
>   3. view 업데이트
>      
>      1. form = ArticleForm() 선언을 위해 상단에 form 클래스 import 해오기
>      
>      2. `from .forms import ArticleForm`
>      
>      3. html 파일 업데이트
>         
>         1. {{form.as_p}}



## Form rendering options

1. as_p()
   
   - 각 필드가 p태그로 감싸져서 렌더링

2. as_ul()
   
   - 각 필드가 목록 항목 li태그 로 감싸져서 렌더링
   
   - ul 태그는 직접 작성

3. as_table()
   
   - 각 필드가 tr태그 로 감싸져서 렌더링
- 보통의 상황은 as_p만 사용



## widget

- 입력받은 CharField()의 스타일 변경을 위해서 () 안에 widget=forms.Textarea로 변경

- <mark>widget은 반드시 form fields에 할당</mark>



## Django ModelForm

> - Form class 와 Model class 의 공통된 부분이 많으므로 같이 사용하는것
>   
>   1. forms.py 에 models에 작성한 Article 클래스를 import 해옴
>   
>   2. ArticleForm(forms.ModelForm): 클래스 선언
>   
>   3. 정보를 작성해줄 Meta 클래스 선언
>   
>   4. class Meta:
>   
>   5. 담을 정보 작성
>   
>   6. model = Article
>   
>   7. fields = `'__all__'`
>   
>   또는
>   
>   8. exclude = (제외대상)
>   
>   이런식으로 작성이 가능해짐
>   
>   당연히 하나만 가져오거나, 특정한것 몇개만 가져오거나 가능함 제외하는 방식으로 가져올 수 도 있음
>   
>   근데 field와 exclude를 같이 쓰는건 별로 권장하는게 아님



### ModelForm 작성 및 클래스 선언 후

> 1. view 수정해주기
>    
>    - form을 사용하는 html 파일을 불러오는 view 함수들을 수정해주면 된다.
>    
>    - 지금은 create 와 update가 form을 사용하니 view를 수정해줘야 함
>    
>    - create 수정해주기
>    
>    ```python
>    def create(request):
>        if request.method == 'POST':
>            form = ArticleForm(request.POST)
>            if form.is_valid():
>                article = form.save()
>                return redirect('articles:detail', article.pk)
>        else:
>            form = ArticleForm()
>    
>        context = {'form' : form }
>        return render(request, 'articles/create.html', context)
>    ```

              요런식으로 수정해주면 된다

**is_valid() method**

- 유효성 검사를 실행하는 메소드

- 유효성 여부를 boolean으로 반환  



> 마찬가지로 update 수정해주기
> 
> ```python
> def update(request, article_pk):
>     article = Article.objects.get(pk = article_pk)
>     if request.method == 'POST':
>         form = ArticleForm(request.POST, instance=article)
>         if form.is_valid():
>             form.save()
>             return redirect('articles:detail', article.pk)
>     else:
>         form = ArticleForm(instance=article)
> 
>     context = {'form' : form, 'article' : article }
>     return render(request, 'articles/update.html', context)
> ```
> 
> instance 들어가는 이유 수정이 되야 하는 정보를 담아줘야 하기 때문임
> 
> 여기서 instance = article 이라 했는데 article에는 pk를 통해 페이지 정보 하나를 불러옴 불러온 article을 instance에 담아서 수정 대상이 되는 form의 정보를 저장해서 html로 넘겨주는 거 그럼 해당하는 페이지 정보가 나와서 수정 되서 저장되는 거  

**view 수정 후 html 파일 수정하기**

> - 기존의 내용을 지우고 {{  form.as_p }} 작성



# Static File

- 별도의 처리없이 파일 내용을 그대로 보여주면 되는 파일

- 파일 자체가 고정 되어 있고 서비스 중에 추가되거나 변경되지 않고 고정 되어 있음

## Media File

> - 사용자가 웹에서 업로드하는 정적 파일
> 
> - 사용자가 `~경로에 있는 사진줘 라고 요청을 보냄` 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공함



## Django에서 정적파일을 구성하고 사용하기 위한 몇가지 단계

1. INSTALLED_APPS에 django.contrib.staticfiles 가 포함되어 있는지 확인하기

2. settings.py에 STATIC_URL 정의

3. 앱의 static 폴더에 정적 파일 위치 시키기

4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기
   
   1. {% load static %}



settings.py 의 하단에 적힌 

STATIC_URL = '/static/'

뒤에

STATICFILES_DIRS=[BASE_DIR / 'static']

정의 해주고 앱폴더 밖에 static 폴더 만들기

폴더 안에 css 적용할 파일 이름 만들고 css 적용

그 후 html 파일로 돌아가서 최상단에 load 작성해주고 head 요소에 link 태그 추가하기

link의 href는 {% static 'base.css' %} 형태로 작성

이후 html에 정적이미지를 추가하려면 img 태그 작성 후 {% static '파일이름' %} 으로 작성
