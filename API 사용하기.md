# API 사용하기

1. djangoframework 설치하기
   
   `pip install djangorestframework`

2. settings.py의 INSTALLED_APPS에 rest_framework 추가히기

3. model 정의하기
   
   - models.py 에 사용할 model 정의
   
   ```python
   class Book(models.Model):
      title = models.CharField(max_length=30)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
   ```

4. serializers.py 정의하기
   
   - serializers.py 생성 후 rest_framework 이용해서 정의하기
     
     ```python
     from rest_framework import serializers
     from .models import Book
     ```
     
      로 임폴트 받아오기
   
   - serializer class 정의하기
     
     ```python
     class BookListSerializer(serializers.ModelSerializer):
      class Meta:
         model = Book
         fields = '__all__'   # << 기본형식
     ```
     
      이런식으로 사용할 serializer 정의해서 사용하면 된다.
   
   - 만약 serializer에 다른 필드를 사용하고 싶다면 model 정의된 필드들을 직접 적어서 사용하면 된다.
     
     ```python
     class BookListSerializer(serializers.ModelSerializer):
     class Meta:
        model = Book
        fields = ('id', 'title')
     ```

5. urls 정의
   
   1. 전체 url에서 사용할 url 분기 후 urls.py 생성하여 정의해주기
      
      ```python
      from djanog.urls import path
      from . import views
      
      app_name = 'books'
      urlpatterns = [
       path('books/', views.book_list, name='book_list')
      ]
      ```

6. views.py 수정
   
   1. serializers를 사용할 것이므로 from import 해올게 많다
      
      ```python
      from rest_framework.response import Response
      from rest_framework.decorators import api_view
      from rest_framework import status
      from django.shortcuts import get_object_or_404
      
      from .serializers import BookListSerializer
      from .models import Book
      
      @api_view(['GET','POST'])
      def book_list(request):
          if request.method == 'GET':
              book = get_list_or_404(Book)
              serializer = BookListSerializer(book,many=True)
              return Response(serializer.data)
      
          elif request.method == 'POST':
              serializer = BookListSerializer(data=request.data)
              if serializer.is_valid(raise_exception=True):
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      ```
- 참고사항
  
  - get_object_or_404
  
  - get_list_or_404
    
    - 차이점
      
      - object는 단일로 들고올때 사용됨 serializer에 넘겨주는거에 단일로 들고오므로 들고옴 model 설정 하나만 넘겨주면 된다
      
      - list 는 여러값을 가지고 올때 사용된다.
        
        model에 넘겨받는 값이 여러개 이므로 serializer에서 받아오는 값도 여러개 이므로 many=True 를 적어줘야 

---

위에까지가 전체 리스트 조회와 생성

# 단일 정보조회 및 수정, 삭제

1. 단일 책정보 조회하기

```python
# url > path('books/<int:book_pk>', views.book_detail, name='book_detail')

@api_view(['GET','DELETE','PUT'])
def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
   # book = Book.objects.get(pk = book_pk)  둘중 하나 사용하면 됨
    if request.method == 'GET':
        serializer = BookListSerializer(book)
        return Response(serializer.data)
```

2. DELETE 요청

```python
elif request.method == 'DELETE':
   book.delete()
   return Response(status=status.HTTP_204_NO_CONTENT)
```

3. PUT 요청
   
   ```python
   elif request.method == 'PUT':
   serializer = BookListSerializer(book, data=request.data)
   if serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_뭐시기뭐시기)
   ```

---

N:1 관계 설정하기

1. models.py 수정
   
   - N:1 관계를 설정할 class 정의 및 ForeignKey로 설정하기 
   
   ```python
   # ex) aritcle / comment로 N:1 관계 정의
   class Comment(models.Model):
       article = models.ForeignKey(Article, on_delete=models.CASCADE)
       content = models.TextField()
   ```

2. serializer 작성
   
   ```python
   from .models import Article, Comment
   
   class CommentSerializer(serializers.ModelSerializer):
       class Meta:
           model = Comment
           fields = '__all__'
   ```
   
   GET으로 전체 데이터 및 단일데이터는 기존의 작성법과 동일
   
   POST 요청시 주의점
   
   - 댓글은 해당 게시글에 달리는 것이므로 해당 게시글의 정보가 필요함
   
   - `url >> path('articles/<int:article_pk>/comments/',views.comment_create)`
   
   ```python
   def comment_create(request, article_pk):
       article = Article.objects.get(pk = artilce_pk)
       serializer = CommentSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           serializer.save(article=artilce)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
   ```
- 또 serializer에서 읽기전용 필드를 설정해 두지 않으면 article 정보를 직접 입력해야 하므로 CommentSerializer에 읽기전용 필드를 설정해야함
  
  `read_only_fields = ('article',)`
  
  DELETE와 PUT 요청은 기존작성방법과 동일

---

역참조를 이용하여 게시글에서 특정 댓글 조회하기

1. serializer 수정
   
   - ArticleSerializer에서 받아오는 정보에 댓글정보를 조회하기 위해 역참조 필드 설정
   
   - `comment_set = serializer.PrimaryKeyRelatedField(many=True, read_only = True)`

역참조 이름 변경하기

지금은 comment_set 으로 접근하는데 이름을 변경하기 위해서는 정참조되는 serializer에서 이름을 변경해 줘야함 

위와같은 경우에서는 comment 필드에서 역참조 될때 이름을 바꿔줘야함

` realted_name = 'comments'` 를 ForeignKey 필드에 추가

이렇게 작성을 완료했으면 위에 comment_set으로 접근할때 길게쓴거 지우고 CommentSerializer(many=True, read_only=True) 해주면 된다.

---

N:M 관계

model에 N:M으로 설정되는 관계 이름을 class에 추가해주기

`ex) >> movie 와 actor의 관계는 N:M 이므로 class에 필드 추가해주기`

`actors = models.ManyToManyFields(Actor. related_name='movies'`
