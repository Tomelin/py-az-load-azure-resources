#!/bin/sh


if [[ -z "${AZURE_SUBSCRIPTION_ID}" ]]; then
  echo "Some default value because AZURE_SUBSCRIPTION_ID is undefined"
  exit 1
fi

if [[ -z "${AZURE_TENANT_ID}" ]]; then
  echo "Some default value because AZURE_TENANT_ID is undefined"
  exit 1
fi

if [[ -z "${AZURE_CLIENT_ID}" ]]; then
  echo "Some default value because AZURE_CLIENT_ID is undefined"
  exit 1
fi

if [[ -z "${AZURE_CLIENT_SECRET}" ]]; then
  echo "Some default value because AZURE_CLIENT_SECRET is undefined"
  exit 1
fi

python job.py
