void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo9","canvas_plotflow_tempo9",0,0,1000,500);
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
  canvas->SetRightMargin(0.3);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",160,-8.0,8.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,0.0);
  S5_ETA_0->SetBinContent(10,0.0);
  S5_ETA_0->SetBinContent(11,0.0);
  S5_ETA_0->SetBinContent(12,0.0);
  S5_ETA_0->SetBinContent(13,0.0);
  S5_ETA_0->SetBinContent(14,0.0);
  S5_ETA_0->SetBinContent(15,0.0);
  S5_ETA_0->SetBinContent(16,0.0);
  S5_ETA_0->SetBinContent(17,0.0);
  S5_ETA_0->SetBinContent(18,0.0);
  S5_ETA_0->SetBinContent(19,0.0);
  S5_ETA_0->SetBinContent(20,0.0);
  S5_ETA_0->SetBinContent(21,0.0);
  S5_ETA_0->SetBinContent(22,0.0);
  S5_ETA_0->SetBinContent(23,0.0);
  S5_ETA_0->SetBinContent(24,0.0);
  S5_ETA_0->SetBinContent(25,0.0);
  S5_ETA_0->SetBinContent(26,0.0);
  S5_ETA_0->SetBinContent(27,0.0);
  S5_ETA_0->SetBinContent(28,0.0);
  S5_ETA_0->SetBinContent(29,0.0);
  S5_ETA_0->SetBinContent(30,0.0);
  S5_ETA_0->SetBinContent(31,406.56873994);
  S5_ETA_0->SetBinContent(32,406.56873994);
  S5_ETA_0->SetBinContent(33,406.56873994);
  S5_ETA_0->SetBinContent(34,1219.70661982);
  S5_ETA_0->SetBinContent(35,813.13747988);
  S5_ETA_0->SetBinContent(36,813.13747988);
  S5_ETA_0->SetBinContent(37,1219.70661982);
  S5_ETA_0->SetBinContent(38,1219.70661982);
  S5_ETA_0->SetBinContent(39,2845.98157958);
  S5_ETA_0->SetBinContent(40,1219.70661982);
  S5_ETA_0->SetBinContent(41,813.13747988);
  S5_ETA_0->SetBinContent(42,2032.8440997);
  S5_ETA_0->SetBinContent(43,3252.55031952);
  S5_ETA_0->SetBinContent(44,2845.98157958);
  S5_ETA_0->SetBinContent(45,1219.70661982);
  S5_ETA_0->SetBinContent(46,3252.55031952);
  S5_ETA_0->SetBinContent(47,3252.55031952);
  S5_ETA_0->SetBinContent(48,4472.25533934);
  S5_ETA_0->SetBinContent(49,813.13747988);
  S5_ETA_0->SetBinContent(50,2439.41283964);
  S5_ETA_0->SetBinContent(51,2845.98157958);
  S5_ETA_0->SetBinContent(52,4065.6873994);
  S5_ETA_0->SetBinContent(53,4878.82727928);
  S5_ETA_0->SetBinContent(54,6911.67097898);
  S5_ETA_0->SetBinContent(55,5285.39521922);
  S5_ETA_0->SetBinContent(56,6505.09903904);
  S5_ETA_0->SetBinContent(57,8944.51467868);
  S5_ETA_0->SetBinContent(58,10977.3583784);
  S5_ETA_0->SetBinContent(59,10164.2184985);
  S5_ETA_0->SetBinContent(60,11383.9263183);
  S5_ETA_0->SetBinContent(61,7724.80685886);
  S5_ETA_0->SetBinContent(62,9757.65055856);
  S5_ETA_0->SetBinContent(63,6911.67097898);
  S5_ETA_0->SetBinContent(64,6911.67097898);
  S5_ETA_0->SetBinContent(65,5691.96315916);
  S5_ETA_0->SetBinContent(66,7724.80685886);
  S5_ETA_0->SetBinContent(67,4472.25533934);
  S5_ETA_0->SetBinContent(68,6911.67097898);
  S5_ETA_0->SetBinContent(69,7318.23891892);
  S5_ETA_0->SetBinContent(70,5285.39521922);
  S5_ETA_0->SetBinContent(71,4472.25533934);
  S5_ETA_0->SetBinContent(72,6098.5310991);
  S5_ETA_0->SetBinContent(73,4878.82727928);
  S5_ETA_0->SetBinContent(74,2845.98157958);
  S5_ETA_0->SetBinContent(75,3659.11945946);
  S5_ETA_0->SetBinContent(76,1219.70661982);
  S5_ETA_0->SetBinContent(77,1626.27535976);
  S5_ETA_0->SetBinContent(78,3659.11945946);
  S5_ETA_0->SetBinContent(79,1626.27535976);
  S5_ETA_0->SetBinContent(80,1626.27535976);
  S5_ETA_0->SetBinContent(81,1219.70661982);
  S5_ETA_0->SetBinContent(82,1219.70661982);
  S5_ETA_0->SetBinContent(83,406.56873994);
  S5_ETA_0->SetBinContent(84,2845.98157958);
  S5_ETA_0->SetBinContent(85,3659.11945946);
  S5_ETA_0->SetBinContent(86,813.13747988);
  S5_ETA_0->SetBinContent(87,4472.25533934);
  S5_ETA_0->SetBinContent(88,5691.96315916);
  S5_ETA_0->SetBinContent(89,4878.82727928);
  S5_ETA_0->SetBinContent(90,6098.5310991);
  S5_ETA_0->SetBinContent(91,3659.11945946);
  S5_ETA_0->SetBinContent(92,6505.09903904);
  S5_ETA_0->SetBinContent(93,4472.25533934);
  S5_ETA_0->SetBinContent(94,6505.09903904);
  S5_ETA_0->SetBinContent(95,6098.5310991);
  S5_ETA_0->SetBinContent(96,7318.23891892);
  S5_ETA_0->SetBinContent(97,7318.23891892);
  S5_ETA_0->SetBinContent(98,7724.80685886);
  S5_ETA_0->SetBinContent(99,10570.7904384);
  S5_ETA_0->SetBinContent(100,10164.2184985);
  S5_ETA_0->SetBinContent(101,6911.67097898);
  S5_ETA_0->SetBinContent(102,7318.23891892);
  S5_ETA_0->SetBinContent(103,8944.51467868);
  S5_ETA_0->SetBinContent(104,6911.67097898);
  S5_ETA_0->SetBinContent(105,6911.67097898);
  S5_ETA_0->SetBinContent(106,10164.2184985);
  S5_ETA_0->SetBinContent(107,5691.96315916);
  S5_ETA_0->SetBinContent(108,4472.25533934);
  S5_ETA_0->SetBinContent(109,6098.5310991);
  S5_ETA_0->SetBinContent(110,3252.55031952);
  S5_ETA_0->SetBinContent(111,2439.41283964);
  S5_ETA_0->SetBinContent(112,3659.11945946);
  S5_ETA_0->SetBinContent(113,4472.25533934);
  S5_ETA_0->SetBinContent(114,2032.8440997);
  S5_ETA_0->SetBinContent(115,2439.41283964);
  S5_ETA_0->SetBinContent(116,813.13747988);
  S5_ETA_0->SetBinContent(117,2032.8440997);
  S5_ETA_0->SetBinContent(118,813.13747988);
  S5_ETA_0->SetBinContent(119,2032.8440997);
  S5_ETA_0->SetBinContent(120,1626.27535976);
  S5_ETA_0->SetBinContent(121,2032.8440997);
  S5_ETA_0->SetBinContent(122,1219.70661982);
  S5_ETA_0->SetBinContent(123,1626.27535976);
  S5_ETA_0->SetBinContent(124,1219.70661982);
  S5_ETA_0->SetBinContent(125,0.0);
  S5_ETA_0->SetBinContent(126,0.0);
  S5_ETA_0->SetBinContent(127,0.0);
  S5_ETA_0->SetBinContent(128,813.13747988);
  S5_ETA_0->SetBinContent(129,406.56873994);
  S5_ETA_0->SetBinContent(130,813.13747988);
  S5_ETA_0->SetBinContent(131,0.0);
  S5_ETA_0->SetBinContent(132,0.0);
  S5_ETA_0->SetBinContent(133,0.0);
  S5_ETA_0->SetBinContent(134,0.0);
  S5_ETA_0->SetBinContent(135,0.0);
  S5_ETA_0->SetBinContent(136,0.0);
  S5_ETA_0->SetBinContent(137,0.0);
  S5_ETA_0->SetBinContent(138,0.0);
  S5_ETA_0->SetBinContent(139,0.0);
  S5_ETA_0->SetBinContent(140,0.0);
  S5_ETA_0->SetBinContent(141,0.0);
  S5_ETA_0->SetBinContent(142,0.0);
  S5_ETA_0->SetBinContent(143,0.0);
  S5_ETA_0->SetBinContent(144,0.0);
  S5_ETA_0->SetBinContent(145,0.0);
  S5_ETA_0->SetBinContent(146,0.0);
  S5_ETA_0->SetBinContent(147,0.0);
  S5_ETA_0->SetBinContent(148,0.0);
  S5_ETA_0->SetBinContent(149,0.0);
  S5_ETA_0->SetBinContent(150,0.0);
  S5_ETA_0->SetBinContent(151,0.0);
  S5_ETA_0->SetBinContent(152,0.0);
  S5_ETA_0->SetBinContent(153,0.0);
  S5_ETA_0->SetBinContent(154,0.0);
  S5_ETA_0->SetBinContent(155,0.0);
  S5_ETA_0->SetBinContent(156,0.0);
  S5_ETA_0->SetBinContent(157,0.0);
  S5_ETA_0->SetBinContent(158,0.0);
  S5_ETA_0->SetBinContent(159,0.0);
  S5_ETA_0->SetBinContent(160,0.0);
  S5_ETA_0->SetBinContent(161,0.0); // overflow
  S5_ETA_0->SetEntries(999);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S5_ETA_1 = new TH1F("S5_ETA_1","S5_ETA_1",160,-8.0,8.0);
  // Content
  S5_ETA_1->SetBinContent(0,0.0); // underflow
  S5_ETA_1->SetBinContent(1,0.0);
  S5_ETA_1->SetBinContent(2,0.0);
  S5_ETA_1->SetBinContent(3,0.0);
  S5_ETA_1->SetBinContent(4,0.0);
  S5_ETA_1->SetBinContent(5,0.0);
  S5_ETA_1->SetBinContent(6,0.0);
  S5_ETA_1->SetBinContent(7,0.0);
  S5_ETA_1->SetBinContent(8,0.0);
  S5_ETA_1->SetBinContent(9,0.0);
  S5_ETA_1->SetBinContent(10,0.0);
  S5_ETA_1->SetBinContent(11,0.0);
  S5_ETA_1->SetBinContent(12,0.0);
  S5_ETA_1->SetBinContent(13,0.0);
  S5_ETA_1->SetBinContent(14,0.0);
  S5_ETA_1->SetBinContent(15,0.0);
  S5_ETA_1->SetBinContent(16,0.0);
  S5_ETA_1->SetBinContent(17,0.0);
  S5_ETA_1->SetBinContent(18,0.0);
  S5_ETA_1->SetBinContent(19,0.0);
  S5_ETA_1->SetBinContent(20,0.0);
  S5_ETA_1->SetBinContent(21,0.0);
  S5_ETA_1->SetBinContent(22,0.0);
  S5_ETA_1->SetBinContent(23,0.0);
  S5_ETA_1->SetBinContent(24,0.0);
  S5_ETA_1->SetBinContent(25,0.0);
  S5_ETA_1->SetBinContent(26,0.0);
  S5_ETA_1->SetBinContent(27,0.0);
  S5_ETA_1->SetBinContent(28,0.0);
  S5_ETA_1->SetBinContent(29,0.0);
  S5_ETA_1->SetBinContent(30,0.0);
  S5_ETA_1->SetBinContent(31,0.0);
  S5_ETA_1->SetBinContent(32,0.0);
  S5_ETA_1->SetBinContent(33,0.0);
  S5_ETA_1->SetBinContent(34,0.0);
  S5_ETA_1->SetBinContent(35,141.959877152);
  S5_ETA_1->SetBinContent(36,141.959877152);
  S5_ETA_1->SetBinContent(37,0.0);
  S5_ETA_1->SetBinContent(38,141.959877152);
  S5_ETA_1->SetBinContent(39,141.959877152);
  S5_ETA_1->SetBinContent(40,141.959877152);
  S5_ETA_1->SetBinContent(41,0.0);
  S5_ETA_1->SetBinContent(42,141.959877152);
  S5_ETA_1->SetBinContent(43,141.959877152);
  S5_ETA_1->SetBinContent(44,0.0);
  S5_ETA_1->SetBinContent(45,0.0);
  S5_ETA_1->SetBinContent(46,141.959877152);
  S5_ETA_1->SetBinContent(47,283.919809859);
  S5_ETA_1->SetBinContent(48,0.0);
  S5_ETA_1->SetBinContent(49,0.0);
  S5_ETA_1->SetBinContent(50,283.919809859);
  S5_ETA_1->SetBinContent(51,0.0);
  S5_ETA_1->SetBinContent(52,141.959877152);
  S5_ETA_1->SetBinContent(53,283.919809859);
  S5_ETA_1->SetBinContent(54,141.959877152);
  S5_ETA_1->SetBinContent(55,141.959877152);
  S5_ETA_1->SetBinContent(56,141.959877152);
  S5_ETA_1->SetBinContent(57,425.879687011);
  S5_ETA_1->SetBinContent(58,141.959877152);
  S5_ETA_1->SetBinContent(59,0.0);
  S5_ETA_1->SetBinContent(60,283.919809859);
  S5_ETA_1->SetBinContent(61,567.839508607);
  S5_ETA_1->SetBinContent(62,0.0);
  S5_ETA_1->SetBinContent(63,141.959877152);
  S5_ETA_1->SetBinContent(64,141.959877152);
  S5_ETA_1->SetBinContent(65,0.0);
  S5_ETA_1->SetBinContent(66,0.0);
  S5_ETA_1->SetBinContent(67,283.919809859);
  S5_ETA_1->SetBinContent(68,0.0);
  S5_ETA_1->SetBinContent(69,0.0);
  S5_ETA_1->SetBinContent(70,283.919809859);
  S5_ETA_1->SetBinContent(71,0.0);
  S5_ETA_1->SetBinContent(72,0.0);
  S5_ETA_1->SetBinContent(73,141.959877152);
  S5_ETA_1->SetBinContent(74,0.0);
  S5_ETA_1->SetBinContent(75,0.0);
  S5_ETA_1->SetBinContent(76,0.0);
  S5_ETA_1->SetBinContent(77,141.959877152);
  S5_ETA_1->SetBinContent(78,0.0);
  S5_ETA_1->SetBinContent(79,0.0);
  S5_ETA_1->SetBinContent(80,0.0);
  S5_ETA_1->SetBinContent(81,0.0);
  S5_ETA_1->SetBinContent(82,0.0);
  S5_ETA_1->SetBinContent(83,0.0);
  S5_ETA_1->SetBinContent(84,0.0);
  S5_ETA_1->SetBinContent(85,0.0);
  S5_ETA_1->SetBinContent(86,141.959877152);
  S5_ETA_1->SetBinContent(87,141.959877152);
  S5_ETA_1->SetBinContent(88,0.0);
  S5_ETA_1->SetBinContent(89,0.0);
  S5_ETA_1->SetBinContent(90,0.0);
  S5_ETA_1->SetBinContent(91,141.959877152);
  S5_ETA_1->SetBinContent(92,283.919809859);
  S5_ETA_1->SetBinContent(93,0.0);
  S5_ETA_1->SetBinContent(94,425.879687011);
  S5_ETA_1->SetBinContent(95,0.0);
  S5_ETA_1->SetBinContent(96,0.0);
  S5_ETA_1->SetBinContent(97,0.0);
  S5_ETA_1->SetBinContent(98,0.0);
  S5_ETA_1->SetBinContent(99,141.959877152);
  S5_ETA_1->SetBinContent(100,141.959877152);
  S5_ETA_1->SetBinContent(101,141.959877152);
  S5_ETA_1->SetBinContent(102,141.959877152);
  S5_ETA_1->SetBinContent(103,283.919809859);
  S5_ETA_1->SetBinContent(104,425.879687011);
  S5_ETA_1->SetBinContent(105,0.0);
  S5_ETA_1->SetBinContent(106,283.919809859);
  S5_ETA_1->SetBinContent(107,283.919809859);
  S5_ETA_1->SetBinContent(108,141.959877152);
  S5_ETA_1->SetBinContent(109,141.959877152);
  S5_ETA_1->SetBinContent(110,141.959877152);
  S5_ETA_1->SetBinContent(111,141.959877152);
  S5_ETA_1->SetBinContent(112,0.0);
  S5_ETA_1->SetBinContent(113,141.959877152);
  S5_ETA_1->SetBinContent(114,141.959877152);
  S5_ETA_1->SetBinContent(115,0.0);
  S5_ETA_1->SetBinContent(116,141.959877152);
  S5_ETA_1->SetBinContent(117,0.0);
  S5_ETA_1->SetBinContent(118,141.959877152);
  S5_ETA_1->SetBinContent(119,283.919809859);
  S5_ETA_1->SetBinContent(120,0.0);
  S5_ETA_1->SetBinContent(121,0.0);
  S5_ETA_1->SetBinContent(122,141.959877152);
  S5_ETA_1->SetBinContent(123,0.0);
  S5_ETA_1->SetBinContent(124,0.0);
  S5_ETA_1->SetBinContent(125,0.0);
  S5_ETA_1->SetBinContent(126,283.919809859);
  S5_ETA_1->SetBinContent(127,0.0);
  S5_ETA_1->SetBinContent(128,0.0);
  S5_ETA_1->SetBinContent(129,141.959877152);
  S5_ETA_1->SetBinContent(130,0.0);
  S5_ETA_1->SetBinContent(131,0.0);
  S5_ETA_1->SetBinContent(132,0.0);
  S5_ETA_1->SetBinContent(133,0.0);
  S5_ETA_1->SetBinContent(134,0.0);
  S5_ETA_1->SetBinContent(135,0.0);
  S5_ETA_1->SetBinContent(136,0.0);
  S5_ETA_1->SetBinContent(137,0.0);
  S5_ETA_1->SetBinContent(138,0.0);
  S5_ETA_1->SetBinContent(139,0.0);
  S5_ETA_1->SetBinContent(140,0.0);
  S5_ETA_1->SetBinContent(141,0.0);
  S5_ETA_1->SetBinContent(142,0.0);
  S5_ETA_1->SetBinContent(143,0.0);
  S5_ETA_1->SetBinContent(144,0.0);
  S5_ETA_1->SetBinContent(145,0.0);
  S5_ETA_1->SetBinContent(146,0.0);
  S5_ETA_1->SetBinContent(147,0.0);
  S5_ETA_1->SetBinContent(148,0.0);
  S5_ETA_1->SetBinContent(149,0.0);
  S5_ETA_1->SetBinContent(150,0.0);
  S5_ETA_1->SetBinContent(151,0.0);
  S5_ETA_1->SetBinContent(152,0.0);
  S5_ETA_1->SetBinContent(153,0.0);
  S5_ETA_1->SetBinContent(154,0.0);
  S5_ETA_1->SetBinContent(155,0.0);
  S5_ETA_1->SetBinContent(156,0.0);
  S5_ETA_1->SetBinContent(157,0.0);
  S5_ETA_1->SetBinContent(158,0.0);
  S5_ETA_1->SetBinContent(159,0.0);
  S5_ETA_1->SetBinContent(160,0.0);
  S5_ETA_1->SetBinContent(161,0.0); // overflow
  S5_ETA_1->SetEntries(71);
  // Style
  S5_ETA_1->SetLineColor(46);
  S5_ETA_1->SetLineStyle(1);
  S5_ETA_1->SetLineWidth(1);
  S5_ETA_1->SetFillColor(46);
  S5_ETA_1->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_10","mystack");
  stack->Add(S5_ETA_0);
  stack->Add(S5_ETA_1);
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
  stack->GetXaxis()->SetTitle("#eta [ j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S5_ETA_0,"signal1TeV");
  legend->AddEntry(S5_ETA_1,"signal4TeV");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_4.eps");

}
