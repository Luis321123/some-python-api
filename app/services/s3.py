import logging

from app.core.bucket_s3 import s3, s3_resource

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class S3Service:
    def __init__(self):
        self.s3_client = s3
        self.s3_resource = s3_resource

    async def upload_file(self, file, bucket_name, folder_name, file_name):
        try:
           key = f"{folder_name}/{file_name}"
           self.s3_client.upload_fileobj(file, bucket_name, key)
        except Exception as ex:
            logger.error(f"Unexpected Error: {ex}")
            return False
        return True

    def get_all_files(self, bucket_name):
        try:
            files = self.s3_client.list_objects_v2(Bucket=bucket_name)
            return files
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            return False
        
    def download_file(self, file_name: str, bucket_name: str):
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params = {'Bucket': bucket_name, 'Key': file_name},
                ExpiresIn = 3600000
            )
            return url
        except Exception as ex:
            logger.error(f"Unexpected Error: {ex}")
            raise ex