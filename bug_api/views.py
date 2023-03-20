from rest_framework.views import APIView
from bug_api.models import Bug
from bug_api.serializer import BugSerializer
from rest_framework.response import Response
from rest_framework import status

class BugList(APIView):
    def get(self, request):
        bugs = Bug.objects.all()
        serializer = BugSerializer(bugs, many=True)
        return Response(serializer.data)


class BugCreate(APIView):
    def post(self, request):
        serializer = BugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BugDetail(APIView):
    def get_bug_by_pk(self, pk):
        try:
            return Bug.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Bug does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        bug = self.get_bug_by_pk(pk)
        serializer = BugSerializer(bug)
        return Response(serializer.data)

    def put(self, request, pk):
        bug = self.get_bug_by_pk(pk)
        serializer = BugSerializer(bug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bug = self.get_bug_by_pk
        bug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        