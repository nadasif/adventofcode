pairs = {'BB': 'H',
         'BC': 'O',
         'BF': 'S',
         'BH': 'C',
         'BK': 'K',
         'BN': 'F',
         'BO': 'K',
         'BP': 'K',
         'BS': 'S',
         'BV': 'P',
         'CB': 'B',
         'CC': 'V',
         'CF': 'C',
         'CH': 'C',
         'CK': 'S',
         'CN': 'P',
         'CO': 'S',
         'CP': 'C',
         'CS': 'H',
         'CV': 'V',
         'FB': 'F',
         'FC': 'H',
         'FF': 'K',
         'FH': 'O',
         'FK': 'K',
         'FN': 'F',
         'FO': 'N',
         'FP': 'F',
         'FS': 'F',
         'FV': 'C',
         'HB': 'C',
         'HC': 'O',
         'HF': 'B',
         'HH': 'F',
         'HK': 'K',
         'HN': 'K',
         'HO': 'S',
         'HP': 'C',
         'HS': 'P',
         'HV': 'O',
         'KB': 'K',
         'KC': 'S',
         'KF': 'B',
         'KH': 'N',
         'KK': 'O',
         'KN': 'B',
         'KO': 'V',
         'KP': 'C',
         'KS': 'O',
         'KV': 'S',
         'NB': 'S',
         'NC': 'S',
         'NF': 'C',
         'NH': 'S',
         'NK': 'S',
         'NN': 'H',
         'NO': 'C',
         'NP': 'B',
         'NS': 'F',
         'NV': 'P',
         'OB': 'H',
         'OC': 'K',
         'OF': 'F',
         'OH': 'S',
         'OK': 'P',
         'ON': 'S',
         'OO': 'N',
         'OP': 'B',
         'OS': 'V',
         'OV': 'S',
         'PB': 'N',
         'PC': 'B',
         'PF': 'F',
         'PH': 'O',
         'PK': 'F',
         'PN': 'K',
         'PO': 'P',
         'PP': 'K',
         'PS': 'N',
         'PV': 'S',
         'SB': 'O',
         'SC': 'B',
         'SF': 'P',
         'SH': 'C',
         'SK': 'B',
         'SN': 'O',
         'SO': 'B',
         'SP': 'O',
         'SS': 'B',
         'SV': 'K',
         'VB': 'P',
         'VC': 'B',
         'VF': 'S',
         'VH': 'S',
         'VK': 'N',
         'VN': 'P',
         'VO': 'B',
         'VP': 'S',
         'VS': 'N',
         'VV': 'C'}
chain = "PBVHVOCOCFFNBCNCCBHK"

spairs = {
	'BB': 'N',
	'BC': 'B',
	'BH': 'H',
	'BN': 'B',
	'CB': 'H',
	'CC': 'N',
	'CH': 'B',
	'CN': 'C',
	'HB': 'C',
	'HC': 'B',
	'HH': 'N',
	'HN': 'C',
	'NB': 'B',
	'NC': 'B',
	'NH': 'C',
	'NN': 'C'}
schain = 'NNCB'
# PBVHVOCOCFFNBCNCCBHK


def inc(counts, key, t = 1):
	if key not in counts:
		counts[key] = 0
	counts[key] += t


def main():
	count = {}
	pCount1 = {}
	inc(count, chain[0])
	for j in range(1, len(chain)):
		inc(pCount1, chain[j - 1] + chain[j])
		inc(count, chain[j])

	itr = 40
	for i in range(itr):
		keys = list(filter(lambda p: pCount1[p] > 0, pCount1.keys()))
		pCount2 = {}
		# s = chain[0]
		for k in keys:
			l = k[0]
			r = k[1]
			c = pairs[k]
			n = pCount1[k]
			inc(pCount2, l + c, n)
			inc(pCount2, c + r, n)
			inc(count, c, n)
		pCount1 = pCount2
	sums = sorted(count.items(), key=lambda v: v[1])
	print(sums)
	hi = sums[len(sums)-1][1]
	lo = sums[0][1]
	print(f'{hi} - {lo} = {hi-lo}')
	
	

main()
