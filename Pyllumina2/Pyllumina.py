import multiprocessing
from FastaSequence import fasta_read
class Pyllumina:
    def __init__(self, 
                 KMER_Length = [90+i*10 for i in range(5)],
                 FirstReadFile = None,
                 SecondReadFile = None,
                 EmpiricalPEProbability = 100,
                 EmpiricalRead1Mid2End = None,
                 EmpiricalRead2Mid2End = None,
                 NumOfThreads = multiprocessing.cpu_count(),
                 FastaFile = None, 
                 ExpectedCoverage=30,
                 Mean = 100,
                 Sigma = 10,
                 FragmentDistribution = 'gaussian' #could be 'gaussian', 'uniform', or 'empirical'
                 ):
        self.SetFragmentDistribution(FragmentDistribution)
        self.SetMean(Mean)
        self.SetSigma(Sigma)
        self.SetFirstReadFile(FirstReadFile)
        self.SetSecondReadFile(SecondReadFile)
        self.SetEmpiricalPEProbability(EmpiricalPEProbability)
        self.SetEmpiricalRead1Mid2End(EmpiricalRead1Mid2End)
        self.SetEmpiricalRead2Mid2End(EmpiricalRead2Mid2End)
        self.SetNumOfThreads(NumOfThreads)
        self.SetFastaFile(FastaFile)
        self.SetKMER_Length(KMER_Length)
        self.SetExpectedCoverage(ExpectedCoverage)
        self.ComputeNumOfReads()
        self.CollectOptionalStatements()
        
    def SetFragmentDistribution(self, FD):
        self.FragmentDistribution = FD
    def SetMean(self,AVG):
        self.Mean = AVG
    def SetSigma(self,Sigma):
        self.Sigma = Sigma
    def SetExpectedCoverage(self,ExpectedCoverage):
        self.ExpectedCoverage = ExpectedCoverage
    def SetKMER_Length(self,KMER_Length):
        KMER_Length = KMER_Length
    def SetFirstReadFile(self,FirstReadFile):
        self.FirstReadFile = FirstReadFile
    def SetSecondReadFile(self,SecondReadFile):
        self.SecondReadFile = SecondReadFile
    def SetEmpiricalPEProbability(self,EmpiricalPEProbability):
        self.EmpiricalPEProbability = EmpiricalPEProbability
    def SetEmpiricalRead1Mid2End(self,EmpiricalRead1Mid2End):
        self.EmpiricalRead1Mid2End = EmpiricalRead1Mid2End
    def SetEmpiricalRead2Mid2End(self,EmpiricalRead2Mid2End):
        self.EmpiricalRead2Mid2End = EmpiricalRead2Mid2End
    def SetNumOfThreads(self,NumOfThreads):
        self.NumOfThreads = NumOfThreads
    def SetFastaFile(self,FastaFile):
        self.FastaFile = FastaFile
    def SetFastaSequence(self,Seq):
        self.FastaSequence = Seq
    
    def GetFragmentDistribution(self):
        return self.FragementDistribution
    def GetMean(self):
        return self.Mean
    def GetSigma(self):
        return self.Sigma
    def GetExpectedCoverage(self):
        return self.ExpectedCoverage
    def GetKMER_Length(self):
        return self.KMER_Length
    def GetFirstReadFile(self):
        return self.FirstReadFile
    def GetSecondReadFile(self):
        return self.SecondReadFile
    def GetEmpiricalPEProbability(self):
        return self.EmpiricalPEProbability
    def GetEmpiricalRead1Mid2End(self):
        return self.EmpiricalRead1Mid2End
    def GetEmpiricalRead2Mid2End(self):
        return self.EmpiricalRead2Mid2End
    def GetNumOfThreads(self):
        return self.NumOfThreads
    def GetFastaFile(self):
        return self.FastaFile
    def GetFastaSequence(self):
        return self.FastaSequence
    
    def ComputeNumOfReads(self):
        if type(self.GetFastaFile()) == str:
            FastaSeq = fasta_read(self.GetFastaFile())
            self.SetFastaSequence(FastaSeq)
            self.SetNumOfReads(FastaSeq[0].GetSeq())
        else:
            tempFastaSeq = list()
            for i in range(len(self.GetFastaFile())):
                FastaSeq = fasta_read(self.GetFastaFile()[i])
                tempFastaSeq.append(FastaSeq)
                self.SetFastaSequence(temp)
    def Build