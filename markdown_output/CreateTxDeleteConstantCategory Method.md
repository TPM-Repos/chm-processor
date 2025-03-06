![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteConstantCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteConstantCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constantCategory_
    The constant category to delete.

_deleteBehaviour_
    The behaviour to apply when deleting children.

Glossary Item Box

Creates a transaction which, when committed, will delete a constant category. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteConstantCategory( _
       ByVal _constantCategory_ As [ProjectConstantCategory](topic4219.md), _
       ByVal _deleteBehaviour_ As [DeleteConstantCategoryBehavior](topic2349.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim constantCategory As [ProjectConstantCategory](topic4219.md)
    Dim deleteBehaviour As [DeleteConstantCategoryBehavior](topic2349.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteConstantCategory(constantCategory, deleteBehaviour)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteConstantCategory( 
       [ProjectConstantCategory](topic4219.md) _constantCategory_ ,
       [DeleteConstantCategoryBehavior](topic2349.md) _deleteBehaviour_
    )  
  
#### Parameters

 _constantCategory_
    The constant category to delete.
_deleteBehaviour_
    The behaviour to apply when deleting children.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


