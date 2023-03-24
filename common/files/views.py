from common.models import *
from rest_framework.views import Response, APIView
from common.files.serializers import CommonFilesViewSerializer
from systemModules.views import userCompany


class CommonFilesView(APIView):
    def get(self, request, module_id, record_id):
        files = CommonFiles.objects.filter(module=module_id, record_id=record_id, company=userCompany(self.request.user.pk))
        return Response(
            CommonFilesViewSerializer(files, many=True).data
        )

    def post(self, request, module_id, record_id):
        module = Module.objects.get(pk=module_id)
        for file in request.FILES.getlist('attached_file'):
            file_name = os.path.basename("media/" + str(file))
            file_extension = pathlib.Path(file_name).suffix
            try:
                icon_id = FileIcon.objects.filter(suffix=file_extension).first()
                new_files = CommonFiles(
                    record_id=record_id,
                    company=userCompany(self.request.user.pk),
                    module=module,
                    attached_file=file,
                    icon_id=icon_id.pk,
                    user_id=request.user.pk,
                )
            except:
                new_files = CommonFiles(
                    record_id=record_id,
                    company=userCompany(self.request.user.pk),
                    module=module,
                    attached_file=file,
                    icon_id=1,
                    user_id=request.user.pk,
                )
            new_files.save()
        return Response(
            'success'
        )