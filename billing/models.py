from django.db import models
from django.shortcuts import reverse
import datetime


# Create your models here.



class Debtor(models.Model):
    
    aadharnumber = models.CharField(max_length=100,unique=True,error_messages={'unique':"*Aadhar Number is already exists."})
    mobilenumber = models.CharField(max_length=10,unique=True,error_messages={'unique':"*Phone Number is already exists."})
    profile = models.ImageField(upload_to='media/',default= 'profile.png')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    user_id = models.CharField(max_length=500, blank=True)
    pancard = models.CharField(max_length=100,unique=True,error_messages={'unique':"*Pan Number is already exists."})
    rationcard = models.CharField(max_length=100,unique=True,error_messages={'unique':"*Ration Card Number is already exists."})
    address = models.TextField(max_length=1000, null=True)
    email = models.EmailField(unique=True,error_messages={'unique':"*Email Id is already taken."}, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)

    @property
    def full_name(self):
        return f" {self.first_name} {self.last_name}"


    def __str__(self):
        return f" {self.first_name} {self.last_name} Debt"

class Documents(models.Model):
    debtor = models.ForeignKey("Debtor",on_delete=models.CASCADE)
    passbook = models.BooleanField(default=False)
    bond = models.BooleanField(default=False)
    deed = models.BooleanField(default=False)
    checkleaf = models.BooleanField(default=False)
    checkleafcount = models.CharField(default=0, blank=True, null=True, max_length=50)
    additionaldocuments = models.BooleanField(default=False)
    additionaldocumentsname = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    totalamount = models.IntegerField(default=0, blank=True, null=True)
    percentage = models.CharField(max_length=100,blank=True)
    docno = models.CharField(max_length=100,blank=True)
    duedate = models.DateTimeField(auto_now_add=False,auto_now=False,null=True)
    intamount = models.IntegerField(default=0, blank=True, null=True)
    pendingdate = models.CharField(max_length=100,blank=True)
    reason = models.CharField(max_length=100,blank=True)
    fineamount = models.CharField(max_length=100,blank=True)
    result = models.CharField(max_length=100,blank=True,null=True )
    paid = models.BooleanField(default=False)
    balanceamount = models.IntegerField(default=0, blank=True, null=True)
    paidamount = models.IntegerField(default=0, blank=True, null=True)
   
    @property
    def due(self):
        da = self.created_at.date
        to = datetime.date.today()
        due_date = da.replace(
            month = to.month + 1,
            day = da.day
            )
        return due_date
    print(duedate)


    def __str__(self):
        return f" {self.debtor}  Documents"

class DocumentImage(models.Model):
    document = models.ForeignKey("Documents",on_delete=models.CASCADE)
    file = models.FileField(upload_to='mydocs/')

    def __str__(self):
        return f" {self.document}  Images"

class IntrestAmount(models.Model):
    amount = models.ForeignKey("Documents",on_delete=models.CASCADE)
    intrestamount = models.IntegerField(default=0, blank=True, null=True)
    pendingdate = models.CharField(max_length=100,blank=True)
    reason = models.CharField(max_length=100,blank=True)
    fineamount = models.CharField(max_length=100,blank=True)
    result = models.CharField(max_length=100,blank=True)
    paid = models.BooleanField(default=False)
    duedate = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    

    def __str__(self):
        return f" {self.amount} Amount"

class DocumentAmount(models.Model):
    debtor = models.ForeignKey("Documents",on_delete=models.CASCADE)
    totalamount = models.IntegerField(default=0, blank=True, null=True)
    percentage = models.CharField(max_length=100,blank=True,null=True)
    paidamount = models.IntegerField(default=0, blank=True, null=True)
    balanceamount = models.IntegerField(default=0, blank=True, null=True)
    result = models.CharField(max_length=100,blank=True,null=True)
    duedate = models.CharField(max_length=100,blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    pendingdate = models.CharField(max_length=100,blank=True,null=True)
    reason = models.CharField(max_length=100,blank=True,null=True)
    fineamount = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return f" {self.debtor} DocumentAmount"


class PaidUnpaid(models.Model):
    debtor = models.ForeignKey("Documents",on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    duedate = models.DateTimeField(auto_now_add=False,auto_now=False,null=True)
    
    def __str__(self):
        return f" {self.debtor} IntrestAmount Paid"





# from rest_framework import serializers

# class DocumentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Documents
#         fields = "__all__"