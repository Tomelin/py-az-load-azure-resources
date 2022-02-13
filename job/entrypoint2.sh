#!/bin/sh


az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID > /dev/null 2>/dev/null 1>/dev/null
az account set --subscription $AZURE_SUBSCRIPTION_ID > /dev/null 2>/dev/null 1>/dev/null
RSC=$(az resource list -o json)
