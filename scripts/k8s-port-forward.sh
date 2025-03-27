#!/bin/bash
POD=$(kubectl get pods -l app=backend -o jsonpath="{.items[0].metadata.name}")
kubectl port-forward pod/$POD 5000:5000