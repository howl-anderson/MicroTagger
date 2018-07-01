from tqdm import tqdm

from tool import dataType

trainLines = 10000
testLines = 1

data = dataType()

from hmm import HMMTagger

hmm_tagger = HMMTagger()

tqdm.write("Training start!")
for i in tqdm(range(trainLines)):
    line = data.getTrainLine()
    hmm_tagger.train_one_line(line)

result = hmm_tagger.predict("19980117-03-001-002  新华社  圣马力诺  １月  １６日  电  〓  （  记者  袁  锦林  ）  圣马力诺  执政官  路易吉·马扎  和  马里诺·扎诺蒂  １６日  上午  举行  仪式  ，  热烈  欢迎  [中国  国务院  副  总理  兼  外交部长  钱  其琛  访问  圣马力诺  。")
"""
19980117-03-001-002/m  新华社/nt  圣马力诺/ns  １月/t  １６日/t  电/n  〓/w  （/wkz  记者/n  袁/nrf  锦林/nrg  ）/wky  圣马力诺/ns  执政官/n  路易吉·马扎/nr  和/c  马里诺·扎诺蒂/nr  １６日/t  上午/t  举行/vt  仪式/n  ，/wd  热烈/ad  欢迎/vt  [中国/ns  国务院/nt]nt  副/b  总理/n  兼/vt  外交部长/n  钱/nrf  其琛/nrg  访问/vt  圣马力诺/ns  。/wj

19980117-03-001-002/m  新华社/nt  圣马力诺/ns  １月/t  １６日/t  电/n  〓/w  （/wkz  记者/n  袁/nrf  锦林/nrg  ）/wky  圣马力诺/ns  执政官/n  路易吉·马扎/wd  和/c  马里诺·扎诺蒂/p  １６日/t  上午/t  举行/vt  仪式/n  ，/wd  热烈/ad  欢迎/vt  [中国/ns  国务院/nt]nt  副/b  总理/n  兼/vt  外交部长/n  钱/nrf  其琛/nrg  访问/vt  圣马力诺/ns  。/wj
19980117-03-001-002/unknow  新华社/nt  圣马力诺/ns  １月/t  １６日/t  电/n  〓/w  （/wkz  记者/n  袁/nrf  锦林/nrg  ）/wky  圣马力诺/ns  执政官/unknow  路易吉·马扎/unknow  和/c  马里诺·扎诺蒂/unknow  １６日/t  上午/t  举行/vt  仪式/n  ，/wd  热烈/a  欢迎/vt  [中国/ns  国务院/nt  副/b  总理/n  兼/vt  外交部长/n  钱/n  其琛/nrg  访问/vt  圣马力诺/ns  。/wj
"""

"""
++ > previous_path_probability  transition_probability   state_observation_likelihood
ud -37.580809668585204          -2.8017642113737127      -9.23815007261545
ns -37.580809668585204          -3.4436180975461075      -8.466811761855313
"""
print(result)
