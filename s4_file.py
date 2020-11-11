
import uuid

#creating a bucket aws s3

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region
            }
            )
    print (bucket_name, current_region)
    return bucket_name, bucket_response
    
    #create first bucket
#first_bucket_name, first_response = create_bucket(
#...     bucket_prefix='firstpythonbucket', 
#...     s3_connection=s3_resource.meta.client)

#naming files

def create_temp_file(size, file_name, file_content):
	random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
	with open(random_file_name, 'w') as f:
		f.write(str(file_content) * size)
	return random_file_name
	
#create first file
# first_file_name = create_temp_file(300, 'firstfile.txt', 'f')   
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
