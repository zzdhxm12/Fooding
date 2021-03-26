from django.db.models import query
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ReviewSerializer
from .models import Review, Store
from accounts.models import User

from reviews import serializers

# Create your views here.
# 회원별 리뷰 불러오기


@api_view(['GET'])
def review_info(request, id):
    if User.objects.filter(id=id).exists():
        review = Review.objects.filter(user_id=id)
        
        review_data = []

        for i in review:
            store = Store.objects.get(id=i.store_id)

            review_data.append({
                "id": i.id,
                "user_id": i.user_id,
                "store_id": i.store_id,
                "store_name": store.store_name,
                "contents": i.contents,
                "write_date": i.write_date,
                "star": i.star,
            })
        
        return JsonResponse(review_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=status.HTTP_200_OK)

        # serializer = ReviewSerializer(review_data, many=True)
 
        # return Response(serializer.data, store_num, status=status.HTTP_200_OK)

    else:
        return Response({'message': '회원정보가 존재하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)


# 가게별 리뷰 불러오기
@api_view(['GET'])
def review_list(request, store_id):
    if Store.objects.filter(id=store_id).exists():
        review = Review.objects.filter(store_id=store_id)

        review_user = []

        for r in review:
            ru = User.objects.get(id=r.user_id)

            review_user.append({
                "id": r.id,
                "user_id": r.user_id,
                "nickname": ru.nickname,
                "contents": r.contents,
                "write_date": r.write_date,
                "store_id": r.store_id,
                "star": r.star,
            })

        return JsonResponse(review_user, safe=False, json_dumps_params={'ensure_ascii': False}, status=status.HTTP_200_OK)

    else:
        return Response({'message': '가게정보가 존재하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)


# 리뷰 목록 불러오기(최신 날짜 순 30개)
@api_view(['GET'])
def review_cur(request):
    list = Review.objects.all().order_by('-write_date')[:30]

    serializer = ReviewSerializer(list, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# 리뷰 작성
@api_view(['POST'])
def review_write(request):

    try:
        if Review.objects.filter(id=request.data.get('id')).exists():
            Review.objects.create(
                user_id = request.data.get('user_id'),
                store_id = request.data.get('store_id'),
                contents = request.data.get('contents'),
                star = request.data.get('star'),
                write_date = request.data.get('write_date'),
            ).save()

            # 스푼 카운트 갱신 및 등급 조정
            if User.objects.get(id=request.data.get('user_id')):
                
                userdata = User.objects.get(id=id)
                userdata.update(spoon_cnt=userdata.spoon_cnt+1)
                if userdata.spoon_cnt >=99:
                    userdata.update(grade='gold')
                elif userdata.spoon_cnt >=49:
                    userdata.update(grade='silver')

                print(userdata)
            return Response({'success': 'success'}, status=status.HTTP_201_CREATED)
    except KeyError:
        return Response({'error': 'KeyError'}, status=status.HTTP_400_BAD_REQUEST)



# 리뷰 삭제(리뷰 번호 일치시 삭제)
@api_view(['DELETE'])
def review_del(request, id):
    if Review.objects.filter(id=id).exists():
        queryset = Review.objects.filter(id=id)
        return queryset.delete()

    else:
        return Response({'message': '리뷰정보가 존재하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)
