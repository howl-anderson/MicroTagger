class Viterbi(object):
    def __init__(self, A, B, start_state='<start>', end_state='<end>'):
        self.A = A
        self.B = B

        self.start_state= start_state
        self.end_state = end_state

        self.trellis = {}

    def predict(self, word_list):
        N = len(word_list)
        trackback = {}

        all_states = self.A.keys() - {self.start_state}  # remove start_state

        # initialization step
        for state in all_states:
            self.trellis[state] = {}
            self.trellis[state][0] = self.A[self.start_state].get(state, 0) * self.B[state].get(word_list[0], 0)
            trackback[state] = {}
            trackback[state][0] = 0

        # recursion step
        for step in range(1, N):
            word = word_list[step]

            for state in all_states:
                # compute all previous path
                candidate_list = []
                for i in self.A.keys() - {self.start_state}:
                    candidate = self.trellis[i][step - 1] * self.A[i].get(state, 0) * self.B[state].get(word, 0)
                    candidate_list.append([i, candidate])

                sorted_candidate_list = sorted(candidate_list, key=lambda x: x[1])
                self.trellis[state][step] = sorted_candidate_list[0][1]

                trackback[state][step] = sorted_candidate_list[0][0]

        # termination step
        candidate_list = []
        for i in all_states:
            candidate = self.trellis[i][N-1] * self.A[i].get(self.end_state, 0)
            candidate_list.append([i, candidate])

        sorted_candidate_list = sorted(candidate_list, key=lambda x: x[1])

        self.trellis[self.end_state] = {}
        self.trellis[self.end_state][N-1] = sorted_candidate_list[0][1]

        trackback[self.end_state] = {}
        trackback[self.end_state][N-1] = sorted_candidate_list[0][0]

        pass


if __name__ == "__main__":
    A = {'<start>': {'A': 1.0}, 'C': {'<end>': 1.0}, 'A': {'B': 1.0}, 'B': {'C': 1.0}}
    B = {'C': {'人': 0.5, '中国人': 0.5}, 'A': {'你': 0.5, '我': 0.5}, 'B': {'是': 0.5, '打': 0.5}}
    viterbi = Viterbi(A, B)
    viterbi.predict("我 是 中国人")
