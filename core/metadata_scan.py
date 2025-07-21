import exifread

def scan_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f)
        return {tag: str(value) for tag, value in tags.items()}
    except Exception as e:
        return {"Error": str(e)}
