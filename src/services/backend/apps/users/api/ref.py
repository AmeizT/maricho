@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bookmarks_add_view(request, id, *args, **kwargs):
    product = get_object_or_404(Product, id=id)
    if request.user.is_authenticated:
        if request.user.bookmarks.filter(id=product.id).exists():
            request.user.bookmarks.remove(product)
            return Response({'message': 'removed'})
        else:
            request.user.bookmarks.add(product)
            return Response({'message': 'added'}, status=status.HTTP_200_OK)
    print(request.user.is_authenticated)
    return Response({'message': 'user'})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bookmarks_add_view(request, id, *args, **kwargs):
    account = get_object_or_404(Account, id=id)
    product = get_object_or_404(Product, id=id)
    if account.bookmarks.filter(id=product.id).exists():
        account.bookmarks.remove(product)
        return Response({'msg': 'removed'})
    else:
        account.bookmarks.add(product)
        return Response({'msg': 'added'})

    return Response({'msg': 'created'}, status=status.HTTP_200_OK)
