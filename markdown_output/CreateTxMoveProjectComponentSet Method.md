Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxMoveProjectComponentSet Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxMoveProjectComponentSet Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldIndex_
    The original index of the component set to move.

_newIndex_
    The new index that the component set is to be moved to.

Glossary Item Box

Creates a transaction that will change a component set's index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxMoveProjectComponentSet( _
       ByVal _oldIndex_ As Integer, _
       ByVal _newIndex_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim oldIndex As Integer
    Dim newIndex As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxMoveProjectComponentSet(oldIndex, newIndex)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxMoveProjectComponentSet( 
       int _oldIndex_ ,
       int _newIndex_
    )  
  
#### Parameters

 _oldIndex_
    The original index of the component set to move.
_newIndex_
    The new index that the component set is to be moved to.

#### Return Value

A transaction that will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


