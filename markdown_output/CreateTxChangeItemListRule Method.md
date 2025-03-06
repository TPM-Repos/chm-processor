![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeItemListRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12980.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeItemListRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_itemList_
    The ItemList the Type definition resides in.

_typeDefinition_
    The name of the type definition whose rule to change.

_newFormula_
    The new formula to apply.

Glossary Item Box

Creates a transaction which, when committed, will change the item rule of the specified ProjectItemListTypeDef 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeItemListRule( _
       ByVal _itemList_ As [ItemList](topic8183.md), _
       ByVal _typeDefinition_ As [ProjectItemListTypeDef](topic4533.md), _
       ByVal _newFormula_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim itemList As [ItemList](topic8183.md)
    Dim typeDefinition As [ProjectItemListTypeDef](topic4533.md)
    Dim newFormula As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeItemListRule(itemList, typeDefinition, newFormula)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeItemListRule( 
       [ItemList](topic8183.md) _itemList_ ,
       [ProjectItemListTypeDef](topic4533.md) _typeDefinition_ ,
       string _newFormula_
    )  
  
#### Parameters

 _itemList_
    The ItemList the Type definition resides in.
_typeDefinition_
    The name of the type definition whose rule to change.
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

©2024 DriveWorks Ltd. All Rights Reserved.
