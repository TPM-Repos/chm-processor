Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeItemListRule Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeItemListRule( _
       ByVal _itemList_ As [ItemList](topic8183.md), _
       ByVal _typeDefinition_ As [ProjectItemListTypeDef](topic4533.md), _
       ByVal _newFormula_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


