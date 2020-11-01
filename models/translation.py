
class TranslationModel:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def metadata(self):
        return self.dictionary['metadata']

    def content_data(self):
        return self.dictionary['content_data']

    def language(self):
        return self.dictionary['language']

    def draft_by(self):
        return self.dictionary['draft_by']

    def slug(self):
        return self.dictionary['slug']

    def permalink(self):
        return self.dictionary['permalink']

    def created_by(self):
        return self.dictionary['created_by']

    def allowed_children(self):
        return self.dictionary['allowed_children']

    def title(self):
        return self.dictionary['title']

    def is_published(self):
        return self.dictionary['is_published']

    def file(self):
        return self.dictionary['file']
