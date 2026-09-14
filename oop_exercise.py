from turtledemo.penrose import start

#TASK1

class GenomicFeature:
    def __init__(self, chromosome, start, end, strand):
        # defining value errors
        if not isinstance(chromosome, str):
            raise ValueError("Chromosome must be a string")
        if not isinstance(start, int) or not isinstance(end, int) or start <= 0 or end <=0:
            raise ValueError("Start and end must be a positive integer")
        if start > end:
            raise ValueError("Start value must not be bigger than end value")
        if strand not in ("+", "-"):
            raise ValueError("Strand must be + or -")

        #storing all values as instance attributes
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.strand = strand

#example = GenomicFeature('chr1', 1, 20, '-')

    def length(self) -> int:
        return self.end - self.start + 1

    def overlaps(self, other: 'GenomicFeature') -> bool:
        if self.chromosome != other.chromosome:
            return False
        return max(self.start, other.start) <= min(self.end, other.end)

    def describe(self) -> str:
        return f"{type(self).__name__} {self.chromosome}:{self.start}-{self.end}({self.strand})"

if __name__ == "__main__":
    a = GenomicFeature("chr1", 1000, 5000, "+")
    b = GenomicFeature("chr1", 4800, 6000, "+")
    c = GenomicFeature("chr2", 1000, 5000, "+")

#testing
#print(a.describe())      # GenomicFeature chr1:1000-5000(+)
#print(a.length())        # 4001
#print(a.overlaps(b))     # True  (4800-5000 shared)
#print(a.overlaps(c))     #false
#GenomicFeature("chr1", 5000, 1000, "+")

class Exon(GenomicFeature):
    def __init__(self, chromosome, start, end, strand, exon_number):
        super().__init__(chromosome, start, end, strand)
        self.exon_number = exon_number

    def add_exon(self, exon):

    def total_exon_length(self):

    def describe(self) -> str:
        return f"{type(self).__name__} {self.chromosome}:{self.start}-{self.end}({self.strand}) exon#{self.exon_number}"


features = [
    GenomicFeature("chr1", 1000, 5000, "+"),
    Exon("chr1", 1000, 1200, "+", 1),
    Exon("chr1", 3000, 3300, "+", 2),
]

for feature in features:
    print(feature.describe())

