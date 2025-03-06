![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteVariableCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteVariableCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variableCategory_
    The variable category to delete.

_deleteBehavior_
    The behavior to apply when deleting children.

Glossary Item Box

Creates a transaction which, when committed, will delete a variable category. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteVariableCategory( _
       ByVal _variableCategory_ As [ProjectVariableCategory](topic4983.md), _
       ByVal _deleteBehavior_ As [DeleteVariableCategoryBehavior](topic2351.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim variableCategory As [ProjectVariableCategory](topic4983.md)
    Dim deleteBehavior As [DeleteVariableCategoryBehavior](topic2351.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteVariableCategory(variableCategory, deleteBehavior)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteVariableCategory( 
       [ProjectVariableCategory](topic4983.md) _variableCategory_ ,
       [DeleteVariableCategoryBehavior](topic2351.md) _deleteBehavior_
    )  
  
#### Parameters

 _variableCategory_
    The variable category to delete.
_deleteBehavior_
    The behavior to apply when deleting children.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


