![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeStateTeams Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13011.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeStateTeams Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The state to update.

_newTeams_
    The list of teams to assign.

_isCreatorPermitted_
    If the creator of the specification is permitted.

_isOwnerPermitted_
    If the owner of the specification is permitted.

_isUniversal_
    If all teams are allowed by the instance.

Glossary Item Box

Creates a transaction which, when committed, will update a state's teams list and properties 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeStateTeams( _
       ByVal _state_ As [State](topic11559.md), _
       ByVal _newTeams_() As String, _
       ByVal _isCreatorPermitted_ As Boolean, _
       ByVal _isOwnerPermitted_ As Boolean, _
       ByVal _isUniversal_ As Boolean _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim state As [State](topic11559.md)
    Dim newTeams() As String
    Dim isCreatorPermitted As Boolean
    Dim isOwnerPermitted As Boolean
    Dim isUniversal As Boolean
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeStateTeams(state, newTeams, isCreatorPermitted, isOwnerPermitted, isUniversal)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeStateTeams( 
       [State](topic11559.md) _state_ ,
       string[] _newTeams_ ,
       bool _isCreatorPermitted_ ,
       bool _isOwnerPermitted_ ,
       bool _isUniversal_
    )  
  
#### Parameters

 _state_
    The state to update.
_newTeams_
    The list of teams to assign.
_isCreatorPermitted_
    If the creator of the specification is permitted.
_isOwnerPermitted_
    If the owner of the specification is permitted.
_isUniversal_
    If all teams are allowed by the instance.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
