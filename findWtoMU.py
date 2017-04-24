from ROOT import * 
import  math, sys

#f = TFile.Open("OutTree.root", "read")
f = TFile.Open("root://cmsxrootd.fnal.gov//store/user/ra2tau/jan2017tuple/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJetsToLNu_HT-0To70_v1_RunIISummer16MiniAODv2/170207_145404/0000/OutTree_100.root", "read")
td = f.Get("TNT")
BOOM = td.Get("BOOM")

TH1F_MuonFromW_eta = TH1F("TH1F_MuonFromW_eta", "#mu #eta;#eta; count", 100, -2.7, 2.7)

c1 = TCanvas()


#print BOOM.Print()

#BOOM.Draw("Gen_eta", "abs(Gen_eta) < 2.7 && abs(Gen_motherpdg_id) == 24.0 &&abs(Gen_pdg_id) == 13.0")
#c1.SaveAs("TH1F_MuonFromW_eta.png")

for counter, event in enumerate(BOOM):
	for counter, particle in enumerate(event.Gen_motherpdg_id):
		# particle
		if abs(int(particle)) == 24 and abs(int(event.Gen_pdg_id[counter])) == 13:
			print particle, event.Gen_pdg_id[counter]
			TH1F_MuonFromW_eta.Fill(event.Gen_eta[counter])
		#for counter, particle in enumerate(event.Gen_motherpdg_id):



TH1F_MuonFromW_eta.Draw()
c1.SaveAs("TH1F_MuonFromW_eta.png")




##[rmueller@cmslpc29 src]$ root -l root://cmsxrootd.fnal.gov//store/user/ra2tau/jan2017tuple/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJetsToLNu_HT-0To70_v1_RunIISummer16MiniAODv2/170207_145404/0000/OutTree_100.root
##root [0]
##Attaching file root://cmsxrootd.fnal.gov//store/user/ra2tau/jan2017tuple/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/WJetsToLNu_HT-0To70_v1_RunIISummer16MiniAODv2/170207_145404/0000/OutTree_100.root as _file0...
##(TFile *) 0x29d0fe0
##root [1] TNT->cd()
##(Bool_t) true
##root [2] BOOM->Draw("Gen_eta", "abs(Gen_eta) < 2.7 && abs(Gen_motherpdg_id) == 24.0 &&abs(Gen_pdg_id) == 13.0")
##Info in <TCanvas::MakeDefCanvas>:  created default TCanvas with name c1
##(Long64_t) 17018
##root [3]