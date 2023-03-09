/ [Menu](/documentation/README.md) / [Tasks](/documentation/tasks/README.md) / [ORM](orm.md)

# Task: ORM

Django has a powerful ORM that almost completely eliminates the need for writing SQL directly.
In this task you will attempt to compose queries to find certain results.

<!-- I have seeded the database in solution to contain 1 million BlogPosts. -->
<br>

<details>
<summary>Behind the scenes</summary>

![Two Buttons](/documentation/images/orm_meme.jpg)

</details>

<br>

Resources:

- https://docs.djangoproject.com/en/4.1/topics/db/queries/
- https://docs.djangoproject.com/en/4.1/topics/db/queries/#complex-lookups-with-q-objects
- https://docs.djangoproject.com/en/4.1/topics/db/aggregation/

<br>
<br>

Table of contents:

- [Reference](#reference)
- [Step: Create queries](#step-create-queries)

<br>
<br>

## Reference

Given these models, write queries in the next [Step](#step-create-queries).

<details>
<summary>Show/hide</summary>

```py
class Author(models.Model):
    first_name = models.CharField(max_length=42)
    last_name = models.CharField(max_length=42)
    born = models.DateTimeField()

class Tag(models.Model):
    name = models.CharField(max_length=42)

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    published = models.DateTimeField()
    price = models.IntegerField()
    hidden = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
```

</details>

<br>
<br>

## Step: Create queries

Given BlogPost as model/item:

1. Find all items sorted by creation date (oldest first).
2. Find earliest published item.
3. Find all items where title is `'DjAnGo'` (any case).
4. Find the last item ordered by `id` (ascending) where `'outfit'` is not mentioned in the text.
5. Find all items published between 2020 and 2022.
6. Find all hidden items.
7. Find the total count of unique authors.
8. Find all items belonging to users with first_name `'Tommy'`.
9. Find all items without title.
10. Find all items where first_name is `'Tommy'` or last_name is not `'Viking'`.
11. Find all items belonging to users with id [11, 22, 33].
12. Find the average price of all items.
13. Find the most expensive item.
14. Find the item with most tags.

<details>
<summary>Solutions</summary>

1.

```py
BlogPost.objects.order_by('creation_date')
```

2.

```py
BlogPost.objects.order_by('-published').first()
# or
BlogPost.objects.order_by('published').last()
```

3.

```py
BlogPost.objects.filter(tilte__iexact='django')
```

4.

```py
BlogPost.objects.exclude(text__contains='outfit').order_by('id').last()
```

5.

```py
BlogPost.objects.filter(published__year__gte='2020', published__year__lte='2022')
```

6.

```py
BlogPost.objects.filter(hidden=True)
```

7.

```py
Author.objects.count()
```

8.

```py
BlogPost.objects.filter(author__first_name='Tommy')
```

9.

```py
BlogPost.objects.filter(title=None)
```

10.

```py
from django.db.models import Q
BlogPost.objects.filter( Q(author__first_name='Tommy') | ~Q(author__last_name='Viking') )
```

11.

```py
BlogPost.objects.filter(author__in=[11,22,33])
```

12.

```py
from django.db.models import Avg
BlogPost.objects.aggregate(Avg('price'))
```

13.

```py
from django.db.models import Max
BlogPost.objects.aggregate(Max('price'))
# or
BlogPost.objects.order_by('-price').first()
```

14.

```py
from django.db.models import Count
BlogPost.objects.annotate(tag_count=Count('tags')).order_by('-tag_count').first()
```

</details>

<br>
<br>

👈 Back to [Tasks](/documentation/tasks/README.md)
