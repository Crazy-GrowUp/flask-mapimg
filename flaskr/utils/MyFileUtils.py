# ALLOWED_EXTENSIONS = {'.txt', '.pdf', '.png', '.jpg', '.jpeg', '.gif'}
def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           "." + filename.rsplit('.', 1)[1].lower() in allowed_extensions
