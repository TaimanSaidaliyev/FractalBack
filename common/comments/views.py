from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from common.models import Comment
from .serializers import  CommentsByRecordId, AddUpdateCommentsById
from systemModules.views import userCompany
from systemModules.models import Module


class CommentsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, record_id, module_id):
        module = Module.objects.get(pk=module_id)
        comments = Comment.objects.filter(module=module,
                                          record_id=record_id,
                                          company=userCompany(self.request.user.pk))\
                                                                .select_related('author__profile')\
                                                                .all().order_by('-created_at')
        return Response({
            'comments': CommentsByRecordId(comments, many=True).data
        })

    def post(self, request, record_id, module_id):
        serializer = AddUpdateCommentsById(data=request.data)
        serializer.is_valid(raise_exception=True)
        module = Module.objects.get(pk=module_id)
        serializer.save(author=self.request.user,
                        company=userCompany(self.request.user.pk),
                        module=module,
                        record_id=record_id,
                        isPublished=True)
        return Response({'post': serializer.data})

    def put(self, request, pk, record_id, module_id):
        if not pk:
            return Response({"error": "Method PUT now allowed"})
        try:
            instance = Comment.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        module = Module.objects.get(pk=module_id)
        serializer = AddUpdateCommentsById(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user,
                        company=userCompany(self.request.user.pk),
                        module=module,
                        record_id=record_id,
                        isPublished=True)

        return Response({"post": serializer.data})


    def delete(self, request, pk):
        if not pk:
            return Response({"error": "Method PUT now allowed"})
        try:
            instance = Comment.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})
        instance.delete()
        return Response('Success')