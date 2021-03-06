'''
    PyDMET: a python implementation of density matrix embedding theory
    Copyright (C) 2014, 2015 Sebastian Wouters
    
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''

import numpy as np

def SortedEigSymmetric( Mat ):

    eigenvals, eigenvecs = np.linalg.eigh( Mat ) # Does not guarantee sorted eigenvectors!
    idx = eigenvals.argsort()   
    eigenvals = eigenvals[idx]
    eigenvecs = eigenvecs[:,idx]
    return ( eigenvals, eigenvecs )

def RestrictedHartreeFock( OEI, numPairs, printSPgap=False ):
    
    energiesRHF, solutionRHF = SortedEigSymmetric( OEI )
    SPgap = energiesRHF[ numPairs ] - energiesRHF[ numPairs-1 ]
    if ( printSPgap ):
        print "   RHF :: HOMO-LUMO gap =",SPgap
    if ( SPgap < 1e-8 ):
        print "ERROR: The single particle gap is zero!"
    assert( SPgap >= 1e-8 )
    return ( energiesRHF, solutionRHF )
    
