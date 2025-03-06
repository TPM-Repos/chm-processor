![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRestoreItemList Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxRestoreItemList Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_itemListDefinition_
    The item list to create the backup transaction for.

Glossary Item Box

Creates a new transaction that when executed will restore the state of the item list to when this transaction was created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxRestoreItemList( _
       ByVal _itemListDefinition_ As [ProjectItemListDef](topic4511.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim itemListDefinition As [ProjectItemListDef](topic4511.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRestoreItemList(itemListDefinition)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRestoreItemList( 
       [ProjectItemListDef](topic4511.md) _itemListDefinition_
    )  
  
#### Parameters

 _itemListDefinition_
    The item list to create the backup transaction for.

# ![](dotnetimages/collapse.gif)Remarks

This is a backup transaction.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


