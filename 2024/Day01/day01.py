class Day01():
    def total_list_diffs(self, list_one, list_two):
        list_one.sort()
        list_two.sort()

        total = 0
        for i in range(len(list_one)):
            total += abs(list_one[i] - list_two[i])

        return total

    def calc_similarity_score(self, list_one, list_two):
        similarity_score = 0

        full_list_counts_dict = self.__create_dict(list_one, list_two)
        full_list_counts_dict = self.__convert_to_dict_counts(full_list_counts_dict, list_two)

        for item in list_one:
            similarity_score += item * full_list_counts_dict[item]

        return similarity_score

    @staticmethod
    def __convert_to_dict_counts(full_item_counts, items) -> dict:
        # dict_of_counts = {item: 0 for item in items}

        for item in items:
            full_item_counts[item] += 1

        return full_item_counts


    @staticmethod
    def __create_dict( list_one, list_two) -> dict:
        full_set_of_lists = set(list_one)
        full_set_of_lists.update(list_two)
        return {item: 0 for item in full_set_of_lists}
