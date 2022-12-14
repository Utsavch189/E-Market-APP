from rest_framework.response import Response
from rest_framework.decorators import api_view
from Auth.Jwt import Authorization
from django.http import HttpResponse
from decouple import config
from datetime import date,datetime
import json
import random
from .models import *
from Admins.models import ApprovedUsers
from Manufacturer.models import DayByDayProductsDistribute,SetProduct
from CommonModules.StockUpdate import Stock
from CommonModules.SortListofObj import sortObj

service=config('distributor_service')
now = datetime.now()

@api_view(['GET'])
def get_stock(request):
    if  (Authorization(request,service))==401:
        return HttpResponse('Request Denied', status=401)

    y=Stock(Authorization(request,service))
    y.updatefordistributor()
    main_obj=DistributorStock.objects.filter(distributor_id=Authorization(request,service))
    prod_head=['ProductID','ProductName','Quantity','Price/Unit']
    colors=['#5780c1','#34568b','#6a8ec8','#ff8a80','#ff5b4d','#ffb9b3','#adc982','#88b04b','#dce8c9','#783a6d','#cd98c3','#b565a7','#c1253c','#fbeaec']
    prod_data=[]
    graph_data=[]
    products=[]
    if main_obj.exists():
        for i in range(0,main_obj.count()):
            num=random.randint(0,13)
            data=[main_obj.values('product_id')[i]['product_id'],main_obj.values('product_name')[i]['product_name'],main_obj.values('product_quantity')[i]['product_quantity'],main_obj.values('price_per_product')[i]['price_per_product']]
            datas={
                "name":main_obj.values('product_name')[i]['product_name'],
                "id":main_obj.values('product_id')[i]['product_id']
            }
            details={
            "name":main_obj.values('product_name')[i]['product_name'],
            "quant":int(main_obj.values('product_quantity')[i]['product_quantity']),
            "color":colors[num],
            "legendFontColor": "#7F7F7F",
            "legendFontSize": 15
            }
            prod_data.append(data)
            graph_data.append(details)
            products.append(datas)
            
        sorted_data=sortObj(graph_data,'quant')
        return Response({"data":prod_data,"head":prod_head,"stock":sorted_data,"status":200,"products":products})
    else:
        return Response({"data":prod_data,"head":prod_head,"stock":graph_data,"status":200,"products":products})


@api_view(['GET'])
def receive_stock_history(request):
    if  (Authorization(request,service))==401:
        return HttpResponse('Request Denied', status=401)
    main_obj=DayByDayProductsDistribute.objects.filter(distributor_id=Authorization(request,service))
    prod_head=['Manufacturer','ProductID','ProductName','Quantity','date']
    prod_data=[]
    if main_obj.exists():
        for i in range(0,main_obj.count()):
            data=[ApprovedUsers.objects.filter(id_no=main_obj.values('manufacturer_id')[i]['manufacturer_id']).values('name')[0]['name'],main_obj.values('product_id')[i]['product_id'],SetProduct.objects.filter(Product_id=main_obj.values('product_id')[i]['product_id']).values('name')[0]['name'],main_obj.values('product_quantity')[i]['product_quantity'],main_obj.values('date')[i]['date']]
            prod_data.append(data)
        return Response({"data":prod_data,"head":prod_head,"status":200})
    else:
        return Response({"data":prod_data,"head":prod_head,"status":200})



@api_view(['POST'])
def distribute(request):
    if  (Authorization(request,service))==401:
        return HttpResponse('Request Denied', status=401)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    retailer_id=body['retailer_id']
    dist_id=Authorization(request,service)
    p_id=body['p_id']
    quant=body['quant']

    ##product##
    obj=SetProduct.objects.filter(Product_id=p_id)
    price=obj.values('price')[0]['price']

    ##stockOFThatProduct##
    obb=DistributorStock.objects.filter(distributor_id=dist_id)
    obb1=obb.filter(product_id=p_id)
    pre_stock=obb1.values('product_quantity')[0]['product_quantity']

    
    if(int(pre_stock)-int(quant)>=0):
        target_obj=DistributeToRetailer.objects.filter(distributor_id=dist_id).filter(retailer_id=retailer_id).filter(product_id=p_id)
        if target_obj.exists():
            try:
                quant_val=target_obj.values('product_quantity')[0]['product_quantity']
                target_obj.update(product_quantity=str(int(quant)+int(quant_val)))
                target_obj.update(total_price=str((int(pre_stock)-int(quant))*(int(price))))
                obb1.update(product_quantity=str(int(pre_stock)-int(quant)))
                obb1.update(total_price=str((int(pre_stock)-int(quant))*(int(price))))
                target_obj.update(calculation_status=False)
                y=Stock(retailer_id)
                y.updateforretailer()
                return Response({"msg":"Distributed","status":200})
            except:
                return Response({"msg":"error!","status":400})
        else:
            try:
                x=DistributeToRetailer(retailer_id=retailer_id,product_id=p_id,distributor_id=dist_id,product_quantity=quant,total_price=str(int(quant)*int(price)),calculation_status=False,date=date.today())
                x.save()
                obb1.update(product_quantity=str(int(pre_stock)-int(quant)))
                y=Stock(retailer_id)
                y.updateforretailer()
                return Response({"msg":"Distributed","status":200})
            except:
                return Response({"msg":"error!","status":400})
    else:
        return Response({"msg":"Stock Limit Exceed","status":400})




