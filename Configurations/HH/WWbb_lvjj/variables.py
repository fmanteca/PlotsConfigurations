# variables

#variables = {}
    
   
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }
    
#variables['nvtx']  = {   'name': 'nvtx',      
                        #'range' : (40,0,40),  
                        #'xaxis' : 'nvtx', 
                         #'fold' : 3
                      #}
                        
variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (40, 0,200),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }

#variables['mllpeak'] = {   'name': 'mll',            #   variable name
                           #'range' : (100,80,100),    #   variable range
                           #'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           #'fold' : 0
                        #}

#variables['mth']  = {   'name': 'mth',            #   variable name    
                        #'range' : (40,0,200),    #   variable range
                        #'xaxis' : 'm_{T}^{H} [GeV]',  #   x axis name
                         #'fold' : 0
                        #}

#variables['dphill']  = {   'name': 'abs(dphill)',     
                        #'range' : (20,0,3.14),   
                        #'xaxis' : '#Delta#phi_{ll}',
                        #'fold' : 3
                        #}

#variables['ptll']  = {   'name': 'ptll',     
                        #'range' : (40, 0,200),   
                        #'xaxis' : 'p_{T}^{ll} [GeV]',
                        #'fold' : 3
                        #}

variables['pt1']  = {   'name': 'std_vector_lepton_pt[0]',     
                        'range' : (10,20,200),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 2                         
                        }

variables['pt2']  = {   'name': 'std_vector_lepton_pt[1]',     
                        'range' : (10,0,100),   
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 0                         
                        }

variables['njets'] =  {
		'name': 'njet',
		'range': (10,0,10),
		'xaxis': '# jets',
		'fold': 3	
	}

variables['nlep'] =  {
                'name': '1*(std_vector_lepton_pt[0]>20) + 1*(std_vector_lepton_pt[1]>20) + 1*(std_vector_lepton_pt[2]>20)+ 1*(std_vector_lepton_pt[3]>20) + 1*(std_vector_lepton_pt[4]>20)',
                'range': (5,0,5),
                'xaxis': '# leptons',
                'fold': 3
        }

#variables['pt3']  = {   'name': 'std_vector_lepton_pt[2]',     
                        #'range' : (10,0,50),   
                        #'xaxis' : 'p_{T} 3rd lep',
                        #'fold'  : 3                         
                        #}

variables['eta1']  = {  'name': 'std_vector_lepton_eta[0]',     
                        'range' : (10,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 0                         
                        }

variables['eta2']  = {  'name': 'std_vector_lepton_eta[1]',     
                        'range' : (10,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 0                         
                        }

#variables['eta1large']  = {  'name': 'std_vector_lepton_eta[0]',
                       #'range' : ([-2.4, -2.1, -1.6, -1.2, -0.8, -0.3, -0.2, 0.2, 0.3, 0.8, 1.2, 1.6, 2.1, 2.4,],),
                       #'xaxis' : '#eta 1st lep',
                       #'fold'  : 3
                       #}

#variables['eta2large']  = {  'name': 'std_vector_lepton_eta[1]',
                       #'range' : ([-2.4, -2.1, -1.6, -1.2, -0.8, -0.3, -0.2, 0.2, 0.3, 0.8, 1.2, 1.6, 2.1, 2.4,],),
                       #'xaxis' : '#eta 2nd lep',
                       #'fold'  : 3
                       #}

#variables['taupt1']  = {'name': 'std_vector_tau_pt[0]',     
                        #'range' : (100,0,200),   
                        #'xaxis' : 'p_{T} 1st tau',
                        #'fold'  : 3                         
                        #}




variables['cmva_1']  = { 
                        'name': 'std_vector_jet_cmvav2[0]',     
                        'range' : (10,-1,1),   
                        'xaxis' : 'cmva jet 1st',
                        'fold'  : 3                         
                        }



variables['cmva_2']  = { 
                        'name': 'std_vector_jet_cmvav2[1]',     
                        'range' : (10,-1,1),   
                        'xaxis' : 'cmva  jet 2nd',
                        'fold'  : 3                         
                        }


variables['cmva_3']  = { 
                        'name': 'std_vector_jet_cmvav2[2]',     
                        'range' : (10,-1,1),   
                        'xaxis' : 'cmva jet 3rd',
                        'fold'  : 3                         
                        }



variables['cmva_4']  = { 
                        'name': 'std_vector_jet_cmvav2[3]',     
                        'range' : (10,-1,1),   
                        'xaxis' : 'cmva  jet 4th',
                        'fold'  : 3                         
                        }

variables['pfmet']  = { 
                        'name': 'metPfType1',     
                        'range' : (20,0,1000),   
                        'xaxis' : 'pfmet [GeV]',
                        'fold'  : 3                         
                        }


#variables['njet']  = {
                        #'name': 'njet',     
                        #'range' : (5,0,5),   
                        #'xaxis' : 'Number of jets',
                        #'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        #}




variables['jetpt1']  = {
                        'name': 'std_vector_jet_pt[0]',     
                        'range' : (10,0,200),   
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt2']  = {
                        'name': 'std_vector_jet_pt[1]',     
                        'range' : (10,0,200),   
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['jetpt3']  = {
                        'name': 'std_vector_jet_pt[2]',     
                        'range' : (10,0,200),   
                        'xaxis' : 'p_{T} 3rd jet',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt4']  = {
                        'name': 'std_vector_jet_pt[3]',     
                        'range' : (10,0,200),   
                        'xaxis' : 'p_{T} 4th jet',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jeteta1']  = {  'name': 'std_vector_jet_eta[0]',
                        'range' : (10,-5.0,5.0),
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 0
                        }

variables['jeteta2']  = {  'name': 'std_vector_jet_eta[1]',
                        'range' : (10,-5.0,5.0),
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 0
                        }


#variables['mtw1']  = {  'name': 'mtw1',
                        #'range' : (40,0,200),
                        #'xaxis' : 'm_{T}^{W_{1}} [GeV]',
                         #'fold' : 3
                        #}

#variables['mtw2']  = {  'name': 'mtw2',
                        #'range' : (40,0,200),
                        #'xaxis' : 'm_{T}^{W_{2}} [GeV]',
                         #'fold' : 3
                        #}

#variables['trkMet']  = {   'name': 'metTtrk',
                        #'range' : (40,0,200),
                        #'xaxis' : 'trk met [GeV]',
                         #'fold' : 3
                        #}

#variables['mpmet']  = { 'name': 'mpmet',
                        #'range' : (40,0,200),
                        #'xaxis' : 'min proj met [GeV]',
                        #'fold' : 3
                        #}

#variables['dymvaggh']  = { 'name': 'dymvaggh',
                        #'range' : (40,-1,1),
                        #'xaxis' : 'DY MVA',
                        #'fold' : 3
                        #}

#variables['dymvavbf']  = { 'name': 'dymvavbf',
                        #'range' : (40,-1,1),
                        #'xaxis' : 'DY MVA',
                        #'fold' : 3
                        #}


variables['mjj']  = {   
			'name': 'mjj',            #   variable name    
                        'range' : (-100, 0,3000),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                         'fold' : 0
                        }
