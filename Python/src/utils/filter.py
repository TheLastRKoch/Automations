import jmespath


class UtilJMESpath:
    def filter(self, query_path, input_data):
        query = jmespath.compile(query_path)
        return query.search(input_data)