@api_view(['POST'])
def a_user(request):
    if  (Authorization(request,service))==401:
        return HttpResponse('Request Denied', status=401)
    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u_id=body['u_id']
    users=[]
    history=[]
    alls=ApprovedUsers.objects.filter(id_no=u_id)

    data={
        'name':alls.values('name')[0]['name'],
        'phone':alls.values('phone')[0]['phone'],
        'email':alls.values('email')[0]['email'],
        'gender':alls.values('gender')[0]['gender'],
        'whatsapp':alls.values('whatsapp_no')[0]['whatsapp_no'],
        'role':alls.values('role')[0]['role'],
        'id':alls.values('id_no')[0]['id_no'],
        }
    users.append(data)

    colors=['#5780c1','#34568b','#6a8ec8','#ff8a80','#ff5b4d','#ffb9b3','#adc982','#88b04b','#dce8c9','#783a6d','#cd98c3','#b565a7','#c1253c','#fbeaec']
    
    proObj=SetProduct.objects.all()
    dist_obj=DistributeToRetailer.objects.filter(retailer_id=u_id)
    my_obj=dist_obj.filter(distributor_id=Authorization(request,service))
    for i in range(0,my_obj.count()):
        num=random.randint(0,13)
        p_name=proObj.filter(Product_id=my_obj.values('product_id')[i]['product_id'])
        details={
            "name":p_name.values('name')[0]['name'],
            "quant":int(my_obj.values('product_quantity')[i]['product_quantity']),
            "color":colors[num],
            "legendFontColor": "#7F7F7F",
            "legendFontSize": 15
        }
        history.append(details)
       

    return Response({"user":users,"history":history})



@api_view(['POST'])
def post_dayBYdayDistribute(request):
    if  (Authorization(request,service))==401:
        return HttpResponse('Request Denied', status=401)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    retailer_id=body['retailer_id']
    dist_id=Authorization(request,service)
    p_id=body['p_id']
    quant=body['quant']

    obb=DistributorStock.objects.filter(distributor_id=dist_id)
    obb1=obb.filter(product_id=p_id)
    pre_stock=obb1.values('product_quantity')[0]['product_quantity']

    if(int(pre_stock)-int(quant)>=0):

        main_obj=DayByDayProductsDistributeToRetailer.objects.filter(product_id=p_id).filter(distributor_id=dist_id).filter(retailer_id=retailer_id).filter(date=date.today())
        if main_obj.exists():
            try:
                pre_quant=main_obj.values('product_quantity')[0]['product_quantity']
                main_obj.update(product_quantity=str(int(quant)+int(pre_quant)))
                return Response({"msg":"Distributed","status":200})
            except:
                return Response({"msg":"error","status":400})
        
        else:
            try:
                y=DayByDayProductsDistributeToRetailer(product_id=p_id,retailer_id=retailer_id,product_quantity=quant,distributor_id=dist_id,date=date.today())
                y.save()
                return Response({"msg":"Distributed","status":200})
            except:
                return Response({"msg":"error","status":400})

    else:
        return Response({"msg":"Stock Limit Exceed","status":400})



@api_view(['GET'])
def get_dayBYdayDistribute(request):
    if  (Authorization(request,service))==401:
        return HttpResponse('Request Denied', status=401)

    main_obj=DayByDayProductsDistributeToRetailer.objects.filter(distributor_id=Authorization(request,service))
    head=['Date','ProductID','ProductName','RetailerName','Quantity']
    tittle=[]
    data=[]
    if main_obj.exists():

        for i in range(0,main_obj.count()):
            a_tittle=[main_obj.values('date')[i]['date']]
            tittle.append(a_tittle)

            p_id=main_obj.values('product_id')[i]['product_id']
            p_name=SetProduct.objects.filter(Product_id=p_id).values('name')[0]['name']
            retailer_id=main_obj.values('retailer_id')[i]['retailer_id']
            retailer_name=ApprovedUsers.objects.filter(id_no=retailer_id).values('name')[0]['name']
            p_quant=main_obj.values('product_quantity')[i]['product_quantity']
            a_data=[main_obj.values('date')[i]['date'],p_id,p_name,retailer_name,p_quant]
            data.append(a_data)
        return Response({"head":head,"data":data,"tittle":tittle,"status":200})
    else:
        return Response({"head":head,"data":data,"tittle":tittle,"status":200})