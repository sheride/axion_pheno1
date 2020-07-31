#include "SampleAnalyzer/User/Analyzer/user.h"
using namespace MA5;

bool user::Initialize(const MA5::Configuration& cfg,
                      const std::map<std::string,std::string>& parameters)
{
  // Initializing PhysicsService for MC
  PHYSICS->mcConfig().Reset();

  // definition of the multiparticle "hadronic"
  PHYSICS->mcConfig().AddHadronicId(-5);
  PHYSICS->mcConfig().AddHadronicId(-4);
  PHYSICS->mcConfig().AddHadronicId(-3);
  PHYSICS->mcConfig().AddHadronicId(-2);
  PHYSICS->mcConfig().AddHadronicId(-1);
  PHYSICS->mcConfig().AddHadronicId(1);
  PHYSICS->mcConfig().AddHadronicId(2);
  PHYSICS->mcConfig().AddHadronicId(3);
  PHYSICS->mcConfig().AddHadronicId(4);
  PHYSICS->mcConfig().AddHadronicId(5);
  PHYSICS->mcConfig().AddHadronicId(21);

  // definition of the multiparticle "invisible"
  PHYSICS->mcConfig().AddInvisibleId(-16);
  PHYSICS->mcConfig().AddInvisibleId(-14);
  PHYSICS->mcConfig().AddInvisibleId(-12);
  PHYSICS->mcConfig().AddInvisibleId(12);
  PHYSICS->mcConfig().AddInvisibleId(14);
  PHYSICS->mcConfig().AddInvisibleId(16);
  PHYSICS->mcConfig().AddInvisibleId(1000022);

  // ===== Signal region ===== //
  Manager()->AddRegionSelection("myregion");

  // ===== Selections ===== //
  Manager()->AddCut("1_PT ( a[1] ) > 300.0 and M ( a[1] a[2] ) > 500.0");

  // ===== Histograms ===== //
  Manager()->AddHisto("1_E", 200,0.0,3000.0);
  Manager()->AddHisto("2_P", 100,0.0,1000.0);

  // No problem during initialization
  return true;
}

