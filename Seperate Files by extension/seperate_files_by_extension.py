def content_file_name(instance, filename):
    name, ext = os.path.splitext(filename)
    ext = ext.lstrip("FOLDER NAME")# Remove leading dot
    if filename.endswith("jpg") or filename.endswith("jpeg"):
         subdir = "phots"
    elif filename.endswith("txt") or filename.endswith("asc"):
         subdir = "docs"
    else:
        subdir = extension
    upload_dir = os.path.join('uploads', 'resource', subdir)
    return os.path.join(upload_dir, filename)