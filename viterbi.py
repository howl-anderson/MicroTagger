import operator
import functools


class Viterbi(object):
    def __init__(self, A, B, start_state='<start>', end_state='<end>'):
        self.A = A
        self.B = B

        self.start_state= start_state
        self.end_state = end_state

        self.trellis = {}

    def _do_predict(self, word_list):
        N = len(word_list)
        T = N - 1
        trackback = {}

        all_states = self.A.keys() - {self.start_state}  # remove start_state

        # initialization step
        for state in all_states:
            self.trellis[state] = {}
            self.trellis[state][0] = self.A[self.start_state].get(state, 0) * self.B[state].get(word_list[0], 0)
            trackback[state] = {}
            trackback[state][0] = self.start_state

        # recursion step
        for step in range(1, N):
            word = word_list[step]

            for state in all_states:
                # compute all previous path
                candidate_list = []
                for i in all_states:
                    previous_path_probability = self.trellis[i][step - 1]
                    transition_probability = self.A[i].get(state, 0)
                    state_observation_likelihood = self.B[state].get(word, 0)

                    candidate = previous_path_probability * transition_probability * state_observation_likelihood
                    candidate_list.append([i, candidate])

                sorted_candidate_list = sorted(candidate_list, key=lambda x: x[1],
                                               reverse=True)  # NOTE: descending sort by reverse = True
                self.trellis[state][step] = sorted_candidate_list[0][1]

                trackback[state][step] = sorted_candidate_list[0][0]

        # termination step
        candidate_list = []
        for i in all_states:
            candidate = self.trellis[i][N-1] * self.A[i].get(self.end_state, 0)
            candidate_list.append([i, candidate])

        sorted_candidate_list = sorted(candidate_list, key=lambda x: x[1],
                                       reverse=True)  # NOTE: descending sort by reverse = True)

        self.trellis[self.end_state] = {}
        self.trellis[self.end_state][N-1] = sorted_candidate_list[0][1]

        trackback[self.end_state] = {}
        trackback[self.end_state][N-1] = sorted_candidate_list[0][0]

        return trackback

    def predict_state(self, word_list):
        traceback = self._do_predict(word_list)

        N = len(word_list)
        T = N - 1

        reverse_state_sequence = []

        reverse_state_sequence.append(self.end_state)

        state = traceback[self.end_state][T]
        reverse_state_sequence.append(state)

        previous_state = state

        reverse_step = reversed(range(len(word_list)))
        for step in reverse_step:
            state = traceback[previous_state][step]
            reverse_state_sequence.append(state)

            previous_state = state

        return list(reversed(reverse_state_sequence))


if __name__ == "__main__":
    A = {'<start>': {'A': 1.0}, 'C': {'<end>': 1.0}, 'A': {'B': 1.0}, 'B': {'C': 1.0}}
    B = {'C': {'人': 0.5, '中国人': 0.5}, 'A': {'你': 0.5, '我': 0.5}, 'B': {'是': 0.5, '打': 0.5}}
    viterbi = Viterbi(A, B)
    viterbi._do_predict(["我", "是", "中国人"])

    state_sequence = viterbi.predict_state(["我", "是", "中国人"])
    print(state_sequence)