bool user::Execute(SampleFormat& sample, const EventFormat& event)
{
  MAfloat32 __event_weight__ = 1.0;
  if (weighted_events_ && event.mc()!=0) __event_weight__ = event.mc()->weight();

  if (sample.mc()!=0) sample.mc()->addWeightedEvents(__event_weight__);
  Manager()->InitializeForNewEvent(__event_weight__);

  // Clearing particle containers
  {
      _P_a_I1I_PTorderingfinalstate_REG_.clear();
      _P_a_I2I_PTorderingfinalstate_REG_.clear();
      _P_aPTorderingfinalstate_REG_.clear();
  }

  // Filling particle containers
  {
    for (MAuint32 i=0;i<event.mc()->particles().size();i++)
    {
      if (isP__aPTorderingfinalstate((&(event.mc()->particles()[i])))) _P_aPTorderingfinalstate_REG_.push_back(&(event.mc()->particles()[i]));
    }
  }

  // Sorting particles
  // Sorting particle collection according to PTordering
  // for getting 1th particle
  _P_a_I1I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_aPTorderingfinalstate_REG_,1,PTordering);

  // Sorting particle collection according to PTordering
  // for getting 2th particle
  _P_a_I2I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_aPTorderingfinalstate_REG_,2,PTordering);

  // Event selection number 1
  //   * Cut: select PT ( a[1] ) > 300.0 and M ( a[1] a[2] ) > 500.0, regions = []
  {
    std::vector<MAbool> filter(2,false);
    {
    {
      MAuint32 ind[1];
      for (ind[0]=0;ind[0]<_P_a_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
      {
        if (_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]->pt()>300.0) {filter[0]=true; break;}
      }
    }
    }
    {
    {
      MAuint32 ind[2];
      std::vector<std::set<const MCParticleFormat*> > combis;
      for (ind[0]=0;ind[0]<_P_a_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
      {
      for (ind[1]=0;ind[1]<_P_a_I2I_PTorderingfinalstate_REG_.size();ind[1]++)
      {
        if (_P_a_I2I_PTorderingfinalstate_REG_[ind[1]]==_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]) continue;

    // Checking if consistent combination
    std::set<const MCParticleFormat*> mycombi;
    for (MAuint32 i=0;i<2;i++)
    {
      mycombi.insert(_P_a_I1I_PTorderingfinalstate_REG_[ind[i]]);
      mycombi.insert(_P_a_I2I_PTorderingfinalstate_REG_[ind[i]]);
    }
    MAbool matched=false;
    for (MAuint32 i=0;i<combis.size();i++)
      if (combis[i]==mycombi) {matched=true; break;}
    if (matched) continue;
    else combis.push_back(mycombi);

        ParticleBaseFormat q;
        q+=_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]->momentum();
        q+=_P_a_I2I_PTorderingfinalstate_REG_[ind[1]]->momentum();
        if (q.m()>500.0) {filter[1]=true; break;}
      }
      }
    }
    }
    MAbool filter_global = (filter[0] && filter[1]);
    if(!Manager()->ApplyCut(filter_global, "1_PT ( a[1] ) > 300.0 and M ( a[1] a[2] ) > 500.0")) return true;
  }

  // Histogram number 1
  //   * Plot: E ( a[1] a[2] ) 
  {
  {
    MAuint32 ind[2];
    std::vector<std::set<const MCParticleFormat*> > combis;
    for (ind[0]=0;ind[0]<_P_a_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
    for (ind[1]=0;ind[1]<_P_a_I2I_PTorderingfinalstate_REG_.size();ind[1]++)
    {
    if (_P_a_I2I_PTorderingfinalstate_REG_[ind[1]]==_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]) continue;

    // Checking if consistent combination
    std::set<const MCParticleFormat*> mycombi;
    for (MAuint32 i=0;i<2;i++)
    {
      mycombi.insert(_P_a_I1I_PTorderingfinalstate_REG_[ind[i]]);
      mycombi.insert(_P_a_I2I_PTorderingfinalstate_REG_[ind[i]]);
    }
    MAbool matched=false;
    for (MAuint32 i=0;i<combis.size();i++)
      if (combis[i]==mycombi) {matched=true; break;}
    if (matched) continue;
    else combis.push_back(mycombi);

    ParticleBaseFormat q;
    q+=_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]->momentum();
    q+=_P_a_I2I_PTorderingfinalstate_REG_[ind[1]]->momentum();
      Manager()->FillHisto("1_E", q.e());
    }
    }
  }
  }

  // Histogram number 2
  //   * Plot: P ( a[1] a[2] ) 
  {
  {
    MAuint32 ind[2];
    std::vector<std::set<const MCParticleFormat*> > combis;
    for (ind[0]=0;ind[0]<_P_a_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
    for (ind[1]=0;ind[1]<_P_a_I2I_PTorderingfinalstate_REG_.size();ind[1]++)
    {
    if (_P_a_I2I_PTorderingfinalstate_REG_[ind[1]]==_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]) continue;

    // Checking if consistent combination
    std::set<const MCParticleFormat*> mycombi;
    for (MAuint32 i=0;i<2;i++)
    {
      mycombi.insert(_P_a_I1I_PTorderingfinalstate_REG_[ind[i]]);
      mycombi.insert(_P_a_I2I_PTorderingfinalstate_REG_[ind[i]]);
    }
    MAbool matched=false;
    for (MAuint32 i=0;i<combis.size();i++)
      if (combis[i]==mycombi) {matched=true; break;}
    if (matched) continue;
    else combis.push_back(mycombi);

    ParticleBaseFormat q;
    q+=_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]->momentum();
    q+=_P_a_I2I_PTorderingfinalstate_REG_[ind[1]]->momentum();
      Manager()->FillHisto("2_P", q.p());
    }
    }
  }
  }

  return true;
}

void user::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}