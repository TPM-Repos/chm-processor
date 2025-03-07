Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateFormControl Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateFormControl Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_parentForm_
    The parent form for the new control.

_parentControl_
    The parent control of the new control, if it is to have one.

_controlType_
    The type of control to create.

_controlName_
    The name to give the control.

Glossary Item Box

Creates a transaction which, when committed, will create a new form control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateFormControl( _
       ByVal _parentForm_ As [Form](topic8086.md), _
       ByVal _parentControl_ As [ContainerControlBase](topic7684.md), _
       ByVal _controlType_ As Type, _
       ByVal _controlName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim parentForm As [Form](topic8086.md)
    Dim parentControl As [ContainerControlBase](topic7684.md)
    Dim controlType As Type
    Dim controlName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateFormControl(parentForm, parentControl, controlType, controlName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateFormControl( 
       [Form](topic8086.md) _parentForm_ ,
       [ContainerControlBase](topic7684.md) _parentControl_ ,
       Type _controlType_ ,
       string _controlName_
    )  
  
#### Parameters

 _parentForm_
    The parent form for the new control.
_parentControl_
    The parent control of the new control, if it is to have one.
_controlType_
    The type of control to create.
_controlName_
    The name to give the control.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


