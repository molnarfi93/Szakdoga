class Class:

    @staticmethod
    def load_classes(json_path):
        """
        """
        classes = []
        with open(json_path) as json_file:
            classes_data = json.load(json_file)['classes']
        for class_name, class_data in classes_data.items():
            c = Class.create_class_from_dict(class_name, class_data)
            classes.append(c)
        return classes

    def __init__(self, name, grade, subject, type, weekly_periods, headcount, no):
        self.name = name
        self.grade = grade
        self.subjects = []
        self.headcount = headcount

        self.type = type
        self.weekly_periods = weekly_periods
        self.sum_periods = 0
        self.room = ""
        self.teacher = ""
        self.no = no

    @staticmethod
    def create_class_from_dict(name, d):
        """
        Create a new class instance from dictionary data.
        :param name: name of the class
        :param d: dictionary
        :return: a class instance
        """
        new_class = Class(name, d['grade'], d['headcount'])
        for subject_name, subject_data in d['subjects'].items():
            subject = create_subject_from_dict(subject_name, subject_data)
            new_class._subjects.append(subject)


classes = Class.load_classes('osztalyok.json')

