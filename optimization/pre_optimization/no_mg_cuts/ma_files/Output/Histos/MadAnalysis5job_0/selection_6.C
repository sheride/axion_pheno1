void selection_6()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo13","canvas_plotflow_tempo13",0,0,700,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S7_DELTAR_0 = new TH1F("S7_DELTAR_0","S7_DELTAR_0",75,0.0,15.0);
  // Content
  S7_DELTAR_0->SetBinContent(0,0.0); // underflow
  S7_DELTAR_0->SetBinContent(1,0.0);
  S7_DELTAR_0->SetBinContent(2,0.0);
  S7_DELTAR_0->SetBinContent(3,484.178825215);
  S7_DELTAR_0->SetBinContent(4,820.589242735);
  S7_DELTAR_0->SetBinContent(5,955.782049776);
  S7_DELTAR_0->SetBinContent(6,1251.31966517);
  S7_DELTAR_0->SetBinContent(7,1251.31966517);
  S7_DELTAR_0->SetBinContent(8,1458.82487597);
  S7_DELTAR_0->SetBinContent(9,1795.23529349);
  S7_DELTAR_0->SetBinContent(10,1983.87650332);
  S7_DELTAR_0->SetBinContent(11,1927.28410037);
  S7_DELTAR_0->SetBinContent(12,2049.90090676);
  S7_DELTAR_0->SetBinContent(13,2449.19132755);
  S7_DELTAR_0->SetBinContent(14,2914.50615178);
  S7_DELTAR_0->SetBinContent(15,3159.73976456);
  S7_DELTAR_0->SetBinContent(16,3175.45976537);
  S7_DELTAR_0->SetBinContent(17,1729.21089006);
  S7_DELTAR_0->SetBinContent(18,987.222051413);
  S7_DELTAR_0->SetBinContent(19,710.548437004);
  S7_DELTAR_0->SetBinContent(20,525.051227344);
  S7_DELTAR_0->SetBinContent(21,342.698137847);
  S7_DELTAR_0->SetBinContent(22,260.95361359);
  S7_DELTAR_0->SetBinContent(23,216.937331298);
  S7_DELTAR_0->SetBinContent(24,166.633048678);
  S7_DELTAR_0->SetBinContent(25,141.480887368);
  S7_DELTAR_0->SetBinContent(26,97.4646050758);
  S7_DELTAR_0->SetBinContent(27,103.752645403);
  S7_DELTAR_0->SetBinContent(28,84.8885244209);
  S7_DELTAR_0->SetBinContent(29,69.1684436022);
  S7_DELTAR_0->SetBinContent(30,66.0244034385);
  S7_DELTAR_0->SetBinContent(31,31.4401936374);
  S7_DELTAR_0->SetBinContent(32,34.5842138011);
  S7_DELTAR_0->SetBinContent(33,37.7282339648);
  S7_DELTAR_0->SetBinContent(34,40.8722421286);
  S7_DELTAR_0->SetBinContent(35,44.0162822923);
  S7_DELTAR_0->SetBinContent(36,15.7200968187);
  S7_DELTAR_0->SetBinContent(37,22.0081371462);
  S7_DELTAR_0->SetBinContent(38,9.43206049121);
  S7_DELTAR_0->SetBinContent(39,0.0);
  S7_DELTAR_0->SetBinContent(40,0.0);
  S7_DELTAR_0->SetBinContent(41,12.5760766549);
  S7_DELTAR_0->SetBinContent(42,6.28804032747);
  S7_DELTAR_0->SetBinContent(43,0.0);
  S7_DELTAR_0->SetBinContent(44,0.0);
  S7_DELTAR_0->SetBinContent(45,0.0);
  S7_DELTAR_0->SetBinContent(46,0.0);
  S7_DELTAR_0->SetBinContent(47,3.14401936374);
  S7_DELTAR_0->SetBinContent(48,0.0);
  S7_DELTAR_0->SetBinContent(49,0.0);
  S7_DELTAR_0->SetBinContent(50,0.0);
  S7_DELTAR_0->SetBinContent(51,0.0);
  S7_DELTAR_0->SetBinContent(52,0.0);
  S7_DELTAR_0->SetBinContent(53,0.0);
  S7_DELTAR_0->SetBinContent(54,0.0);
  S7_DELTAR_0->SetBinContent(55,0.0);
  S7_DELTAR_0->SetBinContent(56,0.0);
  S7_DELTAR_0->SetBinContent(57,0.0);
  S7_DELTAR_0->SetBinContent(58,0.0);
  S7_DELTAR_0->SetBinContent(59,0.0);
  S7_DELTAR_0->SetBinContent(60,0.0);
  S7_DELTAR_0->SetBinContent(61,0.0);
  S7_DELTAR_0->SetBinContent(62,0.0);
  S7_DELTAR_0->SetBinContent(63,0.0);
  S7_DELTAR_0->SetBinContent(64,0.0);
  S7_DELTAR_0->SetBinContent(65,0.0);
  S7_DELTAR_0->SetBinContent(66,0.0);
  S7_DELTAR_0->SetBinContent(67,0.0);
  S7_DELTAR_0->SetBinContent(68,0.0);
  S7_DELTAR_0->SetBinContent(69,0.0);
  S7_DELTAR_0->SetBinContent(70,0.0);
  S7_DELTAR_0->SetBinContent(71,0.0);
  S7_DELTAR_0->SetBinContent(72,0.0);
  S7_DELTAR_0->SetBinContent(73,0.0);
  S7_DELTAR_0->SetBinContent(74,0.0);
  S7_DELTAR_0->SetBinContent(75,0.0);
  S7_DELTAR_0->SetBinContent(76,0.0); // overflow
  S7_DELTAR_0->SetEntries(9999);
  // Style
  S7_DELTAR_0->SetLineColor(9);
  S7_DELTAR_0->SetLineStyle(1);
  S7_DELTAR_0->SetLineWidth(1);
  S7_DELTAR_0->SetFillColor(9);
  S7_DELTAR_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_14","mystack");
  stack->Add(S7_DELTAR_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 40.0 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("#DeltaR [ j_{1} , j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_6.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_6.eps");

}
