Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeTransitionTeams Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeTransitionTeams Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transition_
    The transition to update.

_newTeams_
    The list of teams to assign.

_isCreatorPermitted_
    If the creator of the specification is permitted.

_isOwnerPermitted_
    If the owner of the specification is permitted.

_isUniversal_
    If all teams are allowed by the instance.

Glossary Item Box

Creates a transaction which, when committed, will update a transition's teams list and properties 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeTransitionTeams( _
       ByVal _transition_ As [Transition](topic11757.md), _
       ByVal _newTeams_() As String, _
       ByVal _isCreatorPermitted_ As Boolean, _
       ByVal _isOwnerPermitted_ As Boolean, _
       ByVal _isUniversal_ As Boolean _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim transition As [Transition](topic11757.md)
    Dim newTeams() As String
    Dim isCreatorPermitted As Boolean
    Dim isOwnerPermitted As Boolean
    Dim isUniversal As Boolean
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeTransitionTeams(transition, newTeams, isCreatorPermitted, isOwnerPermitted, isUniversal)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeTransitionTeams( 
       [Transition](topic11757.md) _transition_ ,
       string[] _newTeams_ ,
       bool _isCreatorPermitted_ ,
       bool _isOwnerPermitted_ ,
       bool _isUniversal_
    )  
  
#### Parameters

 _transition_
    The transition to update.
_newTeams_
    The list of teams to assign.
_isCreatorPermitted_
    If the creator of the specification is permitted.
_isOwnerPermitted_
    If the owner of the specification is permitted.
_isUniversal_
    If all teams are allowed by the instance.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


