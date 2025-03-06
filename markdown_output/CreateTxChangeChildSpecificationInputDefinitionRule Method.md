![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeChildSpecificationInputDefinitionRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeChildSpecificationInputDefinitionRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_childSpecificationList_
    The ChildSpecificationList the input definition resides in.

_projectDef_
    The ChildSpecificationProjectDef containing the ChildSpecificationInputDef.

_inputDef_
    The ChildSpecificationInputDef who's rule to change.

_newFormula_
    The new formula to apply.

Glossary Item Box

Creates a transaction which, when committed, will change the item rule of the specified ProjectChildSpecificationInputDef 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeChildSpecificationInputDefinitionRule( _
       ByVal _childSpecificationList_ As [ChildSpecificationList](topic7547.md), _
       ByVal _projectDef_ As [ProjectChildSpecificationProjectDef](topic4067.md), _
       ByVal _inputDef_ As [ProjectChildSpecificationInputDef](topic4047.md), _
       ByVal _newFormula_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim childSpecificationList As [ChildSpecificationList](topic7547.md)
    Dim projectDef As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim inputDef As [ProjectChildSpecificationInputDef](topic4047.md)
    Dim newFormula As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeChildSpecificationInputDefinitionRule(childSpecificationList, projectDef, inputDef, newFormula)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeChildSpecificationInputDefinitionRule( 
       [ChildSpecificationList](topic7547.md) _childSpecificationList_ ,
       [ProjectChildSpecificationProjectDef](topic4067.md) _projectDef_ ,
       [ProjectChildSpecificationInputDef](topic4047.md) _inputDef_ ,
       string _newFormula_
    )  
  
#### Parameters

 _childSpecificationList_
    The ChildSpecificationList the input definition resides in.
_projectDef_
    The ChildSpecificationProjectDef containing the ChildSpecificationInputDef.
_inputDef_
    The ChildSpecificationInputDef who's rule to change.
_newFormula_
    The new formula to apply.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


