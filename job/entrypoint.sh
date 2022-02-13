#!/bin/sh


if [[ -z "${AZURE_SUBSCRIPTION_ID}" ]]; then
  echo "Some default value because AZURE_SUBSCRIPTION_ID is undefined"
  exitt 1
fi

if [[ -z "${AZURE_TENANT_ID}" ]]; then
  echo "Some default value because AZURE_TENANT_ID is undefined"
  exitt 1
fi

if [[ -z "${AZURE_CLIENT_ID}" ]]; then
  echo "Some default value because AZURE_CLIENT_ID is undefined"
  exitt 1
fi

if [[ -z "${AZURE_CLIENT_SECRET}" ]]; then
  echo "Some default value because AZURE_CLIENT_SECRET is undefined"
  exitt 1
fi

az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
az account set --subscription $AZURE_SUBSCRIPTION_ID
az resource list -o json

while :
do
	echo "Do something; hit [CTRL+C] to stop!"
done
