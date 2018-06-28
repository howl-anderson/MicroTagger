class HMMTagger(object):
    def __init__(self):
        self.A = {}
        self.B = {}

        self.state_count = {}  # count of each state
        self.state_bigram = {}  # count of (State_{t} | State_{t-1})

        self.state_obsevation_pair = {}  # count of pair state and emission observation

    def train_one_line(self, line):
        previous_tag = None
        for word_pinyin_tag in line.split():
            # extract
            word_pinyin, tag = word_pinyin_tag.split('/')
            word, pinyin_with_tail = word_pinyin.split('{')
            pinyin = pinyin_with_tail[:-1]

            # compute
            # compute transition count
            if previous_tag is not None:
                # compute bigram count
                self._state_bigram_increase_one(previous_tag, tag)

                # compute state count
                self._tag_count_increase_one(previous_tag)

            # update current as previous_tag
            previous_tag = tag

            # compute emission count
            self._state_observation_pair_increase_one(tag, word)

        # process last tag
        # NOTE:
        # when program execute to here: previous_tag is last tag, because it was assigned in the end of compute loop
        self._tag_count_increase_one(previous_tag)

    def _state_bigram_increase_one(self, previous_tag, tag):
        if previous_tag not in self.state_bigram:
            self.state_bigram[previous_tag] = {}

        tag_state_bigram = self.state_bigram[previous_tag]

        bigram = (previous_tag, tag)

        if bigram not in tag_state_bigram:
            tag_state_bigram[bigram] = 0

        tag_state_bigram[bigram] = tag_state_bigram[bigram] + 1

    def _tag_count_increase_one(self, tag):
        # compute state count
        if tag not in self.state_count:
            self.state_count[tag] = 0

        tag_state_count = self.state_count[tag]

        self.state_count[tag] = tag_state_count + 1

    def _do_train(self):
        for previous_state, previous_state_count in self.state_count.items():
            # compute transition probability

            # NOTE: using dict.get() to prevent no such dict key AKA no such bigram pair
            bigram_local_storage = self.state_bigram.get(previous_tag, {})
            for bigram, bigram_count in bigram_local_storage:
                bigram_probability = bigram_count / previous_state_count

                state = bigram[1]

                if previous_state not in self.A:
                    self.A[previous_state] = {}

                self.A[previous_state][state] = bigram_probability

            # compute emission probability
            emission_local_storage = self.state_obsevation_pair[previous_state]
            for word, word_count in emission_local_storage.items():
                if previous_state not in self.B:
                    self.B[previous_state] = {}

                self.B[previous_state][word] = word_count / previous_state_count

    def predict(self, line):
        if not self.A:  # using self.A as an training-flag indicate if already trained.
            self._do_train()

        word = [i.strip() for i in line.split()]

        # TODO: apply Viterbi algorithms to here
        pass

    def _state_observation_pair_increase_one(self, tag, word):
        if tag not in self.state_obsevation_pair:
            self.state_obsevation_pair[tag] = {}

        if word not in self.state_obsevation_pair[tag]:
            self.state_obsevation_pair[tag][word] = 0

        self.state_obsevation_pair[tag][word] = self.state_obsevation_pair[tag][word] + 1