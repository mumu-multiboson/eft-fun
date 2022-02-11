void rescale(const char *input, const char *output, float xsec, float lumi)
{
    TFile *input_file = new TFile(input);
    TFile *output_file = new TFile(output, "RECREATE");
    TH1D *h, *h2;
    TKey *key;
    TIter next( input_file->GetListOfKeys());
    int i = 0;
    while ((key = (TKey *) next())) {
        h = (TH1D *)input_file->Get(key->GetName()); // copy object to memory
        h2 = (TH1D *)h->Clone();
        h2->Scale(lumi * xsec);
        h2->Write();
    }

}