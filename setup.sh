docker stop fazla_case_container
docker rm fazla_case_container
docker build -t fazla_case .
docker run -d --name fazla_case_container -p 5000:5000 fazla_case