apiVersion: v1
kind: Service
metadata:
  name: capstone-service
spec:
  selector:
    app: capstone
  ports:
  - protocol: TCP
    port: 6000
    targetPort: 5000
  type: LoadBalancer


---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: capstone
spec:
  selector:
    matchLabels:
      app: capstone
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  replicas: 3
  template:
    metadata:
      labels:
        app: capstone
    spec:
      containers:
      - name: capstone
        image: agilealchemy/capstone
        imagePullPolicy: Always
        ports:
        - containerPort: 5000
