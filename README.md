# read_csv_lambda

Execução:
  1. Criar novo lambda function
  
    1.1. Nas configurações personalizadas antes de criar o lambda adicionar VPN
  2. Baixar repositório do git
  
    2.1. Fazer zip dos arquivos
  3. Subir no lambda AWS arquivo zipado
  
    3.1. Realizar o Deploy e inserir no json teste os campos {"bucket_name": "bucket-read-csv", "object_key": "dados.csv"}
  4. Criar Bucket no S3 da forma padrão, não é necessário fazer configurações a mais
  
    4.1. Criar permissão do S3 no lambda
    
      4.1.1 Ir em confirações, ao abrir nova tela criar permissão, adicionar nova política, colocar o S3 como serviço, adicionar objeto Get_object e dar permissão no ARN
  5. Criar endpoint da VPC para dar autorização ao S3
  6. Criar RDS e instacia do banco dados MySQL
