from django.db.models import Count, Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from .models import News, Category
from .serializers import \
    NewsSerializerView, CategoryListView, NewCommentsById, \
    DataSerializer, CategoryListSerializer, UserInformation, AuthorProfileSerializer, AddNewCommentsById, NewsSerializer
from common.models import Comment
from django.contrib.auth.models import User
from systemModules.models import Company, Module
from userInformation.models import Profile


def userCompany(pk):
    user = Profile.objects.get(pk=pk)
    company_pk = Company.objects.get(pk=user.company.pk)
    return company_pk


class NewSingle(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        new = News.objects.get(pk=pk, company=userCompany(self.request.user.pk))
        try:
            profile = Profile.objects.get(pk=new.author.pk, company=userCompany(self.request.user.pk))
        except:
            profile = []
        return Response(
        {
            'author': AuthorProfileSerializer(profile).data,
            'new': NewsSerializerView(new).data
        })


class NewsList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        news = News.objects.filter(company=userCompany(self.request.user.pk)).order_by('-pk')[5:11]
        lastNew = News.objects.filter(company=userCompany(self.request.user.pk)).order_by('-pk').first()
        lastThreeNews = News.objects.filter(company=userCompany(self.request.user.pk)).order_by('-pk')[1:3]
        secondThreeNews = News.objects.filter(company=userCompany(self.request.user.pk)).order_by('-pk')[3:5]
        categories = Category.objects.filter(company=userCompany(self.request.user.pk))
        lastNewsBlock = News.objects.filter(company=userCompany(self.request.user.pk)).order_by('-pk')[:5]
        return Response(
        {
            'news': NewsSerializerView(news, many=True).data,
            'lastNew': NewsSerializerView(lastNew).data,
            'lastThreeNew': NewsSerializerView(lastThreeNews, many=True).data,
            'secondThreeNew': NewsSerializerView(secondThreeNews, many=True).data,
            'categories:': CategoryListView(categories, many=True).data,
            'lastNewsBlock': NewsSerializerView(lastNewsBlock, many=True).data
        })


class NewsAllList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, page=1, limit=5, search_value=None):
        try:
            search_value = request.GET.get('searchValue')
        except:
            search_value = None

        if (search_value):
            news = News.objects.filter(Q(content__icontains=search_value) | Q(title__icontains=search_value),
                                       company=userCompany(self.request.user.pk)).order_by('-pk')
        else:
            news = News.objects.filter(company=userCompany(self.request.user.pk)).order_by('-pk')
        return Response(
        {
            'news': NewsSerializerView(news, many=True).data
        })


class NewsListByCategory(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        news = News.objects.filter(category_id=pk, company=userCompany(self.request.user.pk)).order_by('-pk')
        return Response(
        {
            'news': NewsSerializerView(news, many=True).data
        })


class NewComments(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        comments = Comment.objects.filter(module=1, record_id=pk, company=userCompany(self.request.user.pk))
        return Response({
            'comments': NewCommentsById(comments, many=True).data
        })

    def post(self, request, pk):
        serializer = AddNewCommentsById(data=request.data)
        serializer.is_valid(raise_exception=True)
        module = Module.objects.get(pk=1)
        serializer.save(author=self.request.user,
                        company=userCompany(self.request.user.pk),
                        module=module, record_id=pk,
                        is_published=True)
        return Response({'post': serializer.data})

    def put(self, request, pk):
        if not pk:
            return Response({"error": "Method PUT now allowed"})
        try:
            instance = Comment.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        module = Module.objects.get(pk=1)
        serializer = AddNewCommentsById(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user,
                        company=userCompany(self.request.user.pk),
                        module=module, record_id=pk,
                        is_published=True)

        return Response({"post": serializer.data})


class CategoryList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        categories = Category.objects.annotate(items_count=Count('get_category')).filter(company=userCompany(self.request.user.pk))
        return Response({
            'categories': CategoryListSerializer(categories, many=True).data
        })


class NewAdd(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = DataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user, company=userCompany(self.request.user.pk))
        return Response({
            'post': serializer.data
        })


class NewUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT now allowed"})
        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class NewDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        news = News.objects.get(pk=pk, company=userCompany(self.request.user.pk))
        news.delete()
        return Response({
            'message': 'Удалено'
        })


class WhoAmI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        return Response({
            'user': UserInformation(user, many=False).data
        })


class SetViewNew(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        new = News.objects.get(pk=pk)
        new.views = new.views + 1
        new.save()

        return Response(True)