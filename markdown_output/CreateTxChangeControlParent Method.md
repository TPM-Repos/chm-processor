Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeControlParent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeControlParent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlToMove_
    The control to change the parent of.

_newParent_
    The new parent for the specified control.

Glossary Item Box

Creates a new transaction that when executed will change the parent of the specified control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeControlParent( _
       ByVal _controlToMove_ As [ControlBase](topic7698.md), _
       ByVal _newParent_ As [ContainerControlBase](topic7684.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim controlToMove As [ControlBase](topic7698.md)
    Dim newParent As [ContainerControlBase](topic7684.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeControlParent(controlToMove, newParent)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeControlParent( 
       [ControlBase](topic7698.md) _controlToMove_ ,
       [ContainerControlBase](topic7684.md) _newParent_
    )  
  
#### Parameters

 _controlToMove_
    The control to change the parent of.
_newParent_
    The new parent for the specified control.

#### Return Value

A transaction that will perform the specified action.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


