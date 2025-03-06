![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateTransition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateTransition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the transition.

_sourceStateId_
    The Id of the source state.

_targetStateId_
    The Id of the target state.

Glossary Item Box

Creates a transaction which, when committed, will create an transition with a given name from given source state to target state. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateTransition( _
       ByVal _name_ As String, _
       ByVal _sourceStateId_ As Guid, _
       ByVal _targetStateId_ As Guid _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim name As String
    Dim sourceStateId As Guid
    Dim targetStateId As Guid
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateTransition(name, sourceStateId, targetStateId)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateTransition( 
       string _name_ ,
       Guid _sourceStateId_ ,
       Guid _targetStateId_
    )  
  
#### Parameters

 _name_
    The name of the transition.
_sourceStateId_
    The Id of the source state.
_targetStateId_
    The Id of the target state.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


