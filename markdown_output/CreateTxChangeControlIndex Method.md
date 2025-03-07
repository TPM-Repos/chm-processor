Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeControlIndex Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeControlIndex Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The form control to move.

_newIndex_
    The new index for the form control.

Glossary Item Box

Creates a transaction to change the index of the given form control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeControlIndex( _
       ByVal _control_ As [ControlBase](topic7698.md), _
       ByVal _newIndex_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim control As [ControlBase](topic7698.md)
    Dim newIndex As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeControlIndex(control, newIndex)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeControlIndex( 
       [ControlBase](topic7698.md) _control_ ,
       int _newIndex_
    )  
  
#### Parameters

 _control_
    The form control to move.
_newIndex_
    The new index for the form control.

#### Return Value

A transaction.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


