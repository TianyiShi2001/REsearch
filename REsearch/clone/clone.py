from Bio import Restriction, SeqIO
from Bio.Alphabet.IUPAC import IUPACUnambiguousDNA
from Bio.Restriction import Analysis, RestrictionBatch
from Bio.Seq import Seq

suppliers = dict(B='Life Technologies', C='Minotech Biotechnology', E='Agilent Technologies', I='SibEnzyme Ltd.', J='Nippon Gene Co., Ltd.', K='Takara Bio Inc.', M='Roche Applied Science', N='New England Biolabs',
                 O='Toyobo Biochemicals', Q='Molecular Biology Resources - CHIMERx', R='Promega Corporation', S='Sigma Chemical Corporation', V='Vivantis Technologies', X='EURx Ltd.', Y='SinaClon BioScience Co.')


def read_seq(filename):
    if not filename:
        return None
    ext = filename.rsplit('.')[1]
    parsers = {
        'dna': lambda f: SeqIO.read(f, 'snapgene').seq,
        'gb': lambda f: SeqIO.read(f, 'gb').seq,
        'fasta': lambda f: SeqIO.read(f, 'fasta').seq,
        'fa': lambda f: SeqIO.read(f, 'fasta').seq
    }
    return parsers[ext](filename)


def REsearch(goi='', goiFile='', mcs='', mcsFile=''):
    rb = RestrictionBatch(suppliers=['C', 'B', 'E', 'I', 'K', 'J', 'M', 'O', 'N', 'Q', 'S', 'R', 'V', 'Y', 'X'])

    goi = Seq(goi, IUPACUnambiguousDNA()) if goi else read_seq(goiFile)
    if not goi:
        raise Exception('Please provide a GOI sequence!')
    mcs = Seq(mcs, IUPACUnambiguousDNA()) if mcs else read_seq(mcsFile)
    if not mcs:
        raise Exception('Please provide a MCS sequence!')
    result_mcs = rb.search(mcs)
    result_goi = rb.search(goi)
    REs = set([e for e in result_mcs.keys() if result_mcs[e]]) - set([e for e in result_goi.keys() if result_goi[e]])

    # ana = Analysis(RestrictionBatch(list(REs)), mcs)

    # REs_sorted = sorted(REs, key=lambda e: result_mcs[e])

    # result = {e: result_mcs[e] for e in REs_sorted}

    r = []
    for e in REs:
        for site in result_mcs[e]:
            r.append((str(e), site, "blunt" if e.is_blunt() else e.elucidate(), ' '.join(e.suppl)))

    r.sort(key=lambda i: i[1])

    return r


def html_format(REs):
    return  # [f'{str(e):<10s} { "blunt" if e.is_blunt() else e.elucidate()}' for e in REs]


if __name__ == "__main__":
    goiFile = '/Users/tianyishi/Documents/GitHub/ox/content/tutorial/resources/wrn/in-silico-cloning/original.dna'  # input('GOI file? ')
    goi = 'CGATCTACCATCTACTCGCCCGGGATCTGTGAATGAGGAATTACCAGAAACCGAACCCGAAGATAATGATGAGTTGCCTGAAACAGAACCTGAAAGCGATTCCGATAAACCTACCGTAACCTCGAATAAAACAGAAAACCAAGTTGCTGATGAAGATTATGATTCATTCGACGATTTTGTGCCCAGTCAAACACACACAGCCTCCAAAATACCTGTAAAAAATAAACGAGCCAAAAAGTGCACTGTAGAATCTGATTCATCATCTTCGGATGATT'
    mcs = 'gagaccacaacggtttccctctagaaataattttgtttaactttaagaaggagatataccatggcacatatgagcggccgcgtcgactcgagcgagctcccggggggggttct'  # input('MCS? ')

    print(REsearch(mcs=mcs, goiFile=goiFile))
