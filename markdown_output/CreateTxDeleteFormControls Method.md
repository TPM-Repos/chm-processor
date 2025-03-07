Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteFormControls Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteFormControls Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controls_
    The form controls to delete.

Glossary Item Box

Creates a transaction to delete the given form controls. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteFormControls( _
       ByVal _controls_() As [ControlBase](topic7698.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim controls() As [ControlBase](topic7698.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteFormControls(controls)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteFormControls( 
       [ControlBase](topic7698.md)[] _controls_
    )  
  
#### Parameters

 _controls_
    The form controls to delete.

#### Return Value

A transaction.

# Remarks

The form controls must all belong to the same parent control.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


