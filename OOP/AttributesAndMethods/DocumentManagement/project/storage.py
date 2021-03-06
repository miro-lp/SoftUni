class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return "\n".join([str(d) for d in self.documents])

    def add_category(self, category):
        if category.id not in [c.id for c in self.categories]:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic.id not in [t.id for t in self.topics]:
            self.topics.append(topic)

    def add_document(self, document):
        if document.id not in [d.id for d in self.documents]:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category_change = [c for c in self.categories if c.id == category_id][0]
        category_change.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_change = [t for t in self.topics if t.id == topic_id][0]
        topic_change.topic = new_topic
        topic_change.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document_change = [d for d in self.documents if d.id == document_id][0]
        document_change.file_name = new_file_name

    def delete_category(self, category_id):
        category_delete = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(category_delete)

    def delete_topic(self, topic_id):
        topic_delete = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(topic_delete)

    def delete_document(self, document_id):
        document_delete = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(document_delete)

    def get_document(self, document_id):
        return [d for d in self.documents if d.id == document_id][0]



