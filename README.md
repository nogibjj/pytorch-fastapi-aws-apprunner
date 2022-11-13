## FastAPI PyTorch Example

Converted from [official tutorial](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html)

Tasks:

1.  Run the fastapi app:  `python app.py`
2.  Upload an image to classify, say a cat using the swagger docs url:  /docs
3.  Deploy to AWS using the free tier and the AWS App Runner service

## Notes on Running docker with PyTorch and FastAPI
`docker build .`

Note this is your container name use:  `docker image ls` to find (replace id with your image id):

`docker run -p 127.0.0.1:8080:8080 54a55841624f`

![fastapi-step1](https://user-images.githubusercontent.com/58792/131587003-f5667c28-7cbe-402e-8795-f32a6ca9a4d1.png)
![fastapi-step2](https://user-images.githubusercontent.com/58792/131587286-341e795c-76dc-46a1-8ee9-528134410935.png)
![fastapi-step3](https://user-images.githubusercontent.com/58792/131587004-198ad6d5-2197-4de5-a6dd-4eb3c41e675e.png)
![fastapi-step4](https://user-images.githubusercontent.com/58792/131587005-866b0974-63d7-4fed-abf2-9c634721669f.png)


## Verify Swagger Working


Go to /docs url


### References

* [Watch PyTorch walkthrough on YouTube](https://www.youtube.com/watch?v=-CoOotWG30E)
* [Watch GitHub Universe Talk:  Teaching MLOps at scale with Github](https://watch.githubuniverse.com/on-demand/ec17cbb3-0a89-4764-90a5-9debb58515f8)
* [Building Cloud Computing Solutions at Scale Specialization](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale)
* [Python, Bash and SQL Essentials for Data Engineering Specialization](https://www.coursera.org/learn/web-app-command-line-tools-for-data-engineering-duke)
* [Implementing MLOps in the Enterprise](https://learning.oreilly.com/library/view/implementing-mlops-in/9781098136574/)
* [Practical MLOps: Operationalizing Machine Learning Models](https://www.amazon.com/Practical-MLOps-Operationalizing-Machine-Learning/dp/1098103017)
* [Coursera-Dockerfile](https://gist.github.com/noahgift/82a34d56f0a8f347865baaa685d5e98d)
